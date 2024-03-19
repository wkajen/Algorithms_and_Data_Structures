# skończone zadanie

class Element:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Lista:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, val):
        elem = Element(data=val, next=self.head)
        self.head = elem

    def remove(self):
        if not self.is_empty():
            self.head = self.head.next
        else:
            raise Exception('Lista już jest pusta!')

    def is_empty(self):
        return self.head is None

    def length(self):
        d = 0
        curr = self.head
        while curr is not None:
            d += 1
            curr = curr.next
        return d

    def get(self):
        if self.is_empty():
            raise Exception('Lista jest pusta')
        else:
            return self.head.data

    def __str__(self):
        result = '['
        no = 0
        curr = self.head
        while no < self.length():
            result += str(curr.data)
            if curr.next is not None:
                result += ',\n'
            curr = curr.next
            no += 1
        return result + ']'

    def add_end(self, value):
        if not self.is_empty():
            elem = Element(data=value)
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = elem
        else:
            self.add(value)

    def remove_end(self):
        if not self.is_empty():
            if self.length() == 1:
                self.head = None
            else:
                curr = self.head
                while curr.next.next is not None:
                    curr = curr.next
                curr.next = None
        else:
            raise Exception('Lista jest pusta!')


    def take(self, n):
        if n < 0:
            raise Exception('Nie można wyświetlić ujemnej liczby elementów!')
        newList = Lista()
        if n == 0 or self.length() == 0:
            return newList
        if n > 0:
            newList.add(self.get())
            curr = self.head
            i = 1
            while i < n and i < self.length():
                newList.add_end(curr.next.data)
                curr = curr.next
                i += 1
            return newList

    def drop(self, n):
        if n < 0:
            raise Exception('Nie można pominąć ujemnej liczby elementów')
        else:
            newList = Lista()
            if n >= self.length():
                return newList
            else:
                curr = self.head
                i = 1
                while i < n:
                    curr = curr.next
                    i += 1
                while i < self.length():
                    newList.add_end(curr.next.data)
                    curr = curr.next
                    i += 1

                return newList


def main():
   lista = Lista()
   lista.add(('UJ', 'Kraków', 1364))
   lista.add(('Błędna wartość'))
   print('Lista z błędem na początku:\n', lista)

   lista.remove()
   lista.add(('AGH', 'Kraków', 1919))
   lista.add_end(('PW', 'Warszawa', 1915))
   lista.add_end(('UW', 'Warszawa', 1915))
   lista.add_end('Zła wartość na koniec')
   print('\nLista z błędem na końcu:\n', lista)

   lista.remove_end()
   lista.add_end(('UP', 'Poznań', 1919))
   lista.add_end(('PG', 'Gdańsk', 1945))
   print('\nCała poprawna lista', lista.length(), '-elementowa:\n', lista)

   n = 4
   print('\nNowa lista z', n, 'pierwszych elementów:\n', lista.take(n))
   print('\nNowa lista bez', n, 'pierwszych elementów:\n', lista.drop(n))

   print('\nPierwszy element listy:\n', lista.get())

   lista.destroy()
   print('\nZniszczono całą listę:\n', lista)
   print('\nLista jest teraz pusta?\n', lista.is_empty())

if __name__ == "__main__":
    main()
