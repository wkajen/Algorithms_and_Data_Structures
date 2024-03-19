# skonczone zadanie
import polska


class Node:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, first_node=None, second_node=None, edge=None):
        self.first_node = first_node
        self.second_node = second_node
        self.edge = edge


class List:
    def __init__(self):
        self.tab = []
        self.lista = []
        self.dict = {}

    def insertVertex(self, vertex):
        self.tab.append([])
        self.lista.append(vertex)
        self.dict[vertex] = len(self.lista) - 1

    def insertEdge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.lista and vertex2 in self.lista:
            ind_1 = self.getVertexIdx(vertex1)
            ind_2 = self.getVertexIdx(vertex2)
            if ind_2 not in self.tab[ind_1]:
                self.tab[ind_1].append(ind_2)
            if ind_1 not in self.tab[ind_2]:
                self.tab[ind_2].append(ind_1)
        else:
            print("Nie można wstawić krawędzi")

    def deleteVertex(self, vertex):
        if vertex in self.lista:
            ind = self.getVertexIdx(vertex)
            neighbours = self.neighbours(ind)

            # usunięcie indeksu z listy sąsiadów
            for i in range(len(neighbours)):
                act = neighbours[i]
                for j in range(len(self.tab[act])):
                    if self.tab[act][j] == ind:
                        del self.tab[act][j]
                        break

            del self.tab[ind]

            # zdekrementowanie wyższych indeksów
            for i in range(len(self.tab)):
                for j in range(len(self.tab[i])):
                    if self.tab[i][j] > ind:
                        self.tab[i][j] -= 1

            # uaktualnienie słownika
            del self.dict[vertex]
            act = 0
            for node, ind in self.dict.items():
                self.dict[node] = act
                act += 1

            del self.lista[ind]
        else:
            print('Nie ma takiego węzła')

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.lista and vertex2 in self.lista:
            ind_1 = self.getVertexIdx(vertex1)
            ind_2 = self.getVertexIdx(vertex2)

            for i in range(len(self.tab[ind_1])):
                if self.tab[ind_1][i] == ind_2:
                    del self.tab[ind_1][i]
                    break

            for i in range(len(self.tab[ind_2])):
                if self.tab[ind_2][i] == ind_1:
                    del self.tab[ind_2][i]
                    break
        else:
            print('Nie ma takiej krawędzi')

    def getVertexIdx(self, vertex):
        if vertex in self.lista:
            return self.dict[vertex]
        else:
            print('Nie ma takiego węzła')

    def getVertex(self, vertex_idx):
        if vertex_idx < self.order():
            for node, ind in self.dict.items():
                if ind == vertex_idx:
                    return node
        else:
            print('Nie ma takiego indeksu')

    def neighbours(self, vertex_idx):
        if vertex_idx < len(self.tab):
            return self.tab[vertex_idx]
        else:
            print('Nie ma takiego indeksu')

    def order(self):
        return len(self.lista)

    def size(self):
        size = 0
        for elem in self.tab:
            size += len(elem)
        return int(size / 2)

    def edges(self):
        ret = []
        for i in range(self.order()):
            for j in range(len(self.tab[i])):
                first_node = self.getVertex(i)
                end_node = self.getVertex(self.tab[i][j])
                ret.append((first_node.key, end_node.key))
        return ret


class Matrix:
    def __init__(self):
        self.tab = []
        self.lista = []
        self.dict = {}

    def insertVertex(self, vertex):
        self.tab.append([])
        length = self.order()
        for i in range(length):
            self.tab[i].append(0)
        for j in range(length - 1):
            self.tab[length - 1].append(0)

        self.lista.append(vertex)
        self.dict[vertex] = length - 1

    def insertEdge(self, vertex1, vertex2, edge=None):
        if vertex1 in self.lista and vertex2 in self.lista:
            ind_1 = self.getVertexIdx(vertex1)
            ind_2 = self.getVertexIdx(vertex2)
            self.tab[ind_1][ind_2] = 1
            self.tab[ind_2][ind_1] = 1
        else:
            print("Nie można wstawić krawędzi")

    def deleteVertex(self, vertex):
        if vertex in self.lista:
            ind = self.getVertexIdx(vertex)
            del self.tab[ind]
            for i in range(self.order()):
                del self.tab[i][ind]

            del self.dict[vertex]
            act = 0
            for node, ind in self.dict.items():
                self.dict[node] = act
                act += 1

            del self.lista[ind]

        else:
            print('Nie ma takiego węzła')

    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.lista and vertex2 in self.lista:
            ind_1 = self.getVertexIdx(vertex1)
            ind_2 = self.getVertexIdx(vertex2)
            self.tab[ind_1][ind_2] = 0
            self.tab[ind_2][ind_1] = 0
        else:
            print('Nie ma takiej krawędzi')

    def getVertexIdx(self, vertex):
        if vertex in self.lista:
            return self.dict[vertex]
        else:
            print('Nie ma takiego węzła')

    def getVertex(self, vertex_idx):
        if vertex_idx < self.order():
            for node, ind in self.dict.items():
                if ind == vertex_idx:
                    return node
        else:
            print('Nie ma takiego indeksu')

    def neighbours(self, vertex_idx):
        if vertex_idx < self.order():
            neig = []
            for i in range(self.order()):
                if self.tab[vertex_idx][i] == 1:
                    neig.append(i)
            return neig
        else:
            print('Nie ma takiego węzła')

    def order(self):
        return len(self.tab)

    def size(self):
        edges = 0
        for i in range(self.order()):
            for j in range(self.order()):
                if self.tab[i][j] == 1:
                    edges += 1
        return int(edges / 2)

    def edges(self):
        ret = []
        for i in range(self.order()):
            for j in range(len(self.tab[i])):
                if self.tab[i][j] == 1:
                    first_node = self.getVertex(i)
                    end_node = self.getVertex(j)
                    ret.append((first_node.key, end_node.key))
        return ret


def test(graph):
    nodes = []
    for elem in polska.graf:
        if elem[0] not in nodes:
            nodes.append(elem[0])

    for elem in nodes:
        graph.insertVertex(Node(key=elem))

    for elem in polska.graf:
        graph.insertEdge(Node(key=elem[0]), Node(key=elem[1]))

    malop = Node(key='K')
    lodz = Node(key='E')
    mazow = Node(key='W')

    # usunięcie małopolski
    #graph.deleteVertex(malop)

    # usunięcie połączenia między mazowieckim i łódzkimi
    graph.deleteEdge(mazow, lodz)
    graph.deleteEdge(lodz, mazow)

    polska.draw_map(graph.edges())


def main():
    test(List())    # lista sąsiedztwa
    test(Matrix())     # macierz sąsiedztwa

if __name__ == "__main__":
    main()