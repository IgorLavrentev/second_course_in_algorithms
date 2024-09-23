# Этот файл предназначен для тестирования finding_path_graph.py
import unittest

from finding_path_graph import Stack, Vertex, SimpleGraph


class MyTests(unittest.TestCase):

    def test1(self):
        gr = SimpleGraph(7)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)

        gr.AddEdge(0, 1)
        gr.AddEdge(0, 2)
        gr.AddEdge(0, 3)
        gr.AddEdge(1, 2)
        gr.AddEdge(1, 6)
        gr.AddEdge(2, 3)
        gr.AddEdge(2, 6)
        gr.AddEdge(3, 4)
        gr.AddEdge(3, 6)
        gr.AddEdge(4, 5)

        st = gr.DepthFirstSearch(0, 5)
        self.assertEqual(st[0].Value, 5)
        self.assertEqual(st[1].Value, 4)
        self.assertEqual(st[2].Value, 3)
        self.assertEqual(st[3].Value, 2)
        self.assertEqual(st[4].Value, 1)
        self.assertEqual(st[5].Value, 0)

    def test2(self):
        gr = SimpleGraph(7)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)

        gr.AddEdge(0, 3)
        gr.AddEdge(1, 2)
        gr.AddEdge(3, 5)
        gr.AddEdge(3, 6)
        gr.AddEdge(4, 2)


        st = gr.DepthFirstSearch(0, 6)
        self.assertEqual(st[0].Value, 6)

    def test3(self):
        gr = SimpleGraph(3)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)

        gr.AddEdge(0, 2)

        st = gr.DepthFirstSearch(0, 2)
        self.assertEqual(st[0].Value, 2)


    def test4(self):
        gr = SimpleGraph(3)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)

        gr.AddEdge(0, 2)

        st = gr.DepthFirstSearch(0, 4)
        self.assertEqual(st, False)

    def test5(self):
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

        st = gr.DepthFirstSearch(0, 8)
        self.assertEqual(st[0].Value, 8)
        self.assertEqual(st[1].Value, 7)
        self.assertEqual(st[2].Value, 3)
        self.assertEqual(st[3].Value, 1)
        self.assertEqual(st[4].Value, 0)

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

        st = gr.DepthFirstSearch(3, 8)
        self.assertEqual(st[0].Value, 8)
        self.assertEqual(st[1].Value, 7)
        self.assertEqual(st[2].Value, 3)

    def test7(self):
        gr = SimpleGraph(7)
        gr.AddVertex(0)
        gr.AddVertex(1)
        gr.AddVertex(2)
        gr.AddVertex(3)
        gr.AddVertex(4)
        gr.AddVertex(5)
        gr.AddVertex(6)

        gr.AddEdge(0, 1)
        gr.AddEdge(1, 5)
        gr.AddEdge(1, 2)
        gr.AddEdge(2, 3)
        gr.AddEdge(2, 4)
        gr.AddEdge(2, 5)
        gr.AddEdge(2, 6)

        st = gr.DepthFirstSearch(1, 6)
        self.assertEqual(st[0].Value, 6)
        self.assertEqual(st[1].Value, 2)
        self.assertEqual(st[2].Value, 1)

    def test8(self):
        gr = SimpleGraph(7)
        gr.AddVertex(0)
        gr.AddVertex(1)

        gr.AddEdge(0, 0)

        st = gr.DepthFirstSearch(0, 0)
        self.assertEqual(st[0].Value, 0)

    def test9(self):
        gr = SimpleGraph(7)
        gr.AddVertex(0)
        gr.AddVertex(1)

        gr.AddEdge(0, 0)

        st = gr.DepthFirstSearch(0, 2)
        self.assertEqual(st, False)

    def test10(self):
        gr = SimpleGraph(11)
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
        gr.AddVertex(10)

        gr.AddEdge(0, 5)
        gr.AddEdge(1, 2)
        gr.AddEdge(1, 3)
        gr.AddEdge(1, 4)
        gr.AddEdge(4, 6)
        gr.AddEdge(4, 7)
        gr.AddEdge(4, 8)
        gr.AddEdge(5, 8)
        gr.AddEdge(8, 9)
        gr.AddEdge(8, 10)

        st = gr.DepthFirstSearch(1, 10)
        self.assertEqual(st[0].Value, 10)
        self.assertEqual(st[1].Value, 8)
        self.assertEqual(st[2].Value, 4)
        self.assertEqual(st[3].Value, 1)

    def test11(self):
        gr = SimpleGraph(13)
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
        gr.AddVertex(10)
        gr.AddVertex(11)
        gr.AddVertex(12)

        gr.AddEdge(0, 1)
        gr.AddEdge(1, 8)
        gr.AddEdge(1, 2)
        gr.AddEdge(2, 3)
        gr.AddEdge(2, 9)
        gr.AddEdge(2, 10)
        gr.AddEdge(3, 11)
        gr.AddEdge(3, 12)
        gr.AddEdge(3, 4)
        gr.AddEdge(4, 1)
        gr.AddEdge(4, 5)
        gr.AddEdge(4, 6)
        gr.AddEdge(4, 7)

        st = gr.DepthFirstSearch(1, 7)
        self.assertEqual(st[0].Value, 7)
        self.assertEqual(st[1].Value, 4)
        self.assertEqual(st[2].Value, 3)
        self.assertEqual(st[3].Value, 2)
        self.assertEqual(st[4].Value, 1)

if __name__ == "__main__":
    unittest.main()
