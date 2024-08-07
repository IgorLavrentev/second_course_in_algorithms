class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов

class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild): # добавление нового дочернего узла существующему ParentNode
        ParentNode.Children.append(NewChild)

    def __DeleteNode(self, NodeToDelete_Parent, list_Children, count, NodeToDelete):
        if count == len(list_Children):
            return
        for j in list_Children:
            if NodeToDelete_Parent == j.NodeValue:
                j.Children.remove(NodeToDelete)
                count += 1
                self.__DeleteNode(NodeToDelete_Parent, list_Children, count, NodeToDelete)

    def DeleteNode(self, NodeToDelete): # удаление существующего узла NodeToDelete
        NodeToDelete_Parent = NodeToDelete.Parent
        if NodeToDelete_Parent == self.Root.NodeValue:
            self.Root.Children.remove(NodeToDelete)
            return
        for i in self.Root.Children:
            if NodeToDelete_Parent == i.NodeValue:
                i.Children.remove(NodeToDelete)
            if i.Children != []:
                count = 0
                list_Children = i.Children
                self.__DeleteNode(NodeToDelete_Parent, list_Children, count, NodeToDelete)
        return

    def __GetAllNodes(self, list_all_nodes, list_Children, count):
        count = 0
        for j in list_Children:
            list_all_nodes.append(j)
            count += 1
            if j.Children == []:
                return list_all_nodes
            if j.Children != []: # рекурсивный вызов функции (метода) только если список дочерних узлов не путой
                self.__GetAllNodes(list_all_nodes, j.Children, count)

    def GetAllNodes(self): # выдача всех узлов дерева
        list_all_nodes = []
        list_all_nodes.append(self.Root)
        for i in self.Root.Children:
            list_all_nodes.append(i)
            if i.Children != []: 
                count = 0
                list_Children = i.Children
                self.__GetAllNodes(list_all_nodes, list_Children, count)
        return list_all_nodes

    def __FindNodesByValue(self, val, nodes_found_by_value, list_Children, count):
        if count == len(list_Children):
            return nodes_found_by_value
        for j in list_Children:
            if val == j.NodeValue:
                nodes_found_by_value.append(j)
                count += 1
                self.__FindNodesByValue(val, nodes_found_by_value, list_Children, count)

    def FindNodesByValue(self, val): # поиск узлов по значению
        nodes_found_by_value = []
        if val == self.Root.NodeValue:
            nodes_found_by_value.append(self.Root)
        for i in self.Root.Children:
            if val == i.NodeValue:
                nodes_found_by_value.append(i)
            if i.Children != []:
                count = 0
                list_Children = i.Children
                self.__FindNodesByValue(val, nodes_found_by_value, list_Children, count)
        return nodes_found_by_value

    def MoveNode(self, OriginalNode, NewParent): # перемещения узла вместе с его поддеревом в качестве дочернего для узла NewParent
        self.AddChild(NewParent, OriginalNode)
        self.DeleteNode(OriginalNode)

    def __Count(self, count_Nodes, list_Children, count):
        count = 0
        for j in list_Children:
            count_Nodes += 1
            count += 1
            if j.Children == []:
                return count_Nodes
            if j.Children != []: # рекурсивный вызов функции (метода) только если список дочерних узлов не путой
                return self.__Count(count_Nodes, j.Children, count)

    def Count(self): # количество всех узлов в дереве
        if self.Root == None:
            return None
        count_Nodes = 1
        for i in self.Root.Children:
            count_Nodes += 1
            if i.Children != []: 
                count = 0
                list_Children = i.Children
                count_Nodes = self.__Count(count_Nodes, list_Children, count)
        return count_Nodes

    def __LeafCount(self, number_leaves, list_Children, count):
        if count == len(list_Children):
            return number_leaves
        if list_Children[count].Children == []:
            number_leaves += 1
        count += 1
        return self.__LeafCount(number_leaves, list_Children, count)

    def LeafCount(self): # количество листьев в дереве
        if self.Root.Children == []: # исключение при котором у дерева один узел и без дочерних узлов
            return 1
        number_leaves = 0
        for i in self.Root.Children:
            if i.Children == []:
                number_leaves += 1
            if i.Children != []:
                count = 0
                list_Children = i.Children
                number_leaves = self.__LeafCount(number_leaves, list_Children, count)
        return number_leaves

