# skonczone zadanie

class Element:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data

class TabMix:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(self.size)]

    def func_mix(self, key):
        if isinstance(key, int):
            return key % self.size
        if isinstance(key, str):
            sumLet = 0
            for letter in key:
                sumLet += ord(letter)
            return sumLet % self.size

    def colision_old(self, key_search, i=0):
        index = (self.func_mix(key_search) + self.c1 * i + self.c2 * (i ** 2)) % self.size
        full = 0
        if i == self.size:
            full = 1
        return [index, full]

    def colision(self, key_search, i=0):
        index = (self.func_mix(key_search) + self.c1 * i + self.c2 * (i ** 2)) % self.size
        return index, i == 2*self.size

    def search(self, key_search, i=0):
        index, full = self.colision(key_search, i)
        if full is True:
            return None
        else:
            if self.tab[index] is not None:
                if self.tab[index].key == key_search:
                    return self.tab[index].data
                else:
                    return self.search(key_search, i+1)
            else:
                return self.search(key_search, i + 1)


    def insert_old(self, new_key, new_data):
        i = 0
        while i < self.size + 1:
            new_index, full = self.colision(new_key, i)
            if full == 1:
                print('Brak miejsca')
                break
            else:
                # empty place
                if self.tab[new_index] is None:
                    self.tab[new_index] = Element(key=new_key, data=new_data)
                    break
                else:
                    # klucz się pokrywa -> nadpisanie wartości
                    if self.tab[new_index].key == new_key:
                        self.tab[new_index].data = new_data
                        break
                    # znowu kolizja
                    else:
                        i += 1

    def insert(self, new_key, new_data, i=0):
        new_index, full = self.colision(new_key, i)
        if full is True:
            print('Brak miejsca')
        else:
            # empty place
            if self.tab[new_index] is None:
                self.tab[new_index] = Element(key=new_key, data=new_data)
            else:
                # klucz się pokrywa -> nadpisanie wartości
                if self.tab[new_index].key == new_key:
                    self.tab[new_index].data = new_data
                # znowu kolizja
                else:
                    self.insert(new_key, new_data, i+1)


    def remove_old(self, key_remove):
        i = 0
        while i < self.size+1:
            index, full = self.colision(key_remove, i)
            if self.tab[index] is None or full == 1:
                print('Brak danej')
                break
            else:
                if self.tab[index].key == key_remove:
                    self.tab[index] = None
                    break
                else:
                    i += 1

    def remove(self, key_remove, i=0):
        index, full = self.colision(key_remove, i)
        if full is True:
            print('Brak danej')
        else:
            if self.tab[index].key == key_remove:
                self.tab[index] = None
            else:
                self.remove(key_remove, i+1)


    def __str__(self):
        result = '{'
        ind = 0
        while ind < self.size:
            if self.tab[ind] is None:
                result += str(None)
            else:
                result += str(self.tab[ind].key) + ':' + str(self.tab[ind].data)
            ind += 1
            if ind != self.size:
                result += ', '
        return result + '}'


def main():
    def test1(size, c1=1, c2=0):
        tab = TabMix(size, c1, c2)
        alphabet = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        for i in range(1, 16):
            if i == 6:
                tab.insert(18, alphabet[i - 1])
                i += 1
            if i == 7:
                tab.insert(31, alphabet[i - 1])
                i += 1
            tab.insert(i, alphabet[i-1])
        print(tab)
        print(tab.search(5))
        print(tab.search(14))
        tab.insert(5, 'Z')
        print(tab.search(5))
        tab.remove(5)
        print(tab)
        print(tab.search(31))

        tab.insert('test', 'W')
        print(tab)

    def test2(size, c1, c2):
        tab = TabMix(size, c1, c2)
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        for i in range(1, 16):
            tab.insert(13*i, alphabet[i - 1])
        print(tab)

    test1(13)
    print('\n')
    test2(13, 1, 0)
    print('\n')
    test2(13, 0, 1)
    print('\n')
    test1(13, 0, 1)

if __name__ == "__main__":
    main()

