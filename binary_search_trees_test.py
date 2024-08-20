# Этот файл предназначен для тестирования binary_search_trees.py
import unittest

from binary_search_trees import BSTNode, BSTFind, BST


class MyTests(unittest.TestCase):

    def test1(self):  # метод поиска

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        result_of_function = tree.FindNodeByKey(120)
        self.assertEqual(result_of_function[0].NodeValue, 20)

    def test12(self):  # метод поиска

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        self.assertEqual(tree.FindNodeByKey(100)[0].NodeValue, 1001)

    def test13(self):  # метод поиска

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(90, 30)
        self.assertEqual(tree.FindNodeByKey(90)[0].NodeValue, 30)

    def test2(self):  # метод добавления нового узла

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.FindNodeByKey(90)[1], False)
        tree.AddKeyValue(90, 30)
        self.assertEqual(tree.FindNodeByKey(90)[0].NodeValue, 30)

    def test21(self):  # метод добавления нового узла

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.FindNodeByKey(120)[1], False)
        tree.AddKeyValue(120, 20)
        self.assertEqual(tree.FindNodeByKey(120)[0].NodeValue, 20)

    def test22(self):  # метод добавления нового узла

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.FindNodeByKey(110)[1], True)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.FindNodeByKey(110)[0].NodeValue, 10)
        root = BSTNode(100, 1001, None)

    def test23(self):  # метод добавления нового узла

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 100)
        self.assertEqual(tree.FindNodeByKey(100)[0].NodeKey, 100)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.Count(), 2)
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 110)
        self.assertEqual(tree.FindNodeByKey(110)[0].NodeKey, 110)
        self.assertEqual(tree.FindNodeByKey(100)[0].NodeKey, 100)

    def test24(self):  # метод добавления нового узла

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        self.assertEqual(tree.Count(), 1)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        tree.AddKeyValue(180, 60)
        tree.AddKeyValue(200, 80)
        tree.AddKeyValue(195, 75)
        self.assertEqual(tree.Count(), 9)
        self.assertEqual(tree.FinMinMax(root, False).NodeKey, 90)
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 200)
        self.assertEqual(tree.FindNodeByKey(195)[0].NodeKey, 195)

    def test25(self):  # метод добавления нового узла

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.Count(), 2)
        tree.DeleteNodeByKey(110)
        self.assertEqual(tree.Count(), 1)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.Count(), 2)
        self.assertEqual(tree.FinMinMax(root, False).NodeKey, 100)
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 110)
        self.assertEqual(tree.FindNodeByKey(110)[0].NodeKey, 110)

    def test26(self):  # метод добавления нового узла

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.Count(), 2)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.Count(), 2)
        self.assertEqual(tree.FindNodeByKey(110)[0].NodeKey, 110)

    def test3(self):  # ищем максимальный/минимальный ключ в поддереве

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 120)

    def test31(self):  # ищем максимальный/минимальный ключ в поддереве

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        self.assertEqual(tree.FinMinMax(root, False).NodeKey, 90)

    def test32(self):  # ищем максимальный/минимальный ключ в поддереве

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        self.assertEqual(tree.FinMinMax(root.LeftChild, False).NodeKey, 90)

    def test33(self):  # ищем максимальный/минимальный ключ в поддереве

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        self.assertEqual(tree.FinMinMax(root.RightChild, True).NodeKey, 190)

    def test4(self):  # удаляем узел по ключу
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        self.assertEqual(tree.Count(), 6)
        self.assertEqual(tree.FindNodeByKey(190)[0].NodeKey, 190)
        tree.DeleteNodeByKey(190)
        self.assertEqual(tree.Count(), 5)
        self.assertEqual(tree.FindNodeByKey(190)[0].NodeKey, 140)

    def test41(self):  # удаляем узел по ключу
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        self.assertEqual(tree.Count(), 6)
        self.assertEqual(tree.FindNodeByKey(190)[0].NodeKey, 190)
        tree.DeleteNodeByKey(190)
        self.assertEqual(tree.Count(), 5)
        self.assertEqual(tree.FindNodeByKey(190)[0].NodeKey, 140)

    def test42(self):  # удаляем узел по ключу

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        self.assertEqual(tree.FindNodeByKey(140)[0].NodeKey, 140)
        tree.DeleteNodeByKey(140)
        self.assertEqual(tree.FindNodeByKey(140)[1], False)

    def test43(self):  # удаляем узел по ключу

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        tree.AddKeyValue(180, 60)
        self.assertEqual(tree.FindNodeByKey(190)[0].NodeKey, 190)
        tree.DeleteNodeByKey(190)
        self.assertEqual(tree.FindNodeByKey(190)[1], False)

    def test44(self):  # удаляем узел по ключу

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        tree.AddKeyValue(180, 60)
        tree.AddKeyValue(200, 80)
        self.assertEqual(tree.FindNodeByKey(190)[0].NodeKey, 190)
        tree.DeleteNodeByKey(190)
        self.assertEqual(tree.FindNodeByKey(190)[1], False)

    def test45(self):  # удаляем узел по ключу

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        tree.AddKeyValue(180, 60)
        tree.AddKeyValue(200, 80)
        self.assertEqual(tree.FindNodeByKey(100)[0].NodeKey, 100)
        tree.DeleteNodeByKey(100)
        self.assertEqual(tree.FindNodeByKey(100)[1], False)

    def test46(self):  # удаляем узел по ключу

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        tree.AddKeyValue(180, 60)
        tree.AddKeyValue(200, 80)
        tree.AddKeyValue(195, 75)
        self.assertEqual(tree.FindNodeByKey(190)[0].NodeKey, 190)
        tree.DeleteNodeByKey(190)
        self.assertEqual(tree.FindNodeByKey(190)[1], False)

    def test47(self):  # удаляем узел по ключу (узел не найден)

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(150, 50)
        tree.AddKeyValue(130, 60)
        tree.AddKeyValue(115, 35)
        tree.AddKeyValue(145, 75)
        tree.AddKeyValue(142, 7)
        self.assertEqual(tree.DeleteNodeByKey(200), False)

    def test48(self): # удаляем узел по ключу (удаление дерева состоящего только из корня)

        root = BSTNode(100, 1001, None)
        tree = BST(root)
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.DeleteNodeByKey(100), True)
        self.assertEqual(tree.Count(), 0)
        self.assertEqual(tree.Root, None)
        self.assertEqual(root.NodeKey, None)
        self.assertEqual(root.NodeValue, None)
        self.assertEqual(root.Parent, None)

    def test49(self):  # удаляем узел по ключу (удалние узла у которого нет потомков)
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(150, 50)
        tree.AddKeyValue(130, 60)
        tree.AddKeyValue(115, 35)
        tree.AddKeyValue(145, 75)
        tree.AddKeyValue(142, 7)
        self.assertEqual(tree.FindNodeByKey(90)[0].NodeKey, 90)
        tree.DeleteNodeByKey(90)
        self.assertEqual(tree.FindNodeByKey(90)[1], False)

    def test491(
        self,
    ):  # удаляем узел по ключу (удаление узла у которого один потомок слева)
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(150, 50)
        tree.AddKeyValue(130, 60)
        tree.AddKeyValue(115, 35)
        tree.AddKeyValue(145, 75)
        tree.AddKeyValue(142, 7)
        tree.AddKeyValue(80, 2)
        self.assertEqual(tree.FindNodeByKey(90)[0].NodeKey, 90)
        tree.DeleteNodeByKey(90)
        self.assertEqual(tree.FindNodeByKey(90)[1], False)

    def test492(
        self,
    ):  # удаляем узел по ключу (удаление узла у которого потомок справа)
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(150, 50)
        tree.AddKeyValue(130, 60)
        tree.AddKeyValue(115, 35)
        tree.AddKeyValue(145, 75)
        tree.AddKeyValue(142, 7)
        self.assertEqual(tree.FindNodeByKey(110)[0].NodeKey, 110)
        tree.DeleteNodeByKey(110)
        self.assertEqual(tree.FindNodeByKey(110)[1], False)

    def test493(self):  # удаляем узел по ключу (удаление узла у которого потомок справа и слева)
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(150, 50)
        tree.AddKeyValue(130, 60)
        tree.AddKeyValue(115, 35)
        self.assertEqual(tree.FindNodeByKey(140)[0].NodeKey, 140)
        tree.DeleteNodeByKey(140)
        self.assertEqual(tree.FindNodeByKey(140)[1], False)

    def test494(
        self,
    ):  # удаляем узел по ключу (удаление узла у которого потомок справа и слева +)
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(150, 50)
        tree.AddKeyValue(130, 60)
        tree.AddKeyValue(115, 35)
        tree.AddKeyValue(145, 75)
        tree.AddKeyValue(142, 7)
        self.assertEqual(tree.FindNodeByKey(120)[0].NodeKey, 120)
        tree.DeleteNodeByKey(120)
        self.assertEqual(tree.FindNodeByKey(120)[1], False)

    def test495(self):  # удаляем узел по ключу (удаление узла у которого потомок справа и слева)
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        self.assertEqual(tree.Count(), 1)
        tree.DeleteNodeByKey(100)
        self.assertEqual(tree.Count(), 0)
        tree.AddKeyValue(100, 1001)
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.FindNodeByKey(100)[1], True)

    def test496(self):  # удаляем узел по ключу (удаление узла у которого потомок справа и слева)
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(101, 1002)
        tree.AddKeyValue(98, 1003)
        tree.AddKeyValue(99, 1004)
        tree.AddKeyValue(103, 1005)
        self.assertEqual(tree.Count(), 5)
        self.assertEqual(tree.FinMinMax(root, False).NodeKey, 98)
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 103)
        tree.DeleteNodeByKey(103)
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 101)
        tree.AddKeyValue(103, 1005) 
        self.assertEqual(tree.FinMinMax(root, True).NodeKey, 103)
        self.assertEqual(tree.Count(), 5)

    def test5(self):  # количество узлов в дереве
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        tree.AddKeyValue(120, 20)
        tree.AddKeyValue(90, 30)
        tree.AddKeyValue(140, 40)
        tree.AddKeyValue(190, 70)
        self.assertEqual(tree.Count(), 6)

    def test51(self):  # количество узлов в дереве
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        self.assertEqual(tree.Count(), 1)

    def test52(self):  # количество узлов в дереве
        root = BSTNode(100, 1001, None)
        tree = BST(root)
        tree.AddKeyValue(110, 10)
        self.assertEqual(tree.Count(), 2)
        tree.DeleteNodeByKey(110)
        tree.DeleteNodeByKey(100)
        self.assertEqual(tree.Count(), 0)


if __name__ == "__main__":
    unittest.main()
