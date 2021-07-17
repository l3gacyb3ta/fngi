from ctypes import c_uint8 as U8
from ctypes import c_uint16 as U16
from ctypes import c_uint32 as U32
from ctypes import c_uint64 as U64
from ctypes import c_int8 as I8
from ctypes import c_int16 as I16
from ctypes import c_int32 as I32
from ctypes import c_int64 as I64
from ctypes import c_float as F32
from ctypes import c_double as F64

class WasmNamespace: pass

Wlocal = WasmNamespace()
Wglobal = WasmNamespace()
Wi32 = WasmNamespace()
Wi64 = WasmNamespace()
Wf32 = WasmNamespace()
Wf64 = WasmNamespace()
Wmemory = WasmNamespace()

# A.6 Index of Types
WTidx = 0x10ad
WTi32 = 0x7f
WTi64 = 0x7e
WTf32 = 0x7d
WTf64 = 0x7c
WTelement = 0x70
WTfunction = 0x60
WTresult = 0x40

# A.7 Index of Instructions
Wunreachable = 0x0
Wnop = 0x1
Wblock = 0x2
Wloop = 0x3
Wif = 0x4
Welse = 0x5
Wend = 0xb
Wbr = 0xc
Wbr_if = 0xd
Wbr_table = 0xe
Wreturn = 0xf
Wcall = 0x10
Wcall_indirect = 0x11
Wdrop = 0x1a
Wselect = 0x1b
Wlocal.get = 0x20
Wlocal.set = 0x21
Wlocal.tee = 0x22
Wglobal.get = 0x23
Wglobal.set = 0x24
Wi32.load = 0x28
Wi64.load = 0x29
Wf32.load = 0x2a
Wf64.load = 0x2b
Wi32.load8_s = 0x2c
Wi32.load8_u = 0x2d
Wi32.load16_s = 0x2e
Wi32.load16_u = 0x2f
Wi64.load8_s = 0x30
Wi64.load8_u = 0x31
Wi64.load16_s = 0x32
Wi64.load16_u = 0x33
Wi64.load32_s = 0x34
Wi64.load32_u = 0x35
Wi32.store = 0x36
Wi64.store = 0x37
Wf32.store = 0x38
Wf64.store = 0x39
Wi32.store8 = 0x3a
Wi32.store16 = 0x3b
Wi64.store8 = 0x3c
Wi64.store16 = 0x3d
Wi64.store32 = 0x3e
Wmemory.size = 0x3f
Wmemory.grow = 0x40
Wi32.const = 0x41
Wi64.const = 0x42
Wf32.const = 0x43
Wf64.const = 0x44
Wi32.eqz = 0x45
Wi32.eq = 0x46
Wi32.ne = 0x47
Wi32.lt_s = 0x48
Wi32.lt_u = 0x49
Wi32.gt_s = 0x4a
Wi32.gt_u = 0x4b
Wi32.le_s = 0x4c
Wi32.le_u = 0x4d
Wi32.ge_s = 0x4e
Wi32.ge_u = 0x4f
Wi64.eqz = 0x50
Wi64.eq = 0x51
Wi64.ne = 0x52
Wi64.lt_s = 0x53
Wi64.lt_u = 0x54
Wi64.gt_s = 0x55
Wi64.gt_u = 0x56
Wi64.le_s = 0x57
Wi64.le_u = 0x58
Wi64.ge_s = 0x59
Wi64.ge_u = 0x5a
Wf32.eq = 0x5b
Wf32.ne = 0x5c
Wf32.lt = 0x5d
Wf32.gt = 0x5e
Wf32.le = 0x5f
Wf32.ge = 0x60
Wf64.eq = 0x61
Wf64.ne = 0x62
Wf64.lt = 0x63
Wf64.gt = 0x64
Wf64.le = 0x65
Wf64.ge = 0x66
Wi32.clz = 0x67
Wi32.ctz = 0x68
Wi32.popcnt = 0x69
Wi32.add = 0x6a
Wi32.sub = 0x6b
Wi32.mul = 0x6c
Wi32.div_s = 0x6d
Wi32.div_u = 0x6e
Wi32.rem_s = 0x6f
Wi32.rem_u = 0x70
Wi32.and_ = 0x71
Wi32.or_ = 0x72
Wi32.xor = 0x73
Wi32.shl = 0x74
Wi32.shr_s = 0x75
Wi32.shr_u = 0x76
Wi32.rotl = 0x77
Wi32.rotr = 0x78
Wi64.clz = 0x79
Wi64.ctz = 0x7a
Wi64.popcnt = 0x7b
Wi64.add = 0x7c
Wi64.sub = 0x7d
Wi64.mul = 0x7e
Wi64.div_s = 0x7f
Wi64.div_u = 0x80
Wi64.rem_s = 0x81
Wi64.rem_u = 0x82
Wi64.and_ = 0x83
Wi64.or_ = 0x84
Wi64.xor = 0x85
Wi64.shl = 0x86
Wi64.shr_s = 0x87
Wi64.shr_u = 0x88
Wi64.rotl = 0x89
Wi64.rotr = 0x8a
Wf32.abs = 0x8b
Wf32.neg = 0x8c
Wf32.ceil = 0x8d
Wf32.floor = 0x8e
Wf32.trunc = 0x8f
Wf32.nearest = 0x90
Wf32.sqrt = 0x91
Wf32.add = 0x92
Wf32.sub = 0x93
Wf32.mul = 0x94
Wf32.div = 0x95
Wf32.min = 0x96
Wf32.max = 0x97
Wf32.copysign = 0x98
Wf64.abs = 0x99
Wf64.neg = 0x9a
Wf64.ceil = 0x9b
Wf64.floor = 0x9c
Wf64.trunc = 0x9d
Wf64.nearest = 0x9e
Wf64.sqrt = 0x9f
Wf64.add = 0xa0
Wf64.sub = 0xa1
Wf64.mul = 0xa2
Wf64.div = 0xa3
Wf64.min = 0xa4
Wf64.max = 0xa5
Wf64.copysign = 0xa6
Wi32.wrap_i64 = 0xa7
Wi32.trunc_f32_s = 0xa8
Wi32.trunc_f32_u = 0xa9
Wi32.trunc_f64_s = 0xaa
Wi32.trunc_f64_u = 0xab
Wi64.extend_i32_s = 0xac
Wi64.extend_i32_u = 0xad
Wi64.trunc_f32_s = 0xae
Wi64.trunc_f32_u = 0xaf
Wi64.trunc_f64_s = 0xb0
Wi64.trunc_f64_u = 0xb1
Wf32.convert_i32_s = 0xb2
Wf32.convert_i32_u = 0xb3
Wf32.convert_i64_s = 0xb4
Wf32.convert_i64_u = 0xb5
Wf32.demote_f64 = 0xb6
Wf64.convert_i32_s = 0xb7
Wf64.convert_i32_u = 0xb8
Wf64.convert_i64_s = 0xb9
Wf64.convert_i64_u = 0xba
Wf64.promote_f32 = 0xbb
Wi32.reinterpret_f32 = 0xbc
Wi64.reinterpret_f64 = 0xbd
Wf32.reinterpret_i32 = 0xbe
Wf64.reinterpret_i64 = 0xbf

