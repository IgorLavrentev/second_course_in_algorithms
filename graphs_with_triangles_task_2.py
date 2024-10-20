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


class Queue:
    def __init__(self):
        self.queue = []  # инициализация хранилища данных

    def enqueue(self, item):  # вставка в хвост
        self.queue.append(item)

    def dequeue(self):  # выдача из головы
        if len(self.queue) == 0:
            return None  # если очередь пустая
        el = self.queue[0]
        del self.queue[0]
        return el

    def size(self):
        return len(self.queue)  # размер очереди


class Vertex:

    def __init__(self, val: int):
        self.Value: int = val
        self.Hit: bool = False
        self.way: list = []


class SimpleGraph:

    def __init__(self, size: int):
        self.__max_vertex: int = size
        self.__m_adjacency: list = [[0] * size for _ in range(size)]
        self.__vertex: list = [None] * size

    def AddVertex(self, v: int) -> None:
        # добавление новой вершины
        for i in range(len(self.__vertex)):
            if self.__vertex[i] is None:
                self.__vertex[i] = Vertex(v)
                break

    def RemoveVertex(self, v: int) -> None:
        # код удаления вершины со всеми её рёбрами
        if self.__vertex[v] is not None:
            self.__vertex[v] = None

        for i in range(self.__max_vertex):
            self.__m_adjacency[i][v] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        if self.__m_adjacency[v2][v1] == 1:
            return True
        return False

    def AddEdge(self, v1: int, v2: int) -> None:
        # добавление ребра между вершинами v1 и v2
        if self.__m_adjacency[v2][v1] != 1:
            self.__m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        # удаление ребра между вершинами v1 и v2
        if self.__m_adjacency[v2][v1] == 1:
            self.__m_adjacency[v2][v1] = 0

    def _DepthFirstSearch(
        self, stack_for_graph: Stack, vertwx_x: Vertex, VFrom: int, VTo: int
    ) -> Union[Stack, bool]:

        for n in range(self.__max_vertex):
            # если узел найден, записываем его в стек и возвращаем сам стек как результат работы
            if self.__m_adjacency[n][VFrom] == 1 and self.__vertex[n].Value == VTo:
                stack_for_graph.push(self.__vertex[n])
                return stack_for_graph

        for top in range(self.__max_vertex):
            if self.__m_adjacency[top][VFrom] == 1 and self.__vertex[top].Hit is False:
                vertwx_x = self.__vertex[top]
                vertwx_x.Hit = True
                stack_for_graph.push(vertwx_x)
                return self._DepthFirstSearch(
                    stack_for_graph, vertwx_x, self.__vertex.index(vertwx_x), VTo
                )

        stack_for_graph.pop()
        if stack_for_graph.size() == 0:
            return False

        vertwx_x = stack_for_graph.peek()
        vertwx_x.Hit = True

        return self._DepthFirstSearch(
            stack_for_graph, vertwx_x, self.__vertex.index(vertwx_x), VTo
        )

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> Union[list, bool]:

        # очищаем все дополнительные структуры данных: делаем стек пустым,
        # а все вершины графа отмечаем как непосещённые
        stack_for_graph: Stack = Stack()
        for _ in range(stack_for_graph.size()):
            stack_for_graph.pop()

        # выбираем текущую вершину
        vertwx_x: Vertex = self.__vertex[VFrom]

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

    def _BreadthFirstSearch(
        self,
        vertex_x: Vertex,
        queue: Queue,
        VFrom: int,
        VTo: int,
        previous_vertex_list: list,
    ):

        # 2. Из всех смежных с vertwx_x вершин выбираем любую непосещённую
        for el1 in range(self.__max_vertex):
            if self.__m_adjacency[el1][VFrom] == 1 and self.__vertex[el1].Hit is False:
                vertex_x = self.__vertex[el1]
                vertex_x.Hit = True
                queue.enqueue(vertex_x)
                previous_vertex_list.append(vertex_x)
                flag = True  # флаг для выхода из цикла (из двух циклов)
                # добавление текущего пути элементу
                for w in previous_vertex_list:
                    if flag == False:
                        break
                    for el2 in range(self.__max_vertex):
                        if (
                            self.__m_adjacency[el2][w.Value] == 1
                            and self.__vertex[el2].Value == vertex_x.Value
                        ):
                            temporary_list: list = []
                            temporary_list.append(vertex_x)
                            vertex_x.way = w.way + temporary_list
                            flag = False
                            break

                return self._BreadthFirstSearch(
                    vertex_x, queue, VFrom, VTo, previous_vertex_list
                )

            # Если выбранная вершина равна искомой, значит цель найдена, заканчиваем работу
            if vertex_x.Value == VTo:
                return vertex_x.way

        # Если таких вершин нету, проверяем очередь
        # Если очередь пуста, заканчиваем работу (путь до цели не найден)
        if queue.size() == 0:
            return []

        # Иначе извлекаем из очереди очередной элемент, делаем его текущим vertex_x, и переходим обратно к данному п.2
        vertex_x = queue.dequeue()
        del previous_vertex_list[0]

        return self._BreadthFirstSearch(
            vertex_x, queue, vertex_x.Value, VTo, previous_vertex_list
        )

    def BreadthFirstSearch(self, VFrom: int, VTo: int) -> list:

        # 0. Очищаем все дополнительные структуры данных
        for i in range(len(self.__vertex)):
            self.__vertex[i].Hit = False
            self.__vertex[i].way = []

        queue: Queue = Queue()
        for _ in range(queue.size()):
            queue.dequeue()

        # 1. Выбираем текущую вершину vertex_x
        vertex_x: Vertex = self.__vertex[VFrom]
        vertex_x.Hit = True
        vertex_x.way.append(vertex_x)
        previous_vertex_list: list = []
        previous_vertex_list.append(vertex_x)
        result: list = self._BreadthFirstSearch(
            vertex_x, queue, VFrom, VTo, previous_vertex_list
        )

        if result != []:
            resulting_list: list = []
            for k in range(len(result)):
                resulting_list.append(result[k])
            return resulting_list
        return []

    def WeakVertices(self):  # возвращает список узлов вне треугольников
        list_links = []
        res_list = []
        for i in range(len(self.__vertex)):  # цикл по всем элементам графа

            # исключение (если нет связей ни с одним элементом графа)
            summ = 0
            for el in range(len(self.__vertex)):
                if self.__m_adjacency[el][i] != 1:
                    summ += 1
            if summ == len(self.__vertex):
                res_list.append(self.__vertex[i])
                continue

            flag = True
            # формирование всех связей i-го элемента
            for j in range(len(self.__vertex)):
                if i == j:
                    continue
                if self.__m_adjacency[j][i] == 1:
                    list_links.append(self.__vertex[j])

            # проверка всех связей между элементами
            for k in range(len(list_links)):
                if flag is False:
                    break

                for k_2 in range(len(self.__vertex)):
                    if (
                        self.__m_adjacency[k_2][list_links[k].Value] == 1
                        and self.__vertex[k_2] in list_links
                        and k_2 != list_links[k].Value
                    ):
                        flag = False
                        break
                    if k_2 == len(self.__vertex) - 1 and k == len(list_links) - 1:
                        res_list.append(self.__vertex[i])
                        flag = False
                        break
            list_links = []
        return res_list

    # 1.* Добавьте метод, подсчитывающий общее число треугольников в графе
    def total_number_triangles(self):
        nodes_of_triangle = [] # 
        list_links = []
        for i in range(len(self.__vertex)):  # цикл по всем элементам графа

            # исключение (если нет связей ни с одним элементом графа)
            summ = 0
            for el in range(len(self.__vertex)):
                if self.__m_adjacency[el][i] != 1:
                    summ += 1
            if summ == len(self.__vertex):
                continue

            flag = True
            # формирование всех связей i-го элемента
            for j in range(len(self.__vertex)):
                if i == j:
                    continue
                if self.__m_adjacency[j][i] == 1:
                    list_links.append(self.__vertex[j])

            # проверка всех связей между элементами
            for k in range(len(list_links)):
                if flag is False:
                    break

                for k_2 in range(len(self.__vertex)):
                    if (
                        self.__m_adjacency[k_2][list_links[k].Value] == 1
                        and self.__vertex[k_2] in list_links
                        and k_2 != list_links[k].Value
                    ):
                        flag = False
                        if self.__vertex[i] not in nodes_of_triangle:
                            nodes_of_triangle.append(self.__vertex[i])
                        break
                    if k_2 == len(self.__vertex) - 1 and k == len(list_links) - 1:
                        flag = False
                        break
            list_links = []
        return nodes_of_triangle

    def searching_nodes_class_interface(self):
        list_links = []
        res_list = []
        for i in range(len(self.__vertex)):  # цикл по всем элементам графа

            # исключение (если нет связей ни с одним элементом графа)
            summ = 0
            for el in range(len(self.__vertex)):
                if not self.IsEdge(self.vertex[i].Value, self.__vertex[el].Value):
                    summ += 1
            if summ == len(self.__vertex):
                res_list.append(self.__vertex[i])

            flag = True
            # формирование всех связей i-го элемента
            for j in range(len(self.__vertex)):
                if i == j:
                    continue
                if self.IsEdge(self.__vertex[i].Value, self.__vertex[j].Value):
                    list_links.append(self.__vertex[j])

            # проверка всех связей между элементами
            for k in range(len(list_links)):
                if flag is False:
                    break
                for k_2 in range(len(self.__vertex)):
                    if (
                        self.IsEdge(list_links[k].Value, self.__vertex[k_2].Value)
                        and self.__vertex[k_2] in list_links
                        and k_2 != list_links[k].Value
                    ):
                        flag = False
                        break
                    if k_2 == len(self.__vertex) - 1 and k == len(list_links) - 1:
                        res_list.append(self.__vertex[i])
                        flag = False
                        break
            list_links = []
        return res_list

def searching(original_graph, len_original_graph): 
    nodes_tr = original_graph.total_number_triangles()
    res_list = []
    for i in range(len_original_graph):
        found_graph_element = original_graph.BreadthFirstSearch(0, i)
        if found_graph_element[-1] not in nodes_tr:
            res_list.append(found_graph_element[-1])
    return res_list
