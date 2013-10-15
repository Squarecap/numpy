from _numpypy.multiarray import *

def _fastCopyAndTranspose(a):
    return a.T.copy()

def copyto(dst, src, casting='same_kind', where=None):
    dst.fill(src)

def set_typeDict(d):
    pass

for name in '''
CLIP WRAP RAISE MAXDIMS ALLOW_THREADS BUFSIZE nditer nested_iters
broadcast empty_like fromiter fromfile frombuffer newbuffer getbuffer
int_asbuffer set_numeric_ops can_cast promote_types
min_scalar_type result_type lexsort compare_chararrays putmask einsum inner
_vec_string datetime_data format_longfloat
datetime_as_string busday_offset busday_count is_busday busdaycalendar
_flagdict flagsobj
'''.split():
    assert name not in globals()
    globals()[name] = None