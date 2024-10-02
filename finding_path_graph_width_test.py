# Этот файл предназначен для тестирования finding_path_graph_width.py
import unittest

from finding_path_graph_width import Stack, Vertex, SimpleGraph, Queue


class MyTests(unittest.TestCase):


    def test1(self):
        gr = SimpleGraph(8)

        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)
        gr.AddVertex(7)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(2, 4)
        gr.AddEdge(2, 5)
        gr.AddEdge(3, 6)
        gr.AddEdge(3, 7)

        result_method = gr.BreadthFirstSearch(0, 6)
        self.assertEqual(result_method[0].Value, 0)
        self.assertEqual(result_method[1].Value, 3)
        self.assertEqual(result_method[2].Value, 6)

    def test2(self):
        gr = SimpleGraph(8)

        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)
        gr.AddVertex(7)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(2, 4)
        gr.AddEdge(2, 5)
        gr.AddEdge(3, 6)
        gr.AddEdge(3, 7)

        result_method = gr.BreadthFirstSearch(0, 7)
        self.assertEqual(result_method[0].Value, 0)
        self.assertEqual(result_method[1].Value, 3)
        self.assertEqual(result_method[2].Value, 7)


    def test3(self):
        gr = SimpleGraph(8)

        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)
        gr.AddVertex(7)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(2, 4)
        gr.AddEdge(2, 5)
        gr.AddEdge(3, 6)
        gr.AddEdge(3, 7)

        result_method = gr.BreadthFirstSearch(3, 7)
        self.assertEqual(result_method[0].Value, 3)
        self.assertEqual(result_method[1].Value, 7)


    def test4(self):
        gr = SimpleGraph(9)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)
        gr.AddVertex(7)
        gr.AddVertex(8)

        gr.AddEdge(0, 1)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(3, 2)
        gr.AddEdge(3, 5)
        gr.AddEdge(3, 7)
        gr.AddEdge(2, 6)
        gr.AddEdge(7, 8)

        result_method = gr.BreadthFirstSearch(3, 8)
        self.assertEqual(result_method[0].Value, 3)
        self.assertEqual(result_method[1].Value, 7)
        self.assertEqual(result_method[2].Value, 8)

    def test5(self):
        gr = SimpleGraph(10)

        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)
        gr.AddVertex(7)
        gr.AddVertex(8)
        gr.AddVertex(9)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(1, 5)
        gr.AddEdge(1, 6)
        gr.AddEdge(6, 7)
        gr.AddEdge(2, 7)
        gr.AddEdge(3, 8)
        gr.AddEdge(8, 9)
        gr.AddEdge(9, 7)

        result_method = gr.BreadthFirstSearch(0, 7)
        self.assertEqual(result_method[0].Value, 0)
        self.assertEqual(result_method[1].Value, 2)
        self.assertEqual(result_method[2].Value, 7)

    def test6(self):
        gr = SimpleGraph(9)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)
        gr.AddVertex(7)
        gr.AddVertex(8)

        gr.AddEdge(0, 1)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(3, 2)
        gr.AddEdge(3, 5)
        gr.AddEdge(3, 7)
        gr.AddEdge(2, 6)
        gr.AddEdge(7, 8)

        result_method = gr.BreadthFirstSearch(3, 8)
        self.assertEqual(result_method[0].Value, 3)
        self.assertEqual(result_method[1].Value, 7)
        self.assertEqual(result_method[2].Value, 8)

    def test7(self):
        gr = SimpleGraph(10)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)
        gr.AddVertex(7)
        gr.AddVertex(8)
        gr.AddVertex(9)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(1, 5)
        gr.AddEdge(1, 6)
        gr.AddEdge(2, 7)
        gr.AddEdge(3, 8)
        gr.AddEdge(6, 7)
        gr.AddEdge(8, 9)
        gr.AddEdge(9, 7)

        result_method = gr.BreadthFirstSearch(0, 7)
        self.assertEqual(result_method[0].Value, 0)
        self.assertEqual(result_method[1].Value, 2)
        self.assertEqual(result_method[2].Value, 7)

    def test8(self): # тест по ошибке
        gr = SimpleGraph(6)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(2, 3)
        gr.AddEdge(3, 3)
        gr.AddEdge(3, 4)
        gr.AddEdge(4, 5)

        st = gr.BreadthFirstSearch(0, 4)

        self.assertEqual(st[0].Value, 0)
        self.assertEqual(st[1].Value, 1)
        self.assertEqual(st[2].Value, 4)

    def test9(self):
        gr = SimpleGraph(6)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(2, 3)
        gr.AddEdge(3, 3)
        gr.AddEdge(3, 4)
        gr.AddEdge(4, 5)

        st = gr.BreadthFirstSearch(2, 4)

        self.assertEqual(st[0].Value, 2)
        self.assertEqual(st[1].Value, 3)
        self.assertEqual(st[2].Value, 4)

    def test10(self):
        gr = SimpleGraph(6)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(2, 3)
        gr.AddEdge(3, 3)
        gr.AddEdge(3, 4)
        gr.AddEdge(4, 5)

        st = gr.BreadthFirstSearch(3, 4)

        self.assertEqual(st[0].Value, 3)
        self.assertEqual(st[1].Value, 4)

    def test11(self):
        gr = SimpleGraph(6)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(2, 3)
        gr.AddEdge(3, 3)
        gr.AddEdge(3, 4)
        gr.AddEdge(4, 5)

        st = gr.BreadthFirstSearch(0, 5)

        self.assertEqual(st[0].Value, 0)
        self.assertEqual(st[1].Value, 1)
        self.assertEqual(st[2].Value, 4)
        self.assertEqual(st[3].Value, 5)

    def test12(self):
        gr = SimpleGraph(6)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(2, 3)
        gr.AddEdge(3, 3)
        gr.AddEdge(3, 4)
        gr.AddEdge(4, 5)

        st = gr.BreadthFirstSearch(3, 5)

        self.assertEqual(st[0].Value, 3)
        self.assertEqual(st[1].Value, 4)
        self.assertEqual(st[2].Value, 5)

    def test13(self):
        gr = SimpleGraph(6)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(2, 3)
        gr.AddEdge(3, 3)
        gr.AddEdge(3, 4)
        gr.AddEdge(4, 5)

        st = gr.BreadthFirstSearch(0, 5)

        self.assertEqual(st[0].Value, 0)
        self.assertEqual(st[1].Value, 1)
        self.assertEqual(st[2].Value, 4)
        self.assertEqual(st[3].Value, 5)

if __name__ == "__main__":
    unittest.main()
