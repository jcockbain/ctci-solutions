def print_binary(n):
    print("{0:b}".format(n))


def insert(N, M, i, j):
    j_mask = ~0 << j + 1
    i_mask = 1 << i
    clear_mask = j_mask | i_mask
    N = N & clear_mask
    M <<= i
    return N | M
