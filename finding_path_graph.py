class Stack:
    def __init__(self):
        self.stack = []

    def size(self):  # метод длины стека
        return len(self.stack)

    def pop(self):  # метод удаления последнего добавленного элемента
        if len(self.stack) == 0:
            return None  # если стек пустой
        el = self.stack[0]
        del self.stack[0]
        return el

    def push(self, value):  # метод добавления элемента
        self.stack = [value] + self.stack

    def peek(self):  # метод "возврата" последнего добавленного элемента
        if len(self.stack) == 0:
            return None  # если стек пустой
        return self.stack[0]


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # добавление новой вершины
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break

    def RemoveVertex(self, v):
        # код удаления вершины со всеми её рёбрами
        if self.vertex[v] is not None:
            self.vertex[v] = None

        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.m_adjacency[v2][v1] == 1:
            return True
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        if self.m_adjacency[v2][v1] != 1:
            self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        if self.m_adjacency[v2][v1] == 1:
            self.m_adjacency[v2][v1] = 0

    def _DepthFirstSearch(self, stack_for_graph, vertwx_x, VFrom, VTo):

        for n in range(self.max_vertex):
            # если узел найден, записываем его в стек и возвращаем сам стек как результат работы
            if self.m_adjacency[n][VFrom] == 1 and self.vertex[n].Value == VTo:
                stack_for_graph.push(self.vertex[n])
                return stack_for_graph

        for top in range(self.max_vertex):
            if self.m_adjacency[top][VFrom] == 1 and self.vertex[top].Hit is False:
                vertwx_x = self.vertex[top]
                vertwx_x.Hit = True
                stack_for_graph.push(vertwx_x)
                self._DepthFirstSearch(
                    stack_for_graph, vertwx_x, self.vertex.index(vertwx_x), VTo
                )

        stack_for_graph.pop()
        if stack_for_graph.size() == 0:
            return False

        vertwx_x = stack_for_graph.peek()
        vertwx_x.Hit = True

        return self._DepthFirstSearch(
            stack_for_graph, vertwx_x, self.vertex.index(vertwx_x), VTo
        )

    def DepthFirstSearch(self, VFrom, VTo):

        # очищаем все дополнительные структуры данных: делаем стек пустым,
        # а все вершины графа отмечаем как непосещённые
        stack_for_graph = Stack()
        for _ in range(stack_for_graph.size()):
            stack_for_graph.pop()

        # выбираем текущую вершину
        vertwx_x = self.vertex[0]

        # фиксируем вершину как посещённую
        vertwx_x.Hit = True

        # помещаем вершину в стек
        stack_for_graph.push(vertwx_x)

        result_recursive_function = self._DepthFirstSearch(
            stack_for_graph, vertwx_x, VFrom, VTo
        )
        if result_recursive_function is False:
            return False
        list_nodes_Vertex = []
        for _ in range(result_recursive_function.size()):
            list_nodes_Vertex.append(result_recursive_function.pop())
        return list_nodes_Vertex
