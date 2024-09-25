from typing import Union


class Stack:
    def __init__(self):
        self.stack: list = []

    def size(self) -> int:  # метод длины стека
        return len(self.stack)

    def pop(self):  # метод удаления последнего добавленного элемента
        if len(self.stack) == 0:
            return None  # если стек пустой
        el: Vertex = self.stack[0]
        del self.stack[0]
        return el

    def push(self, value) -> None:  # метод добавления элемента
        self.stack = [value] + self.stack

    def peek(self):  # метод "возврата" последнего добавленного элемента
        if len(self.stack) == 0:
            return None  # если стек пустой
        return self.stack[0]


class Vertex:

    def __init__(self, val: int):
        self.Value: int = val
        self.Hit: bool = False


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex: int = size
        self.m_adjacency: list = [[0] * size for _ in range(size)]
        self.vertex: list = [None] * size

    def AddVertex(self, v: int) -> None:
        # добавление новой вершины
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break

    def RemoveVertex(self, v: int) -> None:
        # код удаления вершины со всеми её рёбрами
        if self.vertex[v] is not None:
            self.vertex[v] = None

        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        if self.m_adjacency[v2][v1] == 1:
            return True
        return False

    def AddEdge(self, v1: int, v2: int) -> None:
        # добавление ребра между вершинами v1 и v2
        if self.m_adjacency[v2][v1] != 1:
            self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        # удаление ребра между вершинами v1 и v2
        if self.m_adjacency[v2][v1] == 1:
            self.m_adjacency[v2][v1] = 0

    def _DepthFirstSearch(
        self, stack_for_graph: Stack, vertwx_x: Vertex, VFrom: int, VTo: int
    ) -> Union[Stack, bool]:

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
                return self._DepthFirstSearch(
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

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> Union[list, bool]:

        # очищаем все дополнительные структуры данных: делаем стек пустым,
        # а все вершины графа отмечаем как непосещённые
        stack_for_graph: Stack = Stack()
        for _ in range(stack_for_graph.size()):
            stack_for_graph.pop()

        # выбираем текущую вершину
        vertwx_x: Vertex = self.vertex[VFrom]

        # фиксируем вершину как посещённую
        vertwx_x.Hit = True

        # помещаем вершину в стек
        stack_for_graph.push(vertwx_x)

        result_recursive_function: object = self._DepthFirstSearch(
            stack_for_graph, vertwx_x, VFrom, VTo
        )
        if result_recursive_function is False:
            return []
        list_nodes_Vertex: list = []
        for _ in range(result_recursive_function.size()):
            list_nodes_Vertex.append(result_recursive_function.pop())
        list_nodes_Vertex.reverse()
        return list_nodes_Vertex
