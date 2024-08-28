# Этот файл предназначен для тестирования binary_search_trees_two.py
import unittest

from binary_search_trees_two import aBST


class MyTests(unittest.TestCase):

    def test1(self):

        array = aBST(3)
        array.AddKey(10)
        array.AddKey(12)
        array.AddKey(14)
        array.AddKey(11)
        array.AddKey(6)
        array.AddKey(4)
        array.AddKey(8)

        self.assertEqual(array.FindKeyIndex(10), 0)
        self.assertEqual(array.FindKeyIndex(12), 2)
        self.assertEqual(array.FindKeyIndex(14), 6)
        self.assertEqual(array.FindKeyIndex(11), 5)
        self.assertEqual(array.FindKeyIndex(6), 1)
        self.assertEqual(array.FindKeyIndex(4), 3)
        self.assertEqual(array.FindKeyIndex(8), 4)

    def test2(self):

        array = aBST(5)
        array.AddKey(10)
        array.AddKey(12)
        array.AddKey(14)
        array.AddKey(11)
        array.AddKey(6)
        array.AddKey(4)
        array.AddKey(8)

        self.assertEqual(array.FindKeyIndex(10), 0)
        self.assertEqual(array.FindKeyIndex(12), 2)
        self.assertEqual(array.FindKeyIndex(14), 6)
        self.assertEqual(array.FindKeyIndex(11), 5)
        self.assertEqual(array.FindKeyIndex(6), 1)
        self.assertEqual(array.FindKeyIndex(4), 3)
        self.assertEqual(array.FindKeyIndex(8), 4)

        self.assertEqual(array.FindKeyIndex(4), 3)
        self.assertEqual(array.FindKeyIndex(8), 4)

    def test3(self):

        array = aBST(4)
        array.AddKey(10)
        array.AddKey(8)
        array.AddKey(3)
        array.AddKey(9)
        array.AddKey(100)
        array.AddKey(150)
        array.AddKey(160)
        array.AddKey(140)
        array.AddKey(90)
        array.AddKey(145)
        array.AddKey(130)
        array.AddKey(1)

        self.assertEqual(array.FindKeyIndex(10), 0)
        self.assertEqual(array.FindKeyIndex(8), 1)
        self.assertEqual(array.FindKeyIndex(3), 3)
        self.assertEqual(array.FindKeyIndex(9), 4)
        self.assertEqual(array.FindKeyIndex(100), 2)
        self.assertEqual(array.FindKeyIndex(150), 6)
        self.assertEqual(array.FindKeyIndex(160), 14)
        self.assertEqual(array.FindKeyIndex(140), 13)
        self.assertEqual(array.FindKeyIndex(90), 5)
        self.assertEqual(array.FindKeyIndex(145), 28)
        self.assertEqual(array.FindKeyIndex(130), 27)
        self.assertEqual(array.FindKeyIndex(1), 7)

    def test4(self):

        array = aBST(4)
        array.AddKey(10)
        array.AddKey(8)
        array.AddKey(3)
        array.AddKey(9)
        array.AddKey(100)
        array.AddKey(150)
        array.AddKey(160)
        array.AddKey(140)
        array.AddKey(90)
        array.AddKey(145)
        array.AddKey(130)
        array.AddKey(1)
        array.AddKey(160)

        self.assertEqual(array.AddKey(180), -30)
        self.assertEqual(array.FindKeyIndex(180), 30)
        self.assertEqual(array.AddKey(200), -1)
        self.assertEqual(array.AddKey(259), -1)

        self.assertEqual(array.FindKeyIndex(10), 0)
        self.assertEqual(array.FindKeyIndex(8), 1)
        self.assertEqual(array.FindKeyIndex(3), 3)
        self.assertEqual(array.FindKeyIndex(9), 4)
        self.assertEqual(array.FindKeyIndex(100), 2)
        self.assertEqual(array.FindKeyIndex(150), 6)
        self.assertEqual(array.FindKeyIndex(160), 14)
        self.assertEqual(array.FindKeyIndex(140), 13)
        self.assertEqual(array.FindKeyIndex(90), 5)
        self.assertEqual(array.FindKeyIndex(145), 28)
        self.assertEqual(array.FindKeyIndex(130), 27)
        self.assertEqual(array.FindKeyIndex(1), 7)

        self.assertEqual(array.FindKeyIndex(1), 7)
        self.assertEqual(array.FindKeyIndex(259), None)

    def test5(self):

        array = aBST(1)
        array.AddKey(10)
        array.AddKey(15)
        array.AddKey(5)

        self.assertEqual(array.AddKey(15), -1)
        self.assertEqual(array.AddKey(10), -1)
        self.assertEqual(array.AddKey(5), -1)

        self.assertEqual(array.FindKeyIndex(10), 0)
        self.assertEqual(array.FindKeyIndex(15), 2)
        self.assertEqual(array.FindKeyIndex(5), 1)

        self.assertEqual(array.FindKeyIndex(100), None)
        self.assertEqual(array.FindKeyIndex(150), None)
        self.assertEqual(array.FindKeyIndex(50), None)

    def test6(self):

        array = aBST(3)
        array.AddKey(50)
        array.AddKey(25)
        array.AddKey(75)
        array.AddKey(37)
        array.AddKey(62)
        array.AddKey(84)
        array.AddKey(31)
        array.AddKey(43)
        array.AddKey(55)
        array.AddKey(92)

        self.assertEqual(array.AddKey(50), -1)
        self.assertEqual(array.AddKey(25), -1)
        self.assertEqual(array.AddKey(75), -1)
        self.assertEqual(array.AddKey(37), -1)
        self.assertEqual(array.AddKey(62), -1)
        self.assertEqual(array.AddKey(84), -1)
        self.assertEqual(array.AddKey(31), -1)
        self.assertEqual(array.AddKey(43), -1)
        self.assertEqual(array.AddKey(55), -1)
        self.assertEqual(array.AddKey(92), -1)


if __name__ == "__main__":
    unittest.main()
