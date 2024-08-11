class SimpleTreeNode:

    def __init__(self, val: int, parent: int):
        self.NodeValue: int = val  # значение в узле
        self.Parent: int = parent  # родитель или None для корня
        self.Children: list = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root: int):
        self.Root: int = root  # корень, может быть None

    def AddChild(
        self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode
    )-> None:  # добавление нового дочернего узла существующему ParentNode
        ParentNode.Children.append(NewChild)

    def __DeleteNode(self, NodeToDelete_Parent: int, list_Children: list, count: int, NodeToDelete: SimpleTreeNode) -> None:
        if count == len(list_Children):
            return
        for j in list_Children:
            if NodeToDelete_Parent == j.NodeValue:
                j.Children.remove(NodeToDelete)
                count += 1
                self.__DeleteNode(
                    NodeToDelete_Parent, list_Children, count, NodeToDelete
                )

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:  # удаление существующего узла NodeToDelete
        NodeToDelete_Parent: int = NodeToDelete.Parent
        if NodeToDelete_Parent == self.Root.NodeValue:
            self.Root.Children.remove(NodeToDelete)
            return
        for i in self.Root.Children:
            if NodeToDelete_Parent == i.NodeValue:
                i.Children.remove(NodeToDelete)
            if i.Children != []:
                count: int = 0
                list_Children: list = i.Children
                self.__DeleteNode(
                    NodeToDelete_Parent, list_Children, count, NodeToDelete
                )
        return

    def __GetAllNodes(self, list_all_nodes: list, list_Children: list, count:int) -> None:
        if count == len(list_Children) and list_Children == []:
            return
        count += 1
        for j in list_Children:
            if len(list_all_nodes) == 1:
                limit: int = 1
            elif len(list_all_nodes) != 0:
                limit: int = len(list_all_nodes) - 1
            for r in range(limit):
                if j.NodeValue <= list_all_nodes[0].NodeValue:
                    list_all_nodes.insert(j, 0)
                elif j.NodeValue > list_all_nodes[len(list_all_nodes) - 1].NodeValue:
                    list_all_nodes.append(j)
                elif (
                    list_all_nodes[r].NodeValue
                    < j.NodeValue
                    <= list_all_nodes[r + 1].NodeValue
                ):
                    list_all_nodes.insert(r + 1, j)
            if j.Children != []:
                self.__GetAllNodes(list_all_nodes, j.Children, count)

    def GetAllNodes(self) -> list:  # выдача всех узлов дерева
        list_all_nodes: list = []
        list_all_nodes.append(self.Root)
        for i in self.Root.Children:
            if len(list_all_nodes) == 1:
                limit: int = 1
            elif len(list_all_nodes) != 0:
                limit: int = len(list_all_nodes) - 1
            for k in range(limit):
                if i.NodeValue <= list_all_nodes[0].NodeValue:
                    list_all_nodes.insert(i, 0)
                elif i.NodeValue > list_all_nodes[len(list_all_nodes) - 1].NodeValue:
                    list_all_nodes.append(i)
                elif (
                    list_all_nodes[k].NodeValue
                    < i.NodeValue
                    <= list_all_nodes[k + 1].NodeValue
                ):
                    list_all_nodes.insert(k + 1, i)
            if i.Children != []:
                count: int = 0
                list_Children: list = i.Children
                self.__GetAllNodes(list_all_nodes, list_Children, count)
        return list_all_nodes

    def __FindNodesByValue(self, val: int, nodes_found_by_value: list, list_Children: list, count: int) -> None:
        if count == len(list_Children) and list_Children == []:
            return
        count += 1
        for j in list_Children:
            if val == j.NodeValue:
                nodes_found_by_value.append(j)
            if j.Children != []:
                self.__FindNodesByValue(val, nodes_found_by_value, j.Children, count)

    def FindNodesByValue(self, val: int) -> list:  # поиск узлов по значению
        nodes_found_by_value: list = []
        if val == self.Root.NodeValue:
            nodes_found_by_value.append(self.Root)
        for i in self.Root.Children:
            if val == i.NodeValue:
                nodes_found_by_value.append(i)
            if i.Children != []:
                count: int = 0
                list_Children: list = i.Children
                self.__FindNodesByValue(val, nodes_found_by_value, list_Children, count)
        return nodes_found_by_value

    # перемещения узла вместе с его поддеревом в качестве дочернего для узла NewParent
    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode) -> None:
        self.AddChild(NewParent, OriginalNode)
        self.DeleteNode(OriginalNode)
        OriginalNode.Parent = NewParent.NodeValue

    def __Count(self, count_Nodes: int, list_Children: list, count: int)-> None:
        if count == len(list_Children) and list_Children == []:
            return
        count += 1
        for j in list_Children:
            self.count_Nodes += 1
            if j.Children != []:
                self.__Count(count_Nodes, j.Children, count)

    def Count(self)-> int:  # количество всех узлов в дереве
        if self.Root is None:
            return None
        self.count_Nodes: int = 1
        for i in self.Root.Children:
            self.count_Nodes += 1
            if i.Children != []:
                count: int = 0
                list_Children: list = i.Children
                self.__Count(self.count_Nodes, list_Children, count)
        return self.count_Nodes

    def __LeafCount(self, number_leaves: int, list_Children: list, count: int) -> None:
        if count == len(list_Children) and list_Children == []:
            return
        for j in list_Children:
            if list_Children[count].Children == []:
                self.number_leaves += 1
            if j.Children != []:
                self.__LeafCount(number_leaves, j.Children, count)
        count += 1

    def LeafCount(self)-> int:  # количество листьев в дереве
        if (
            self.Root.Children == []
        ):  # исключение при котором у дерева один узел и без дочерних узлов
            return 1
        self.number_leaves: int = 0
        for i in self.Root.Children:
            if i.Children == []:
                self.number_leaves += 1
            if i.Children != []:
                count: int = 0
                list_Children: list = i.Children
                self.__LeafCount(self.number_leaves, list_Children, count)
        return self.number_leaves

