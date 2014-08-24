import numpy

# translated from numpy/lib/src/_compiled_base.c
def _binary_search(key, arr, length):
    imin = 0
    imax = length

    if key > arr[length - 1]:
        return length

    while imin < imax:
        imid = imin + ((imax - imin) >> 1)
        if key >= arr[imid]:
            imin = imid + 1
        else:
            imax = imid

    return imin - 1


# translated from numpy/lib/src/_compiled_base.c
def interp(x, xp, fp, left=None, right=None):
    lenxp = len(xp)
    if lenxp == 0:
        raise ValueError("array of sample points is empty")
    if lenxp != len(fp):
        raise ValueError("fp and xp are not of the same length.")

    afp = numpy.array(fp, dtype=numpy.double, order='C', ndmin=1)
    axp = numpy.array(xp, dtype=numpy.double, order='C', ndmin=1)
    ax = numpy.array(x, dtype=numpy.double, order='C', ndmin=1)

    af = numpy.array(x, dtype=numpy.double)

    dy = afp
    dx = axp
    dz = ax
    dres = af

    if left is not None:
        lval = left
    else:
        lval = dy[0]
    if right is not None:
        rval = right
    else:
        rval = dy[-1]

    for i, el in enumerate(af):
        j = _binary_search(dz[i], dx, lenxp)

        if (j == -1):
            dres[i] = lval
        elif (j == lenxp - 1):
            dres[i] = dy[j]
        elif (j == lenxp):
            dres[i] = rval
        else:
            slope = (dy[j + 1] - dy[j])/(dx[j + 1] - dx[j]);
            dres[i] = slope*(dz[i] - dx[j]) + dy[j];

    return af


for name in '''
_insert add_docstring digitize bincount add_newdoc_ufunc
ravel_multi_index unravel_index packbits unpackbits
'''.split():
    if name not in globals():
        globals()[name] = None
