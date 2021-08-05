from dataclasses import dataclass
from .wasm import *
import inspect

@dataclass
class RefTy:
    ty: 'Ty'

def fsizeof(ty: 'Ty'):
    if isinstance(ty, DataTy) or (
            inspect.isclass(ty) and issubclass(ty, DataTy)):
        return sizeof(ty)
    elif isinstance(ty, StructTy):
        return ty.size
    elif isinstance(ty, RefTy):
        return sizeof(Ptr)
    else:
        raise ValueError(f"Has no size: {ty}")

def alignField(offset: int, ty: DataTy):
    """Calculate correct offset for dataTy."""
    size = fsizeof(ty)
    if size == 0: raise TypeError("Zero sized type: " + str(ty))
    alignment = min(4, size)
    if alignment == 3: alignment = 4

    mod = offset % alignment
    if mod == 0: return offset
    return offset + (alignment - mod)

def calcOffsetsAndSize(fields: List[DataTy]):
    offset = 0
    offsets = []
    for ty in fields:
        offset = alignField(offset, ty)
        offsets.append(offset)
        offset += fsizeof(ty)
    return offsets, offset

@dataclass
class Field:
    name: str
    ty: DataTy
    index: int
    offset: int

def assertAllStkTypes(tys):
    for ty in tys:
        assert ty in {I32, I64, F32, F64}


class StructTy:
    """Create a struct data type from core types."""

    def __init__(self, fields: List[Tuple[str, DataTy]], isStk=False):
        self.isStk = isStk
        self.names = list(map(operator.itemgetter(0), fields))
        self.tys = list(map(operator.itemgetter(1), fields))
        self.offsets, self.size = calcOffsetsAndSize(self.tys)
        self.fields = {}
        for i in range(len(self.names)):
            name = self.names[i]
            self.fields[name] = Field(
                name=name,
                ty=self.tys[i],
                index=i,
                offset=self.offsets[i],
            )

        if isStk: assertAllStkTypes(self.tys)

    def field(self, key: str):
        """Return the field given a '.' separated key.

        For use with nested structs.
        """
        st = self
        field = None
        try:
            for k in key.split('.'):
                field = st.fields[k]
                st = field.ty
        except KeyError as e:
            raise KeyError(f"{key}: {e}")
        return field

    def offset(self, key: str):
        st = self
        offset = 0
        try:
            for k in key.split('.'):
                field = st.fields[k]
                offset += field.offset
                st = field.ty
        except KeyError as e:
            raise KeyError(f"{key}: {e}")
        return offset

    def ty(self, key: str):
        return self.field(key).ty

    def __getitem__(self, item):
        return self.fields[item]

def testStruct():
    a = StructTy([
        ('a1', U32),
        ('a2', U8),
        ('a3', U16),
        ('a4', U64),
    ])
    assert 0 == a['a1'].offset
    assert 4 == a['a2'].offset
    assert 6 == a['a3'].offset
    assert 8 == a['a4'].offset

    b = StructTy([
        ('u8', U8),
        ('a', a),
    ])
    assert 0 == b['u8'].offset
    assert 4 == b['a'].offset
    assert 4 == b.offset('a.a1')
    assert 8 == b.offset('a.a2')


class FnStructTy(StructTy):
    """A struct specifically for keeping track of function data. Has fields:
    - wasmTrueLocals: the wasm inputs+locals which are accessed by index.
    - inp: (non stk) input type to the fn.
    - &ret: (non stk) return type from the fn.
    - locals: (non wasm) local variables in the function.

    All of the above types are themselves structs.
    """
    def __init__(
            self,
            wasmTrueLocals: List[DataTy],
            inp: StructTy,
            ret: RefTy,
            locals_: StructTy):
        wasmTrueLocals = StructTy(
            fields=[(None, ty) for ty in wasmTrueLocals],
            isStk=True)
        fields = [
            ('wasmTrueLocals', wasmTrueLocals),
            ('inp', inp),
            ('ret', ret),
            ('locals', locals_),
        ]
        return super().__init__(fields)

    def wasmLocalOffset(self, index):
        return self.wasmTrueLocals.offset + self.wasmTrueLocals.offsets[index]

    @property
    def wasmTrueLocals(self): return self.fields['wasmTrueLocals']

    @property
    def inp(self): return self.fields['inp']

    @property
    def ret(self): return self.fields['ret']

    @property
    def locals(self): return self.fields['locals']

Ty = Union[DataTy, StructTy, RefTy]