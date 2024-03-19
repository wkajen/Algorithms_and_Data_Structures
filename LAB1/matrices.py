# skończone zadanie

class Matrices:
    def __init__(self, elem, param = 0):
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


    def __add__(self, other):
        r1 = self.size()[0]
        col1 = self.size()[1]
        r2 = other.size()[0]
        col2 = other.size()[1]
        sumMat = []
        if r1 == r2 and col1 == col2:
            for i in range(r1):
                row = []
                for j in range(col1):
                    row.append(self[i][j] + other[i][j])
                sumMat.append(row)
            return Matrices(sumMat)
        else:
            raise Exception("Nieodpowiednie wymiary macierzy")


    def __mul__(self, other):
        r1 = self.size()[0]
        col1 = self.size()[1]
        r2 = other.size()[0]
        col2 = other.size()[1]
        mulMat = []
        if r1 == col2 and col1 == r2:
            for i in range(r1):
                row = []
                for j in range(col2):
                    multiplier = 0
                    for k in range(r2):
                        multiplier += self[i][k] * other[k][j]
                    row.append(multiplier)
                mulMat.append(row)
            return Matrices(mulMat)
        else:
            raise Exception("Nieodpowiednie wymiary macierzy")

    def __getitem__(self, item):
        return self.__matrix[item]

    def __str__(self):
        result = ''
        for i in range(self.size()[0]):
            result += (str(self[i]) + '\n')
        return result

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])


def transpose(matrix):
    newMatrix = []
    for k in range(matrix.size()[1]):
        kolumny = []
        for w in range(matrix.size()[0]):
            kolumny.append(matrix[w][k])
        newMatrix.append(kolumny)
    return Matrices(newMatrix)

def main():
    matrix_1 = Matrices([[1,0,2], [-1,3,1]])
    matrix_2 = Matrices((2,3), 1)
    matrix_3 = Matrices([[3,1], [2,1], [1,0]])

    print(transpose(matrix_1))
    print(matrix_1 + matrix_2)
    #print(matrix_1 * matrix_3)

if __name__ == "__main__":
    main()