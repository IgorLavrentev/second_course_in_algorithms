# Этот файл предназначен для тестирования pyramids.py
import unittest

from pyramids import Heap


class MyTests(unittest.TestCase):

    def test1(self):
        mass = Heap()
        mass.MakeHeap([6, 4, 3, 2, 1, 0], 2)
        mass.Add(5)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), 5)
        self.assertEqual(mass.GetMax(), 4)
        self.assertEqual(mass.GetMax(), 3)
        self.assertEqual(mass.GetMax(), 2)
        self.assertEqual(mass.GetMax(), 1)
        self.assertEqual(mass.GetMax(), 0)

    def test2(self):
        mass = Heap()
        mass.MakeHeap([6, 4, 3, 2, 1, 0], 3)
        mass.Add(5)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), 5)
        self.assertEqual(mass.GetMax(), 4)
        self.assertEqual(mass.GetMax(), 3)
        self.assertEqual(mass.GetMax(), 2)
        self.assertEqual(mass.GetMax(), 1)
        self.assertEqual(mass.GetMax(), 0)

    def test3(self):
        mass = Heap()
        mass.MakeHeap([6], 3)
        mass.Add(5)
        mass.Add(4)
        mass.Add(3)
        mass.Add(2)
        mass.Add(1)
        mass.Add(0)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), 5)
        self.assertEqual(mass.GetMax(), 4)
        self.assertEqual(mass.GetMax(), 3)
        self.assertEqual(mass.GetMax(), 2)
        self.assertEqual(mass.GetMax(), 1)
        self.assertEqual(mass.GetMax(), 0)

    def test4(self):
        mass = Heap()
        mass.MakeHeap([6], 4)
        mass.Add(5)
        mass.Add(4)
        mass.Add(3)
        mass.Add(2)
        mass.Add(1)
        mass.Add(0)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), 5)
        self.assertEqual(mass.GetMax(), 4)
        self.assertEqual(mass.GetMax(), 3)
        self.assertEqual(mass.GetMax(), 2)
        self.assertEqual(mass.GetMax(), 1)
        self.assertEqual(mass.GetMax(), 0)

    def test5(self):
        mass = Heap()
        mass.MakeHeap([], 2)
        mass.Add(6)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), -1)

    def test6(self):
        mass = Heap()
        mass.MakeHeap([6, 4, 3, 2, 1, 7], 2)
        self.assertEqual(mass.GetMax(), 7)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), 4)
        self.assertEqual(mass.GetMax(), 3)
        self.assertEqual(mass.GetMax(), 2)
        self.assertEqual(mass.GetMax(), 1)

    def test7(self):
        mass = Heap()
        mass.MakeHeap([6, 4, 3, 2, 1, 7], 4)
        self.assertEqual(mass.GetMax(), 7)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), 4)
        self.assertEqual(mass.GetMax(), 3)
        self.assertEqual(mass.GetMax(), 2)
        self.assertEqual(mass.GetMax(), 1)

    def test8(self):
        mass = Heap()
        mass.MakeHeap([1, 4, 3, 2, 5, 6], 3)
        self.assertEqual(mass.GetMax(), 6)
        self.assertEqual(mass.GetMax(), 5)
        mass.Add(6)
        self.assertEqual(mass.GetMax(), 6)

    def test9(self):
        mass = Heap()
        mass.MakeHeap([1, 4, 3, 2, 5, 6], 3)
        self.assertEqual(mass.GetMax(), 6)
        mass.Add(6)
        self.assertEqual(mass.GetMax(), 6)

    def test10(self):
        mass = Heap()
        mass.MakeHeap([110, 90, 40, 70, 80, 30, 10, 20, 50, 60, 65, 31, 29, 11, 9], 3)
        self.assertEqual(mass.GetMax(), 110)
        self.assertEqual(mass.GetMax(), 90)
        self.assertEqual(mass.GetMax(), 80)
        self.assertEqual(mass.GetMax(), 70)
        self.assertEqual(mass.GetMax(), 65)
        self.assertEqual(mass.GetMax(), 60)
        self.assertEqual(mass.GetMax(), 50)
        self.assertEqual(mass.GetMax(), 40)
        self.assertEqual(mass.GetMax(), 31)
        self.assertEqual(mass.GetMax(), 30)
        self.assertEqual(mass.GetMax(), 29)
        self.assertEqual(mass.GetMax(), 20)
        self.assertEqual(mass.GetMax(), 11)
        self.assertEqual(mass.GetMax(), 10)
        self.assertEqual(mass.GetMax(), 9)

    def test11(self):
        mass = Heap()
        mass.MakeHeap([110, 90, 40, 70, 80, 30, 10, 20, 50, 60, 65, 31, 29, 11, 9], 3)
        self.assertEqual(mass.get_MakeHeap(), [110, 90, 40, 70, 80, 31, 11, 20, 50, 60, 65, 30, 29, 10, 9])


if __name__ == "__main__":
    unittest.main()
