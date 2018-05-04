
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    from numpy import array
    from numpy import diag
    from numpy import eye
    from numpy import float64
    from numpy import complex64

    from compas.hpc import give_cuda
except ImportError as e:
    pass

try:
    import pycuda
    import pycuda.autoinit
except ImportError as e:
    pass


__author__    = ['Andrew Liew <liew@arch.ethz.ch>']
__copyright__ = 'Copyright 2018, Block Research Group - ETH Zurich'
__license__   = 'MIT License'
__email__     = 'liew@arch.ethz.ch'


__all__ = [
    'diag_cuda',
#     'det_cuda',
    # 'dot_cuda',
#     'eig_cuda',
    'eye_cuda',
]


# def det_cuda(a):

#     """ GPUArray square matrix determinant.

#     Parameters
#     ----------
#     a : gpuarray
#         GPUArray matrix of size (m x m).

#     Returns
#     -------
#     float
#         Determinant of the square matrix.

#     Notes
#     -----
#     - Requires CULA.

#     Examples
#     --------
#     >>> a = det_cuda(give_cuda([[5, -2, 1], [0, 3, -1], [2, 0, 7]]))
#     103

#     """

#     return skcuda.linalg.det(a)


# def dot_cuda(a, b):

#     """ Matrix multiplication of two GPUArrays.

#     Parameters
#     ----------
#     a : gpuarray
#         GPUArray matrix 1 (m x n).
#     b : gpuarray
#         GPUArray matrix 2 (n x o).

#     Returns
#     -------
#     gpuarray
#         [c] = [a][b] of size (m x o)

#     Examples
#     --------
#     >>> a = give_cuda([[0, 1], [2, 3]])
#     >>> b = give_cuda([[0, 1], [1, 0]])
#     >>> c = dot_cuda(a, b)
#     array([[ 1.,  0.],
#            [ 3.,  2.]])

#     >>> type(c)
#     <class 'pycuda.gpuarray.GPUArray'>

#     """

#     return pycuda.gpuarray.dot(a, b)


# # def cuda_eig(a):
# #     """ Matrix Eigenvectors and Eigenvalues of GPUArray.

# #     Notes
# #         - Requires CULA.
# #         - Input GPUArray is a square matrix, either real or complex.

# #     Parameters:
# #         a (gpuarray): GPUArray of a square matrix (m x m).

# #     Returns:
# #         gpuarray: Normalised Eigenvectors (right)
# #         gpuarray: Eigenvalues.

# #     """
# #     vr, w = skcuda.linalg.eig(a)
# #     return vr, w


def diag_cuda(a):

    """ Construct GPUArray diagonal.

    Parameters
    ----------
    a : array, list
        Elements along diagonal.

    Returns
    -------
    gpuarray
        GPUArray with inserted diagonal.

    Examples
    --------
    >>> a = diag_cuda([1, 2, 3])
    array([[ 1.,  0.,  0.],
           [ 0.,  2.,  0.],
           [ 0.,  0.,  3.]])

    >>> type(a)
    <class 'pycuda.gpuarray.GPUArray'>

    """

    return give_cuda(diag(a))


def eye_cuda(n):

    """ Create GPUArray identity matrix (ones on diagonal) of size (n x n).

    Parameters
    ----------
    n : int
        Size of identity matrix (n x n).

    Returns
    -------
    gpuarray
        Identity matrix (n x n) as GPUArray.

    Examples
    --------
    >>> a = eye_cuda(3)
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])

    >>> type(a)
    <class 'pycuda.gpuarray.GPUArray'>

    """

    return give_cuda(eye(n, dtype=float64))


# # from numpy import float64
# # from numpy import ceil

# # from compas.hpc.cuda.math_ import cuda_sqrt
# # from compas.hpc.cuda.math_ import cuda_sum


# # __all__ = [
# #     'cuda_conj',
# #     'cuda_cross',
# #     'cuda_hermitian',
# #     'cuda_inv',
# #     'cuda_normrow',
# #     'cuda_pinv',
# #     'cuda_svd',
# #     'cuda_trace',
# #     'cuda_transpose'
# # ]


