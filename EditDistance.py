
def EditDistRecursive(x, y):
    # This implementation is VERY slow
    if len(x) == 0:
        return len(y)
    elif len(y) == 0:
        return len(x)
    else:
        distHoriz = EditDistRecursive(x[:-1], y) + 1
        distVert = EditDistRecursive(x, y[:-1]) + 1
        if x[-1] == y[-1]:
            distDiag = EditDistRecursive(x[:-1], y[:-1])
        else:
            distDiag = EditDistRecursive(x[:-1], y[:-1]) + 1
        return min(distHoriz, distVert, distDiag)

# Dynamic programming ~ create a matrix filled with the edit distances for the substrings already computed to save time
#                 Y
#          A  G  A  T  C  C
#       G [0, 1, 2, 3, 4, 5]
#   X   T [1, 0, 0, 0, 0, 0]
#       A [2, 0, 0, 0, 0, 0]
#       A [3, 0, 0, 0, 0, 0]
#       T [4, 0, 0, 0, 0, 0]

# The Edit distance is the delta between two patterns X and Y that are not necesatily the same length
# including substitutions, insertions and deletions
# Hamming distance assumes patterns of same length and allows only for substitutions
def EditDistance(x, y):
    Matrix = []
    for _ in range(len(x) + 1): # + 1 because the first column and row are for empty string
        row = [0] * (len(y) + 1)
        Matrix.append(row)
    Matrix[0] = [i for i in range(len(y) + 1)]
    for i in range(len(x) + 1):
        Matrix[i][0] = i
    # up until here it's just creating the Matrix
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            distHoriz = Matrix[i][j - 1] + 1
            distVert = Matrix[i - 1][j] + 1
            if x[i - 1] == y[j - 1]:
                distDiag = Matrix[i-1][j-1]
            else:
                distDiag = Matrix[i-1][j-1] + 1
            Matrix[i][j] = min(distHoriz, distVert, distDiag)
    # Edit distance is the value in the bottom right corner of the matrix
    return Matrix[-1][-1]



