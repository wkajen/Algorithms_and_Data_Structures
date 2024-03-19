# skończone zadanie

def realloc(tab, size):
    old_size = len(tab)
    return [tab[i] if i < old_size else None for i in range(size)]

class Queue:
    def __init__(self):
        self.size = 5
        self.tab = [None for i in range(self.size)]
        self.ind_write = 0
        self.ind_read = 0

    def is_empty(self):
        return self.ind_read == self.ind_write

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.ind_read]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            ind_act = self.ind_read
            if self.ind_read + 1 == self.size:
                self.ind_read = 0
            else:
                self.ind_read += 1
            return self.tab[ind_act]

    def enqueue(self, data):
        self.tab[self.ind_write] = data

        if self.ind_write + 1 == self.size:
            self.ind_write = 0
        else:
            self.ind_write += 1

        if self.ind_write == self.ind_read:
            self.tab = realloc(self.tab, 2 * self.size)

            i = self.ind_write
            while i < self.size:
                self.tab[self.size + i] = self.tab[i]
                self.tab[i] = None
                i += 1

            self.ind_read += self.size
            self.size = 2 * self.size

    def print_queue(self):
        result = '['
        act = self.ind_read
        while act != self.ind_write:
            if act == self.size:
                act = -1
            if self.tab[act] is not None:
                result += str(self.tab[act]) + ' '
            act += 1
        if not self.is_empty():
            result = result[:-1]
        return result + ']'

    def print_tab(self):
        result = '['
        for i in range(self.size):
            result += str(self.tab[i])
            if i + 1 != self.size:
                result += ' '
        return result + ']'


def main():
    queue = Queue()
    for i in range(1, 5):
       queue.enqueue(i)
    print('Pierwsza dana (dequeue):', queue.dequeue())
    print('Druga dana (peek):', queue.peek())
    print('Aktualna kolejka:', queue.print_queue())
    for i in range(5, 9):
       queue.enqueue(i)
    print('Aktualna tablica:', queue.print_tab())
    while queue.is_empty() is not True:
       print('Usuwana dana:', queue.dequeue())
    print('Pusta kolejka:', queue.print_queue())


if __name__ == "__main__":
    main()

