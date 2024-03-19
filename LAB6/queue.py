# skonczone zadanie

class Element:
    def __init__(self, priorytet=None, data=None):
        self.priorytet = priorytet
        self.data = data

    def __lt__(self, other):
        if self.priorytet < other.priorytet:
            return self.data
        else:
            return other.data

    def __gt__(self, other):
        if self.priorytet > other.priorytet:
            return self.data
        else:
            return other.data

    def __str__(self):
        return str(self.priorytet) + ' : ' + str(self.data)


class Queue:
    def __init__(self):
        self.tab = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0].data

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            ret = self.tab[0].data

            if self.size == 1:
                del self.tab[0]
                self.size -= 1
                return ret

            else:
                self.tab[0], self.tab[-1] = self.tab[-1], self.tab[0]
                #self.tab.pop(-1)
                del self.tab[-1]
                self.size -= 1
                act = 0

                if self.left(act) < self.size:
                    if self.right(act) >= self.size:
                        if self.tab[self.left(act)].priorytet > self.tab[act].priorytet:
                            self.tab[self.left(act)], self.tab[act] = self.tab[act], self.tab[self.left(act)]
                    else:

                        if self.tab[self.left(act)].priorytet > self.tab[self.right(act)].priorytet:
                            greater_ind = self.left(act)
                        else:
                            greater_ind = self.right(act)

                        while self.tab[act].priorytet < self.tab[greater_ind].priorytet:
                            self.tab[greater_ind], self.tab[act] = self.tab[act], self.tab[greater_ind]

                            act = self.left(act)
                            if self.left(act) > self.size-1:
                                break

                            if self.right(act) < self.size-1:
                                if self.tab[self.left(act)].priorytet > self.tab[self.right(act)].priorytet:
                                    greater_ind = self.left(act)
                                else:
                                    greater_ind = self.right(act)
                            else:
                                if self.left(act) > self.size - 1:
                                    break
                                else:
                                    greater_ind = self.left(act)
                return ret


    def enqueue(self, nowy_priorytet, nowe_data):
        self.tab.append(Element(priorytet=nowy_priorytet, data=nowe_data))
        self.size += 1

        if not self.is_empty():
            act_ind = self.size - 1
            parent_ind = self.parent(act_ind)
            while self.tab[act_ind].priorytet > self.tab[parent_ind].priorytet:
                self.tab[parent_ind], self.tab[act_ind] = self.tab[act_ind], self.tab[parent_ind]
                act_ind = self.parent(act_ind)
                parent_ind = self.parent(act_ind)
                if parent_ind < 0:
                    #parent_ind = 0
                    break


    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2


    def print_tab(self):
        print('{', end=' ')
        for i in range(self.size - 1):
            print(self.tab[i], end=', ')
        if self.size > 0:
        #if self.tab[self.size - 1]:
            print(self.tab[self.size - 1], end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def main():
    queue = Queue()
    lista = [4, 7, 6, 7, 5, 2, 2, 1]
    napis = "ALGORYTM"
    for i in range(len(lista)):
        queue.enqueue(lista[i], napis[i])

    queue.print_tree(0, 0)
    queue.print_tab()
    print(queue.dequeue())
    print(queue.peek())
    queue.print_tab()

    queue.print_tree(0, 0)

    while not queue.is_empty():
        print(queue.dequeue())

    queue.print_tab()


if __name__ == "__main__":
    main()
