import math


class Heap:

    def __init__(self):
        self.HeapArray: list = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a: list, depth: int) -> None:
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        tree_size: int = pow(2, (depth + 1)) - 1
        self.HeapArray = [None] * tree_size  # массив ключей
        for i in a:
            self.Add(i)

    def _GetMax(self, index: int, count: int) -> None:
        if count > len(self.HeapArray):
            return

        if (
            self.HeapArray[(count - 1) // 2] is not None
            and self.HeapArray[count] < self.HeapArray[(count - 1) // 2]
            and (2 * count + 1) >= len(self.HeapArray)
            and (2 * count + 2) >= len(self.HeapArray)
        ):
            return

        if (
            self.HeapArray[(count - 1) // 2] is not None
            and self.HeapArray[count] < self.HeapArray[(count - 1) // 2]
            and self.HeapArray[2 * count + 1] is not None
            and self.HeapArray[2 * count + 2] is not None
            and self.HeapArray[count] > self.HeapArray[2 * count + 1]
            and self.HeapArray[count] > self.HeapArray[2 * count + 2]
        ):
            return

        if (
            self.HeapArray[2 * count + 1] is None
            and self.HeapArray[2 * count + 2] is not None
            and self.HeapArray[count] < self.HeapArray[2 * count + 2]
        ):
            self.HeapArray[count], self.HeapArray[2 * count + 2] = (
                self.HeapArray[2 * count + 2],
                self.HeapArray[count],
            )
            return self._GetMax(index, 2 * count + 2)

        if (
            self.HeapArray[2 * count + 2] is None
            and self.HeapArray[2 * count + 1] is not None
            and self.HeapArray[count] < self.HeapArray[2 * count + 1]
        ):
            self.HeapArray[count], self.HeapArray[2 * count + 1] = (
                self.HeapArray[2 * count + 1],
                self.HeapArray[count],
            )
            return self._GetMax(index, 2 * count + 1)

        if (
            self.HeapArray[2 * count + 1] is not None
            and self.HeapArray[2 * count + 2] is not None
            and self.HeapArray[count] < self.HeapArray[2 * count + 1]
            and self.HeapArray[2 * count + 1] > self.HeapArray[2 * count + 2]
        ):
            self.HeapArray[count], self.HeapArray[2 * count + 1] = (
                self.HeapArray[2 * count + 1],
                self.HeapArray[count],
            )
            return self._GetMax(index, 2 * count + 1)

        if (
            self.HeapArray[2 * count + 1] is not None
            and self.HeapArray[2 * count + 2] is not None
            and self.HeapArray[count] < self.HeapArray[2 * count + 2]
            and self.HeapArray[2 * count + 1] < self.HeapArray[2 * count + 2]
        ):
            self.HeapArray[count], self.HeapArray[2 * count + 2] = (
                self.HeapArray[2 * count + 2],
                self.HeapArray[count],
            )
            return self._GetMax(index, 2 * count + 2)

    def GetMax(self) -> int:
        if all(element is None for element in self.HeapArray):
            return -1  # если куча пуста

        el_root: int = self.HeapArray[0]
        # выбираем самый последний существующий элемент массива (крайний правый на нижнем уровне)
        i: int = 1
        while self.HeapArray[len(self.HeapArray) - i] is None:
            i += 1
            if i > len(self.HeapArray):
                return -1
        ind: int = len(self.HeapArray) - i

        # перемещаем его в корень
        self.HeapArray[0] = self.HeapArray[ind]

        # начинаем сдвигать элемент вниз по дереву
        count: int = 0
        self._GetMax(ind, count)
        self.HeapArray[ind] = None
        return el_root

    def _add(self, index: int, key: int, count: int) -> None:
        if index < 0:
            return

        # исключение при котором добавляемый элемент больше корня
        if (index - 1) // 2 < 0 and index == 0:
            return

        if (
            self.HeapArray[(index - 1) // 2] is not None
            and self.HeapArray[index] is not None
            and self.HeapArray[(index - 1) // 2] > self.HeapArray[index]
        ):
            return

        if (
            self.HeapArray[(index - 1) // 2] is None
            and self.HeapArray[index] is not None
        ):
            self.HeapArray[(index - 1) // 2] = self.HeapArray[index]
            self.HeapArray[index] = None

        if (
            self.HeapArray[(index - 1) // 2] is not None
            and self.HeapArray[(index - 1) // 2] < key
        ):
            self.HeapArray[index], self.HeapArray[(index - 1) // 2] = (
                self.HeapArray[(index - 1) // 2],
                self.HeapArray[index],
            )
        count -= 1
        return self._add(((index - 1) // 2), key, count)

    def Add(self, key: int) -> bool:
        # если массив пустой
        if self.HeapArray[0] is None:
            self.HeapArray[0] = key
            return True
        # если куча вся заполнена
        if all(element is not None for element in self.HeapArray):
            return False
        # выбираем самый последний существующий элемент массива (крайний правый на нижнем уровне)
        i: int = 1
        while self.HeapArray[len(self.HeapArray) - i] is not None:
            i += 1
            if i > len(self.HeapArray):
                return False
        ind: int = len(self.HeapArray) - i
        count: int = int(math.log2(len(self.HeapArray)) + 1)
        self.HeapArray[ind] = key
        self._add(ind, key, count)
