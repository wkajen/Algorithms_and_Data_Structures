# skonczone zadanie dodatkowe

class Matrices:
    def __init__(self, elem, param=0):
        if isinstance(elem, tuple):
            r = elem[0]
            col = elem[1]
            self.__matrix = []
            for i in range(r):
                row = []
                for j in range(col):
                    row.append(param)
                self.__matrix.append(row)
        else:
            self.__matrix = elem

    def __str__(self):
        result = ''
        for i in range(self.size()[0]):
            result += (str(self[i]) + '\n')
        return result

    def __getitem__(self, item):
        return self.__matrix[item]

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])


def chio(matrix):
    n = matrix.size()[0]
    n_2 = matrix.size()[1]

    if n == n_2 and n > 2:
        first = matrix[0][0]
        det = 1
        newMatrix = []
        while n >= 2:
            newMatrix = Matrices((n - 1, n - 1))

            #jesli 1-szy element jest zerem
            if first == 0:
                i = 1
                while matrix[i][0] == 0 and i < n-1:
                    i += 1
                if i == n-1 and matrix[i][0] == 0:     #kiedy wszystkie wyrazy z pierwszej kolumny są równe 0
                    raise Exception("Nie można policzyć wyznacznika")
                else:
                    for j in range(n):
                        matrix[0][j], matrix[i][j] = matrix[i][j], matrix[0][j]
                    first = matrix[0][0]
                det = -det

            det *= 1 / (first ** (n - 2))

            for w in range(n - 1):
                for k in range(n - 1):
                    newMatrix[w][k] = matrix[0][0] * matrix[w + 1][k + 1] - matrix[w + 1][0] * matrix[0][k + 1]
            n -= 1
            first = newMatrix[0][0]
            matrix = newMatrix

        return det * newMatrix[0][0]

    else:
        raise Exception("Błędna matrix")


def main():
    matrix_1 = Matrices([
        [5, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])

    matrix_2 = Matrices([
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])

    print(chio(matrix_1))
    print(chio(matrix_2))

if __name__ == "__main__":
    main()