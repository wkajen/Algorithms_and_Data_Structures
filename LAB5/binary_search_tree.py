# skonczone zadanie

class Element:
    def __init__(self, key=None, data=None, left_node=None, right_node=None):
        self.key = key
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

class Tree:
    def __init__(self):
        self.head = None

    def search(self, key_search):
        if self.head is None:
            print('Drzewo jest puste')
            return None
        else:
            return self._search(self.head, key_search)

    def _search(self, node, key_search):
        if node is None:
            print('Nie znaleziono takiego klucza:', key_search)
            return None
        else:
            if node.key == key_search:
                return node.data
            elif key_search < node.key:
                return self._search(node.left_node, key_search)
            else:
                return self._search(node.right_node, key_search)


    def insert(self, new_key, new_data):
        if self.head is None:
            self.head = Element(key=new_key, data=new_data)
        else:
            self._insert(self.head, new_key, new_data)

    def _insert(self, node, new_key, new_data):
        if new_key < node.key:
            if node.left_node is None:
                node.left_node = Element(key=new_key, data=new_data)
            else:
                self._insert(node.left_node, new_key, new_data)
        elif new_key > node.key:
            if node.right_node is None:
                node.right_node = Element(key=new_key, data=new_data)
            else:
                self._insert(node.right_node, new_key, new_data)
        else:
            node.data = new_data


    def find_succesor(self, node, parent=None):  # podaje już prawego noda
        if node.left_node is None:
            return node, parent
        else:
            return self.find_succesor(node.left_node, node)


    def delete(self, key_del):
        if self.head is not None:
            self._delete(self.head, key_del)
        else:
            print('Nie można usunąć podanego klucza - drzewo jest puste')

    def _delete(self, node, key_del, parent=None, left_child=None):
        if node is not None:
            if node.key == key_del:
                if node.left_node is None and node.right_node is not None:
                    if parent is None:
                        self.head = node.right_node
                    else:
                        if left_child:
                            parent.left_node = node.right_node
                        else:
                            parent.right_node = node.right_node

                elif node.left_node is not None and node.right_node is None:
                    if parent is None:
                        self.head = node.left_node
                    else:
                        if left_child:
                            parent.left_node = node.left_node
                        else:
                            parent.right_node = node.left_node

                elif node.left_node is None and node.right_node is None:
                    if parent is None:
                        self.head = None
                    else:
                        if left_child:
                            parent.left_node = None
                        else:
                            parent.right_node = None
                else:
                    left_side = node.left_node
                    right_side = node.right_node
                    succesor, succ_parent = self.find_succesor(node.right_node)

                    if parent is None:
                        self.head.key = succesor.key
                        self.head.data = succesor.data
                        succ_parent.left_node = None

                    else:
                        if left_child:
                            parent.left_node = succesor
                            parent.left_node.left_node = left_side
                        else:
                            parent.right_node = succesor
                            parent.right_node.left_node = left_side

            elif key_del < node.key:
                self._delete(node.left_node, key_del, node, True)
            elif key_del > node.key:
                self._delete(node.right_node, key_del, node, False)
        else:
            print('Nie ma takiego klucza:', key_del)


    def height(self):
        result = self._height(self.head)
        if result == -1:
            return 0
        else:
            return result

    def _height_old(self, node):
        if node is None:
            return -1
        else:
            left_len = self._height(node.left_node)
            right_len = self._height(node.right_node)

            if left_len > right_len:
                return left_len + 1
            else:
                return right_len + 1

    def _height(self, node):
        if node is None:
            return -1
        else:
            return max(self._height(node.left_node), self._height(node.right_node)) + 1


    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right_node, lvl + 5)

            print()
            print(lvl * " ", node.key, node.data)

            self._print_tree(node.left_node, lvl + 5)


    def print_tree_list(self):
        result = '['
        if self.head is not None:
            result += self._print_tree_list(self.head)
            result = result[:-2]
        result += ']'
        print(result)

    def _print_tree_list(self, node):
        result = ''
        if node.left_node is not None:
            result += self._print_tree_list(node.left_node)
        result += str(node.key) + ':' + str(node.data) + ', '
        if node.right_node is not None:
            result += self._print_tree_list(node.right_node)
        return result


def main():
    dict = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    tree = Tree()
    for elem in dict.items():
        tree.insert(elem[0], elem[1])
    tree.print_tree()
    tree.print_tree_list()
    print(tree.search(24))
    tree.insert(20, 'AA')
    tree.insert(6, 'M')
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print_tree_list()
    tree.print_tree()

if __name__ == "__main__":
    main()