# Name Lookup Dict (for debugging)
wasmName = {
  Wunreachable: 'unreachable',
  Wnop: 'nop',
  Wblock: 'block',
  Wloop: 'loop',
  Wif: 'if',
  Welse: 'else',
  Wend: 'end',
  Wbr: 'br',
  Wbr_if: 'br_if',
  Wbr_table: 'br_table',
  Wreturn: 'return',
  Wcall: 'call',
  Wcall_indirect: 'call_indirect',
  Wdrop: 'drop',
  Wselect: 'select',
  Wlocal.get: 'local.get',
  Wlocal.set: 'local.set',
  Wlocal.tee: 'local.tee',
  Wglobal.get: 'global.get',
  Wglobal.set: 'global.set',
  Wi32.load: 'i32.load',
  Wi64.load: 'i64.load',
  Wf32.load: 'f32.load',
  Wf64.load: 'f64.load',
  Wi32.load8_s: 'i32.load8_s',
  Wi32.load8_u: 'i32.load8_u',
  Wi32.load16_s: 'i32.load16_s',
  Wi32.load16_u: 'i32.load16_u',
  Wi64.load8_s: 'i64.load8_s',
  Wi64.load8_u: 'i64.load8_u',
  Wi64.load16_s: 'i64.load16_s',
  Wi64.load16_u: 'i64.load16_u',
  Wi64.load32_s: 'i64.load32_s',
  Wi64.load32_u: 'i64.load32_u',
  Wi32.store: 'i32.store',
  Wi64.store: 'i64.store',
  Wf32.store: 'f32.store',
  Wf64.store: 'f64.store',
  Wi32.store8: 'i32.store8',
  Wi32.store16: 'i32.store16',
  Wi64.store8: 'i64.store8',
  Wi64.store16: 'i64.store16',
  Wi64.store32: 'i64.store32',
  Wmemory.size: 'memory.size',
  Wmemory.grow: 'memory.grow',
  Wi32.const: 'i32.const',
  Wi64.const: 'i64.const',
  Wf32.const: 'f32.const',
  Wf64.const: 'f64.const',
  Wi32.eqz: 'i32.eqz',
  Wi32.eq: 'i32.eq',
  Wi32.ne: 'i32.ne',
  Wi32.lt_s: 'i32.lt_s',
  Wi32.lt_u: 'i32.lt_u',
  Wi32.gt_s: 'i32.gt_s',
  Wi32.gt_u: 'i32.gt_u',
  Wi32.le_s: 'i32.le_s',
  Wi32.le_u: 'i32.le_u',
  Wi32.ge_s: 'i32.ge_s',
  Wi32.ge_u: 'i32.ge_u',
  Wi64.eqz: 'i64.eqz',
  Wi64.eq: 'i64.eq',
  Wi64.ne: 'i64.ne',
  Wi64.lt_s: 'i64.lt_s',
  Wi64.lt_u: 'i64.lt_u',
  Wi64.gt_s: 'i64.gt_s',
  Wi64.gt_u: 'i64.gt_u',
  Wi64.le_s: 'i64.le_s',
  Wi64.le_u: 'i64.le_u',
  Wi64.ge_s: 'i64.ge_s',
  Wi64.ge_u: 'i64.ge_u',
  Wf32.eq: 'f32.eq',
  Wf32.ne: 'f32.ne',
  Wf32.lt: 'f32.lt',
  Wf32.gt: 'f32.gt',
  Wf32.le: 'f32.le',
  Wf32.ge: 'f32.ge',
  Wf64.eq: 'f64.eq',
  Wf64.ne: 'f64.ne',
  Wf64.lt: 'f64.lt',
  Wf64.gt: 'f64.gt',
  Wf64.le: 'f64.le',
  Wf64.ge: 'f64.ge',
  Wi32.clz: 'i32.clz',
  Wi32.ctz: 'i32.ctz',
  Wi32.popcnt: 'i32.popcnt',
  Wi32.add: 'i32.add',
  Wi32.sub: 'i32.sub',
  Wi32.mul: 'i32.mul',
  Wi32.div_s: 'i32.div_s',
  Wi32.div_u: 'i32.div_u',
  Wi32.rem_s: 'i32.rem_s',
  Wi32.rem_u: 'i32.rem_u',
  Wi32.and_: 'i32.and',
  Wi32.or_: 'i32.or',
  Wi32.xor: 'i32.xor',
  Wi32.shl: 'i32.shl',
  Wi32.shr_s: 'i32.shr_s',
  Wi32.shr_u: 'i32.shr_u',
  Wi32.rotl: 'i32.rotl',
  Wi32.rotr: 'i32.rotr',
  Wi64.clz: 'i64.clz',
  Wi64.ctz: 'i64.ctz',
  Wi64.popcnt: 'i64.popcnt',
  Wi64.add: 'i64.add',
  Wi64.sub: 'i64.sub',
  Wi64.mul: 'i64.mul',
  Wi64.div_s: 'i64.div_s',
  Wi64.div_u: 'i64.div_u',
  Wi64.rem_s: 'i64.rem_s',
  Wi64.rem_u: 'i64.rem_u',
  Wi64.and_: 'i64.and',
  Wi64.or_: 'i64.or',
  Wi64.xor: 'i64.xor',
  Wi64.shl: 'i64.shl',
  Wi64.shr_s: 'i64.shr_s',
  Wi64.shr_u: 'i64.shr_u',
  Wi64.rotl: 'i64.rotl',
  Wi64.rotr: 'i64.rotr',
  Wf32.abs: 'f32.abs',
  Wf32.neg: 'f32.neg',
  Wf32.ceil: 'f32.ceil',
  Wf32.floor: 'f32.floor',
  Wf32.trunc: 'f32.trunc',
  Wf32.nearest: 'f32.nearest',
  Wf32.sqrt: 'f32.sqrt',
  Wf32.add: 'f32.add',
  Wf32.sub: 'f32.sub',
  Wf32.mul: 'f32.mul',
  Wf32.div: 'f32.div',
  Wf32.min: 'f32.min',
  Wf32.max: 'f32.max',
  Wf32.copysign: 'f32.copysign',
  Wf64.abs: 'f64.abs',
  Wf64.neg: 'f64.neg',
  Wf64.ceil: 'f64.ceil',
  Wf64.floor: 'f64.floor',
  Wf64.trunc: 'f64.trunc',
  Wf64.nearest: 'f64.nearest',
  Wf64.sqrt: 'f64.sqrt',
  Wf64.add: 'f64.add',
  Wf64.sub: 'f64.sub',
  Wf64.mul: 'f64.mul',
  Wf64.div: 'f64.div',
  Wf64.min: 'f64.min',
  Wf64.max: 'f64.max',
  Wf64.copysign: 'f64.copysign',
  Wi32.wrap_i64: 'i32.wrap_i64',
  Wi32.trunc_f32_s: 'i32.trunc_f32_s',
  Wi32.trunc_f32_u: 'i32.trunc_f32_u',
  Wi32.trunc_f64_s: 'i32.trunc_f64_s',
  Wi32.trunc_f64_u: 'i32.trunc_f64_u',
  Wi64.extend_i32_s: 'i64.extend_i32_s',
  Wi64.extend_i32_u: 'i64.extend_i32_u',
  Wi64.trunc_f32_s: 'i64.trunc_f32_s',
  Wi64.trunc_f32_u: 'i64.trunc_f32_u',
  Wi64.trunc_f64_s: 'i64.trunc_f64_s',
  Wi64.trunc_f64_u: 'i64.trunc_f64_u',
  Wf32.convert_i32_s: 'f32.convert_i32_s',
  Wf32.convert_i32_u: 'f32.convert_i32_u',
  Wf32.convert_i64_s: 'f32.convert_i64_s',
  Wf32.convert_i64_u: 'f32.convert_i64_u',
  Wf32.demote_f64: 'f32.demote_f64',
  Wf64.convert_i32_s: 'f64.convert_i32_s',
  Wf64.convert_i32_u: 'f64.convert_i32_u',
  Wf64.convert_i64_s: 'f64.convert_i64_s',
  Wf64.convert_i64_u: 'f64.convert_i64_u',
  Wf64.promote_f32: 'f64.promote_f32',
  Wi32.reinterpret_f32: 'i32.reinterpret_f32',
  Wi64.reinterpret_f64: 'i64.reinterpret_f64',
  Wf32.reinterpret_i32: 'f32.reinterpret_i32',
  Wf64.reinterpret_i64: 'f64.reinterpret_i64',
}