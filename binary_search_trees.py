class BSTNode:

    def __init__(self, key: int, val: int, parent):
        self.NodeKey: int = key  # ключ узла
        self.NodeValue: int = val  # значение в узле
        self.Parent: BSTNode = parent  # родитель или None для корня
        self.LeftChild: BSTNode = None  # левый потомок
        self.RightChild: BSTNode = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node: BSTNode = None
        self.NodeHasKey: bool = False
        self.ToLeft: bool = False


class BST:

    def __init__(self, node: BSTNode):
        self.Root: BSTNode = node  # корень дерева, или None

    def __FindNodeByKey(
        self, key: int, Node_BST: BSTNode
    ) -> BSTNode | bool | bool or bool:
        if self.Root.NodeKey == key:
            return Node_BST, True, False
        if key == Node_BST.NodeKey:
            return Node_BST, True, False
        if key < Node_BST.NodeKey and Node_BST.LeftChild is None:
            return Node_BST, False, True
        if key > Node_BST.NodeKey and Node_BST.RightChild is None:
            return Node_BST, False, False
        if key < Node_BST.NodeKey:
            if Node_BST.LeftChild:
                return self.__FindNodeByKey(key, Node_BST.LeftChild)
        if key > Node_BST.NodeKey:
            if Node_BST.RightChild:
                return self.__FindNodeByKey(key, Node_BST.RightChild)
        return None

    def FindNodeByKey(self, key: int) -> BSTNode | bool | bool:
        # исключение для пустого дерева
        if self.Root is None:
            intermediate_result: BSTFind = BSTFind()
            intermediate_result.Node = None
            intermediate_result.NodeHasKey = False
            intermediate_result.ToLeft = False
            return intermediate_result

        intermediate_result: BSTFind = BSTFind()
        (
            intermediate_result.Node,
            intermediate_result.NodeHasKey,
            intermediate_result.ToLeft,
        ) = self.__FindNodeByKey(key, self.Root)
        if intermediate_result.Node is not None:
            return intermediate_result
        #else:
        #    return None

    def AddKeyValue(self, key: int, val: int) -> bool:

        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True
        search_result: BSTNode | bool | bool = self.FindNodeByKey(key)
        if search_result.NodeHasKey is True:
            return False  # если ключ уже есть
        if search_result.NodeHasKey is False and search_result.ToLeft is True:
            search_result.Node.LeftChild = BSTNode(key, val, search_result.Node)
            return True
        if search_result.NodeHasKey is False and search_result.ToLeft is False:
            search_result.Node.RightChild = BSTNode(key, val, search_result.Node)
            return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if FromNode.RightChild and FindMax is True:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        if FromNode.LeftChild and FindMax is False:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        return FromNode

    def __Left_DeleteNodeByKey(self, Node_Left: BSTNode, count: int) -> BSTNode:
        if Node_Left.LeftChild is None:
            if count > 0:
                Node_Left.Parent.LeftChild = None
            return Node_Left
        count += 1
        return self.__Left_DeleteNodeByKey(Node_Left.LeftChild, count)

    def DeleteNodeByKey(self, key: int) -> bool:
        search_result: BSTFind = self.FindNodeByKey(key)  # ищем в дереве узел
        node: BSTNode = search_result.Node
        if search_result.NodeHasKey is False:
            return False  # если узел не найден

        # исключение при удалении корня, если в дереве только корень
        if (
            node.NodeKey == self.Root.NodeKey
            and self.Root.LeftChild is None
            and self.Root.RightChild is None
        ):

            self.Root.NodeKey = None
            self.Root.NodeValue = None
            self.Root.Parent = None
            self.Root = None
            return True

        # условие при которм у узла ноль потомков
        if node.LeftChild is None and node.RightChild is None and node.NodeKey is key:

            parent_result: BSTNode | bool | bool = self.FindNodeByKey(
                node.Parent.NodeKey
            )  # ищем родительский узел в дереве
            if (
                parent_result.Node.RightChild is not None
                and parent_result.Node.RightChild.NodeKey is node.NodeKey
            ):
                parent_result.Node.RightChild = None
                return True
            if (
                parent_result.Node.LeftChild is not None
                and parent_result.Node.LeftChild.NodeKey is node.NodeKey
            ):
                parent_result.Node.LeftChild = None
                return True

        if (
            node.NodeKey is key
            and node.NodeKey is self.Root.NodeKey
            and node.LeftChild != None
            and node.RightChild != None
        ):
            # 1. Найти узел на замену удаляемому
            count: int = 0
            new_node: BSTNode = self.__Left_DeleteNodeByKey(node.RightChild, count)

            # 2. Присвоить потомкам найденного узла потомки удаляемого
            if node.RightChild.NodeKey != new_node.NodeKey:
                new_node.RightChild = node.RightChild
            if node.LeftChild.NodeKey != new_node.NodeKey:
                new_node.LeftChild = node.LeftChild

            # 3. Присвоить графе "Parent" потомков значение найденного узла
            if node.RightChild.NodeKey != new_node.NodeKey:
                new_node.RightChild.Parent = new_node

            if node.LeftChild.NodeKey != new_node.NodeKey:
                new_node.LeftChild.Parent = new_node

            # 5. Добавить нового потомка родителю удаляемого узла
            self.Root = new_node
            return True

        # исключение при удалении узла из корня дерева
        if (
            (node.NodeKey is key)
            and (node.NodeKey is self.Root.NodeKey)
            and (node.LeftChild != None or node.RightChild != None)
        ):
            # 1. Присвоить графе "Parent" потомков значение найденного узла
            if node.RightChild:
                node.RightChild.Parent = None
                self.Root = node.RightChild

            if node.LeftChild:
                node.LeftChild.Parent = None
                self.Root = node.LeftChild

            # 2. Добавить нового потомка родителю удаляемого узла
            return True

        # условие при которм у узла один потомок
        if (
            node.LeftChild is None
            and node.RightChild is not None
            and node.NodeKey is key
            and node.Parent is not None
        ):
            parent_result: BSTNode | bool | bool = self.FindNodeByKey(
                node.Parent.NodeKey
            )  # ищем родительский узел в дереве

            if (
                parent_result.Node.RightChild is not None
                and parent_result.Node.RightChild.NodeKey is node.NodeKey
            ):
                node.RightChild.Parent = node.Parent
                parent_result.Node.RightChild = node.RightChild
                return True
            if (
                parent_result.Node.LeftChild is not None
                and parent_result.Node.LeftChild.NodeKey is node.NodeKey
            ):
                node.RightChild.Parent = node.Parent
                parent_result.Node.LeftChild = node.RightChild
                return True

        if (
            node.LeftChild is not None
            and node.RightChild is None
            and node.NodeKey is key
            and node.Parent is not None
        ):

            parent_result: BSTNode | bool | bool = self.FindNodeByKey(
                node.Parent.NodeKey
            )  # ищем родительский узел в дереве

            if (
                parent_result.Node.RightChild is not None
                and parent_result.Node.RightChild.NodeKey is node.NodeKey
            ):
                node.LeftChild.Parent = node.Parent
                parent_result.Node.RightChild = node.LeftChild
                return True
            if (
                parent_result.Node.LeftChild is not None
                and parent_result.Node.LeftChild.NodeKey is node.NodeKey
            ):
                node.LeftChild.Parent = node.Parent
                parent_result.Node.LeftChild = node.LeftChild
                return True

        # условие при которм у узла два потомка
        if (
            node.LeftChild is not None
            and node.RightChild is not None
            and node.NodeKey is key
        ):

            # 1. Найти узел на замену удаляемому
            count: int = 0
            new_node: BSTNode = self.__Left_DeleteNodeByKey(node.RightChild, count)

            # 2. Присвоить потомкам найденного узла потомки удаляемого
            if node.RightChild.NodeKey != new_node.NodeKey:
                new_node.RightChild = node.RightChild
            if node.LeftChild.NodeKey != new_node.NodeKey:
                new_node.LeftChild = node.LeftChild

            # 3. Присвоить графе "Parent" найденного узла "Parent" удаляемого узла
            new_node.Parent = node.Parent

            # 4. Присвоить графе "Parent" потомков значение найденного узла
            if (
                node.RightChild.NodeKey != new_node.NodeKey
                and node.NodeKey == self.Root.NodeKey
            ):
                new_node.RightChild.Parent = new_node

            if (
                node.LeftChild.NodeKey != new_node.NodeKey
                and node.NodeKey == self.Root.NodeKey
            ):
                new_node.LeftChild.Parent = new_node

            if (
                node.RightChild.NodeKey != new_node.NodeKey
                and node.NodeKey != self.Root.NodeKey
            ):
                new_node.RightChild.Parent = new_node

            if (
                node.LeftChild.NodeKey != new_node.NodeKey
                and node.NodeKey != self.Root.NodeKey
            ):
                new_node.LeftChild.Parent = new_node

            # 5. Добавить нового потомка родителю удаляемого узла

            if (
                node.NodeKey != self.Root.NodeKey
                and node.Parent.LeftChild is not None
                and node.Parent.LeftChild.NodeKey == node.NodeKey
            ):
                node.Parent.LeftChild = new_node

            if (
                node.NodeKey != self.Root.NodeKey
                and node.Parent.RightChild is not None
                and node.Parent.RightChild.NodeKey == node.NodeKey
            ):
                node.Parent.RightChild = new_node

            if self.Root.NodeKey == node.NodeKey:
                self.Root = new_node

    def __Count(self, node_1: BSTNode, list_node_1: list) -> int:
        if node_1 is not None:
            self.__Count(node_1.RightChild, list_node_1)
            list_node_1.append(node_1)
            self.__Count(node_1.LeftChild, list_node_1)
            return len(list_node_1)

    def Count(self) -> int:  # количество узлов в дереве
        if self.Root is None:
            return 0
        node: BSTNode = self.Root
        list_node: list = []
        return self.__Count(node, list_node)