# # def cuda_conj(a):
# #     """ Complex conjugate of GPUArray elements.

# #     Parameters:
# #         a (gpu): Complex GPUArray.

# #     Returns:
# #         gpu: The complex conjugate of the GPUArray.

# #     Examples:
# #         a = cuda_conj(cuda_give([1 + 2.j, 3 - 4.j], type='complex'))
# #         array([ 1.-2.j,  3.+4.j], dtype=complex64)
# #         >>> type(a)
# #         <class 'pycuda.gpuarray.GPUArray'>
# #     """
# #     return skcuda.linalg.conj(a)


# # try:
# #     kernel_code_template = """
# #     __global__ void cross_product(float *a, float *b, float *c)
# #     {
# #         int i = threadIdx.x + blockDim.x * blockIdx.x;
# #         int n = 3;
# #         float A1 = a[i * n + 0];
# #         float A2 = a[i * n + 1];
# #         float A3 = a[i * n + 2];
# #         float B1 = b[i * n + 0];
# #         float B2 = b[i * n + 1];
# #         float B3 = b[i * n + 2];
# #         c[i * n + 0] = A2 * B3 - A3 * B2;
# #         c[i * n + 1] = A3 * B1 - A1 * B3;
# #         c[i * n + 2] = A1 * B2 - A2 * B1;
# #     }
# #     """
# #     kernel_code = kernel_code_template % {'m': 3}
# #     mod = pycuda.compiler.SourceModule(kernel_code)
# #     cross_product = mod.get_function("cross_product")
# # except NameError as e:
# #     pass


# # def cuda_cross(a, b, bsize):
# #     """ Cross-product of two GPUArrays (row by row).

# #     Parameters:
# #         a (gpu): GPUArray 1 of vectors (m x 3).
# #         b (gpu): GPUArray 2 of vectors (m x 3).
# #         bsize (int): < Blocksize divided by 3.

# #     Returns:
# #         gpu: Returns the m vectors from a x b
# #     """
# #     m = a.shape[0]
# #     c = pycuda.gpuarray.empty((m, 3), float64)
# #     grid = (int(ceil(m / bsize)), 1)
# #     cross_product(a, b, c, block=(bsize, 3, 1), grid=grid)
# #     return c


# # def cuda_hermitian(a):
# #     """ Hermitian conjugate transpose of GPUArray.

# #     Parameters:
# #         a (gpu): Complex GPUArray.

# #     Returns:
# #         gpu: The complex conjugate transpose of the GPUArray.

# #     Examples:
# #         >>> a = cuda_hermitian(cuda_give([[1 + 2.j, 3 - 4.j],[0 - 5.j, 6 - 1.j]], type='complex'))
# #         array([[ 1.-2.j,  0.+5.j],
# #                [ 3.+4.j,  6.+1.j]], dtype=complex64)
# #         >>> type(a)
# #         <class 'pycuda.gpuarray.GPUArray'>
# #     """
# #     return skcuda.linalg.hermitian(a)


# # def cuda_inv(a):
# #     """ Inverse of GPUArray matrix.

# #     Notes
# #         - Requires CULA.

# #     Parameters:
# #         a (gpu): Input square GPUArray (m x m).

# #     Returns:
# #         gpu: Matrix inverse as a GPUArray (m x m).

# #     Examples:
# #         >>> a = cuda_inv(cuda_give([[4, 7], [2, 6]]))
# #         array([[ 0.6, -0.7],
# #                [-0.2,  0.4]])
# #         >>> type(a)
# #         <class 'pycuda.gpuarray.GPUArray'>
# #     """
# #     return skcuda.linalg.inv(a)


# # def cuda_normrow(a):
# #     """ GPUArray of vectors norm.2 (row by row).

# #     Parameters:
# #         a (gpu): GPUArray of vectors (m x n).

