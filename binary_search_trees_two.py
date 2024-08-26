class aBST:
    def summ(self, depth_in):  # вычисление количества элементов дерева
        summ_el = 0
        for i in range(depth_in):
            summ_el += 2 ** (depth_in - 1 - i)
        return summ_el

    def __init__(self, depth):
        tree_size = self.summ(depth)
        self.Tree = [None] * tree_size  # массив ключей

    def __FindNodeByKey(self, node, level, key, count):

        if count > level:
            return None

        # возвращаем индекс, если значение уже есть в массиве
        if key is node:
            return self.Tree.index(node)

        # если найден подходящий слот
        if node is None and 2 * count + 1 > level and 2 * count + 2 > level:
            return -count
        if node is None and 2 * count + 1 is not None and 2 * count + 2 is not None:
            return -count

        if (
            node is None
            and self.Tree[2 * count + 1] is None
            and self.Tree[2 * count + 2] is None
        ):
            return -count
        if (
            node is None
            and self.Tree[2 * count + 1] is None
            and self.Tree[2 * count + 2] > node
        ):
            return -count
        if (
            node is None
            and self.Tree[2 * count + 1] < node
            and self.Tree[2 * count + 2] is None
        ):
            return -count
        if (
            node is None
            and self.Tree[2 * count + 1] < node
            and self.Tree[2 * count + 2] > node
        ):
            return -count

        # переход к следующему узлу
        if key < node:
            return self.__FindNodeByKey(
                self.Tree[2 * count + 1], level, key, 2 * count + 1
            )
        if key > node:
            return self.__FindNodeByKey(
                self.Tree[2 * count + 2], level, key, 2 * count + 2
            )

    def FindKeyIndex(self, key):
        if self.Tree is None:
            return 0
        node = self.Tree[0]
        level: int = len(self.Tree)
        count: int = 0  # переменная для индекса
        return self.__FindNodeByKey(node, level, key, count)

    def AddKey(self, key):
        if self.Tree[0] is None:
            self.Tree[0] = key
        ind = self.FindKeyIndex(key)
        if ind == 0 and all(element is None for element in self.Tree):
            self.Tree[0] = key
        elif ind is not None:
            self.Tree[abs(ind)] = key
        if ind is None:
            return -1
