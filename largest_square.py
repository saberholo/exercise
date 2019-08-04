import numpy as np


l, w = np.random.randint(1, 100, (2,))
print("Length:{}\nWidth:{}".format(l, w))
mat = np.random.randint(0, 2, (l, w))
for row in mat:
    print(row)


def find_largest_square(mat):

    res = 0
    l, w = mat.shape

    if mat.sum() > 0:
        res += 1
    else:
        return 0


    for i in range(l-1):
        for j in range(w-1):
            if mat[i][j] == 1 and mat[i+1][j] == 1 and mat[i][j+1] == 1:
                limit = min(l - i, w - j)
                for k in reversed(range(limit)):
                    if mat[i+k][j+k] == 1 and mat[i, j:j+k].sum() == k and mat[i:i+k, j].sum() == k and mat[i+k, j:j+k].sum() == k and mat[i:i+k, j+k].sum() == k:
                        res = max(res, k+1)
                        break

    return res

largest_square = find_largest_square(mat)
print("Length of the largest square:\t{}".format(largest_square))
