alphabet = ['A', 'C', 'G', 'T']

#     A  C  G  T
#  A [0, 4, 2, 4, 8]
#  C [4, 0, 4, 2, 8]
#  G [2, 4, 0, 4, 8]
#  T [4, 2, 4, 0, 8]
#    [8, 8, 8, 8, 8]

penalties = [
    [0, 4, 2, 4, 8],
    [4, 0, 4, 2, 8],
    [2, 4, 0, 4, 8],
    [4, 2, 4, 0, 8],
    [8, 8, 8, 8, 8]
]


def GlobalAlignment(x, y):
    Matrix = []
    for _ in range(len(x) + 1):
        row = [0] * (len(y) + 1)
        Matrix.append(row)

    for i in range(1, len(x) + 1):
        Matrix[i][0] = Matrix[i - 1][0] +  penalties[alphabet.index(x[i - 1])][-1]

    for i in range(1, len(y) + 1):
        Matrix[0][i] = Matrix[0][i - 1] + penalties[-1][alphabet.index(y[i - 1])]

    # up until here it's just creating the Matrix
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            distHoriz = Matrix[i][j - 1] + penalties[-1][alphabet.index(y[j - 1])]
            distVert = Matrix[i - 1][j] + penalties[alphabet.index(x[i - 1])][-1]
            if x[i - 1] == y[j - 1]:
                distDiag = Matrix[i - 1][j - 1]
            else:
                distDiag = Matrix[i - 1][j - 1] + penalties[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])]
            Matrix[i][j] = min(distHoriz, distVert, distDiag)
    return Matrix[-1][-1]
