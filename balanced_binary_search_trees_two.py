class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def __FindNodeByKey(self, key, Node):
        if key == Node.NodeKey:
            return Node, True, False
        if key < Node.NodeKey and Node.LeftChild is None:
            return Node, False, True
        if key > Node.NodeKey and Node.RightChild is None:
            return Node, False, False
        if key < Node.NodeKey:
            if Node.LeftChild:
                return self.__FindNodeByKey(key, Node.LeftChild)
        if key > Node.NodeKey:
            if Node.RightChild:
                return self.__FindNodeByKey(key, Node.RightChild)
        return None

    def FindNodeByKey(self, key):
        intermediate_result = BSTFind()
        Node = self.Root
        (
            intermediate_result.Node,
            intermediate_result.NodeHasKey,
            intermediate_result.ToLeft,
        ) = self.__FindNodeByKey(key, Node)
        search_res = []
        search_res.append(intermediate_result.Node)
        search_res.append(intermediate_result.NodeHasKey)
        search_res.append(intermediate_result.ToLeft)
        if search_res != []:
            return search_res
        else:
            return None

    def recursion(self, parent, range_array, Level_tree):
        if len(range_array) <= 0:
            return
        # создание в дереве нового узла Node с текущим "корневым" (центральным) значением
        Node = BSTNode(range_array[len(range_array) // 2], parent)
        if Level_tree == 0:
            self.Root = Node
            self.Root.Parent = None
        Node.Level = Level_tree
        Level_tree += 1
        # вызов рекурсивно recursion() с диапазоном массива слева от корня и параметром-узлом parent
        Node.LeftChild = self.recursion(
            Node, range_array[: len(range_array) // 2], Level_tree
        )
        # вызов рекурсивно recursion() с диапазоном массива справа от корня и параметром-узлом parent
        Node.RightChild = self.recursion(
            Node, range_array[len(range_array) // 2 + 1 :], Level_tree
        )
        return Node

    def GenerateTree(self, a):
        a.sort()
        # создание в дереве нового узла Node с текущим "корневым" (центральным) значением
        Node = BSTNode(a[len(a) // 2], None)
        self.Root = Node
        self.Level = 0
        self.recursion(Node, a, self.Level)
        return Node

    # метод по определению высоты дерева
    def height(self, node) -> int:
        if node is None:
            return 0
        left_height = self.height(node.LeftChild)
        right_height = self.height(node.RightChild)
        if left_height >= right_height:
            return left_height + 1
        if left_height < right_height:
            return right_height + 1

    def __IsBalanced(self, root_node):
        if root_node is None:
            return True
        Left = self.height(root_node.LeftChild)
        Right = self.height(root_node.RightChild)
        if (
            ((abs(Left - Right) == 1) or (abs(Left - Right) == 0))
            and self.__IsBalanced(root_node.LeftChild) is True
            and self.__IsBalanced(root_node.RightChild) is True
        ):
            return True
        return False

    def IsBalanced(self, root_node):
        Find_node = self.FindNodeByKey(
            root_node.NodeKey
        )  # поиск узла в текущем дереве по ключу
        root_node = Find_node[0]
        return self.__IsBalanced(self.Root)
