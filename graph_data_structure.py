class Vertex:

    def __init__(self, val):
        self.Value = val


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