# #     Returns:
# #         gpu: Vector lengths (m,).

# #     Examples:
# #         >>> a = cuda_normrow(cuda_give([[1, 2], [3, 4]]))
# #         array([ 2.23606798,  5.])
# #         >>> type(a)
# #         <class 'pycuda.gpuarray.GPUArray'>
# #     """
# #     return cuda_sqrt(cuda_sum(a * a, axis=1))


# # def cuda_pinv(a):
# #     """ Moore-Penrose pseudo inverse of the GPUArray.

# #     Notes:
# #         - Singular values smaller than 10^-15 are set to zero.
# #         - Requires CULA.

# #     Parameters:
# #         a (gpu): Input GPUArray (m x n).

# #     Returns:
# #         gpu: Pseudo inverse.

# #     Examples:
# #         >>> a = cuda_pinv(cuda_give([[1, 3, -1], [2, 0, 3]]))
# #         array([[ 0.1056338 ,  0.16197183],
# #                [ 0.27464789,  0.02112676],
# #                [-0.07042254,  0.22535211]])
# #         >>> type(a)
# #         <class 'pycuda.gpuarray.GPUArray'>
# #     """
# #     return skcuda.linalg.pinv(a)


# # def cuda_svd(a, jobu='S', jobvt='S'):
# #     """ GPUArray Singular Value Decomposition.

# #     Notes
# #         - Requires CULA.

# #     Parameters:
# #         a (gpu): GPUArray (m x n) to decompose.

# #     Returns:
# #         gpu: Unitary matrix (m x k).
# #         gpu: Singular values.
# #         gpu: vh matrix (k x n).

# #     """
# #     return skcuda.linalg.svd(a)


# # def cuda_trace(a):
# #     """ GPUArray trace, the sum along the main diagonal.

# #     Parameters:
# #         a (gpu): Input GPUArray.

# #     Returns:
# #         float: tr(GPUArray).

# #     Examples:
# #         >>> a = cuda_trace(cuda_give([[0, 1], [2, 3]]))
# #         3.0
# #         >>> type(a)
# #         <class 'numpy.float64'>
# #     """
# #     return skcuda.linalg.trace(a)


# # def cuda_transpose(a):
# #     """ Transpose a GPUArray.

# #     Parameters:
# #         a (gpu): GPUArray of size (m x n).

# #     Returns:
# #         gpu: GPUArray transpose (n x m).

# #     Examples:
# #         >>> a = cuda_transpose(cuda_give([[0, 1], [2, 3]]))
# #         array([[ 0.,  2.],
# #                [ 1.,  3.]])
# #         >>> type(a)
# #         <class 'pycuda.gpuarray.GPUArray'>
# #     """
# #     return skcuda.linalg.transpose(a)

# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    # a = diag_cuda([1., 2., 3.])
    a = eye_cuda(3)
#     c = det_cuda(give_cuda([[5, -2, 1], [0, 3, -1], [2, 0, 7]]))

    print(a)

    # from compas.hpc import give_cuda

    # a = give_cuda([[0, 1], [2, 3]])
    # b = give_cuda([[0, 1], [1, 0]])
    # c = dot_cuda(a, b)

    # print(c)

    # a = cuda_transpose(cuda_give([[0, 1], [2, 3]]))
    # b = cuda_trace(cuda_give([[0, 1], [2, 3]]))
# #     c = cuda_pinv(cuda_give([[1, 3, -1], [2, 0, 3]]))
# #     d = cuda_normrow(cuda_give([[1, 2], [3, 4]]))
# #     e = cuda_inv(cuda_give([[4, 7], [2, 6]]))
# #     f = cuda_hermitian(cuda_give([[1 + 2.j, 3 - 4.j], [0 - 5.j, 6 - 1.j]], type='complex'))
# #     g = cuda_det(cuda_give([[5, -2, 1], [0, 3, -1], [2, 0, 7]]))
# #     h = cuda_conj(cuda_give([1 + 2.j, 3 - 4.j], type='complex'))
