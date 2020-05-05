import numpy

numpy.random.seed(4)


def matrix_factorization(A, K, beta=0.06, lan_da=0.03, loop=5000):
    # 2
    u = numpy.sum(A) / (user * item - numpy.count_nonzero(A == 0))
    # 4
    bs = numpy.arange(user, dtype='float')
    sum_rate_s = numpy.sum(A, axis=1)
    for s in range(user):
        ds = numpy.count_nonzero(A[s, :] > 0)
        bs[s] = (sum_rate_s[s] - ds * u) / ds

    # 8
    bi = numpy.arange(item, dtype='float')
    sum_rate_i = numpy.sum(A, axis=0)
    for s in range(item):
        di = numpy.count_nonzero(A[:, s] > 0)
        bi[s] = (sum_rate_i[s] - di * u) / di

    # 9 10
    W = numpy.random.rand(user, K)
    H = numpy.random.rand(K, item)

    cur = 0
    while cur < loop:
        for s in range(user):
            for i in range(item):
                if A[s][i] > 0:
                    # 13
                    psi = u + bs[s] + bi[i] + numpy.dot(W[s, :], H[:, i])
                    # print('psi', psi)
                    # 14
                    esi = A[s][i] - psi
                    # 15
                    u += (beta * esi)
                    # print('u ', u)
                    # 16
                    bs[s] += beta * (esi - lan_da * bs[s])
                    bi[i] += beta * (esi - lan_da * bi[i])
                    # 18
                    for k in range(K):
                        W[s][k] += beta * \
                            (2 * esi * H[k][i] - lan_da * W[s][k])
                        H[k][i] += beta * \
                            (2 * esi * W[s][k] - lan_da * H[k][i])
        cur += 1
    return W, H, bs, bi, u


A = numpy.array([
    [1, 4, 5, 0, 3],
    [5, 1, 0, 5, 2],
    [4, 1, 2, 5, 0],
    [0, 3, 4, 0, 4]
])

user = A.shape[0]
item = A.shape[1]

W1, H1, bs1, bi1, u1 = matrix_factorization(A, 2)

Y = numpy.dot(W1, H1)
C = numpy.array([[round(Y[i][j]) for j in range(item)] for i in range(user)])


print('Ma tran ban dau:\n ', A)
print('ma tran A3:\n', C)