class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

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
        if self.Root.NodeKey == key:
            return Node, True, False
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

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root.NodeKey = key
            self.Root.NodeValue = val
            return
        search_result = self.FindNodeByKey(key)
        if search_result[1] is True:
            return False  # если ключ уже есть
        if search_result[1] is False and search_result[2] is True:
            search_result[0].LeftChild = BSTNode(key, val, search_result[0])
        if search_result[1] is False and search_result[2] is False:
            search_result[0].RightChild = BSTNode(key, val, search_result[0])

    def FinMinMax(self, FromNode, FindMax):
        if FromNode.RightChild and FindMax is True:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        if FromNode.LeftChild and FindMax is False:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        return FromNode

    def __Left_DeleteNodeByKey(self, Node_Left, count):
        if Node_Left.LeftChild is None:
            if count > 0:
                Node_Left.Parent.LeftChild = None
            return Node_Left
        count += 1
        return self.__Left_DeleteNodeByKey(Node_Left.LeftChild, count)

    def DeleteNodeByKey(self, key):
        search_result = self.FindNodeByKey(key)  # ищем в дереве узел
        node = search_result[0]
        if search_result[1] is False:
            return False  # если узел не найден

        # исключение при удалении корня, если в дереве только корень
        if (
            node.NodeKey == self.Root.NodeKey
            and self.Root.LeftChild is None
            and self.Root.RightChild is None
        ):
            self.Root = None
            return True

        # условие при которм у узла ноль потомков
        if node.LeftChild is None and node.RightChild is None and node.NodeKey is key:

            parent_result = self.FindNodeByKey(
                node.Parent.NodeKey
            )  # ищем родительский узел в дереве
            if (
                parent_result[0].RightChild is not None
                and parent_result[0].RightChild.NodeKey is node.NodeKey
            ):
                parent_result[0].RightChild = None
                return True
            if (
                parent_result[0].LeftChild is not None
                and parent_result[0].LeftChild.NodeKey is node.NodeKey
            ):
                parent_result[0].LeftChild = None
                return True

        # условие при которм у узла один потомок
        if (
            node.LeftChild is None
            and node.RightChild is not None
            and node.NodeKey is key
        ):
            parent_result = self.FindNodeByKey(
                node.Parent.NodeKey
            )  # ищем родительский узел в дереве
            if parent_result[0].RightChild.NodeKey is key:
                node.RightChild.Parent = node.Parent
                parent_result[0].RightChild = node.RightChild
                return True
            if parent_result[0].LeftChild.NodeKey is key:
                node.RightChild.Parent = node.Parent
                parent_result[0].LeftChild = node.RightChild
                return True

        if (
            node.LeftChild is not None
            and node.RightChild is None
            and node.NodeKey is key
        ):
            parent_result = self.FindNodeByKey(
                node.Parent.NodeKey
            )  # ищем родительский узел в дереве
            if parent_result[0].RightChild.NodeKey is key:
                node.LeftChild.Parent = node.Parent
                parent_result[0].RightChild = node.LeftChild
                return True
            if parent_result[0].LeftChild.NodeKey is key:
                node.LeftChild.Parent = node.Parent
                parent_result[0].LeftChild = node.LeftChild
                return True

        # условие при которм у узла два потомка
        if (
            node.LeftChild is not None
            and node.RightChild is not None
            and node.NodeKey is key
        ):

            # 1. Найти узел на замену удаляемому
            count = 0
            res = self.__Left_DeleteNodeByKey(node.RightChild, count)

            # 2. Присвоить потомкам найденного узла потомки удаляемого
            if node.RightChild.NodeKey != res.NodeKey:
                res.RightChild = node.RightChild
            if node.LeftChild.NodeKey != res.NodeKey:
                res.LeftChild = node.LeftChild

            # 3. Присвоить графе "Parent" найденного узла "Parent" удаляемого узла
            res.Parent = node.Parent

            # 4. Присвоить графе "Parent" потомков значение найденного узла
            if (
                node.RightChild.NodeKey != res.NodeKey
                and node.NodeKey == self.Root.NodeKey
            ):
                res.RightChild.Parent = res

            if (
                node.LeftChild.NodeKey != res.NodeKey
                and node.NodeKey == self.Root.NodeKey
            ):
                res.LeftChild.Parent = res

            if (
                node.RightChild.NodeKey != res.NodeKey
                and node.NodeKey != self.Root.NodeKey
            ):
                res.RightChild.Parent = res

            if (
                node.LeftChild.NodeKey != res.NodeKey
                and node.NodeKey != self.Root.NodeKey
            ):
                res.LeftChild.Parent = res

            # 5. Добавить нового потомка родителю удаляемого узла

            if (
                node.NodeKey != self.Root.NodeKey
                and node.Parent.LeftChild is not None
                and node.Parent.LeftChild.NodeKey == node.NodeKey
            ):
                node.Parent.LeftChild = res

            if (
                node.NodeKey != self.Root.NodeKey
                and node.Parent.RightChild is not None
                and node.Parent.RightChild.NodeKey == node.NodeKey
            ):
                node.Parent.RightChild = res

            if self.Root.NodeKey == node.NodeKey:
                self.Root = res

    def __Count(self, node_1, list_node_1):
        if node_1 is not None:
            self.__Count(node_1.RightChild, list_node_1)
            list_node_1.append(node_1)
            self.__Count(node_1.LeftChild, list_node_1)
            return len(list_node_1)

    def Count(self):  # количество узлов в дереве
        if self.Root is None:
            return None
        node = self.Root
        list_node = []
        return self.__Count(node, list_node)
