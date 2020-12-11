# 15 сен 2020, 18:00:40 - ID - 34479844
MAX_PRIORITY_NAME = set("kondratiy")

class Binary_Max_Heap:
    def __init__(self):
        self.size = 0
        self.heap = [(0, "", 0, "")]

    # вствка элемента
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.heapify_after_insert(self.size)

    # Восстанавливаем свойства кучи после добавления
    def heapify_after_insert(self, index):
        while index // 2 > 0:
            if self.compare_index(index, index // 2):
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index //= 2

    # Удалаяем приоритетный элемент с вершины кучи
    def del_max(self):
        return_elem = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.heapify_after_delete(1)
        return return_elem

    # Сравнение индексов
    def compare_index(self, this_index, other_index):
        # сравниваем сумму очков
        if self.heap[this_index][0] > self.heap[other_index][0]:
            return True

        # если суммы равны, то лексикографическое сравнение имен
        elif self.heap[this_index][0] == self.heap[other_index][0] and self.heap[this_index][1] < self.heap[other_index][1]:
            return True

        # если суммы и имена равны, то сравниваем по приоритету вхождения
        elif self.heap[this_index][0] == self.heap[other_index][0] and self.heap[this_index][1] == self.heap[other_index][1] \
                and self.heap[this_index][2] > self.heap[other_index][2]:
            return True

    # Ищем индекс наибольшего из детей
    def get_max_child_index(self, index):
        if 2 * index + 1 > self.size:
            return 2 * index
        else:
            if self.compare_index(2 * index, 2 * index + 1):
                return 2 * index
            else:
                return 2 * index + 1

    # Восстанавливаем свойства кучи после удаленя приоритетного элемента (проталкиваем элемент вниз)
    def heapify_after_delete(self, index):
        while 2 * index <= self.size:
            max_child = self.get_max_child_index(index)
            if self.compare_index(max_child, index):
                self.heap[index], self.heap[max_child] = self.heap[max_child], self.heap[index]
            index = max_child

    # Пирамидальная сортировка массива
    def sort(self):
        help_arr = []
        while self.size > 0:
            help_arr.append(self.del_max())
        return help_arr


if __name__ == "__main__":
    n = int(input())
    econom_heap = Binary_Max_Heap()
    elite_arr = []
    econom_priority = set()

    k = 0
    while k < n:
        string_for_heap = input()
        input_str = string_for_heap.split()
        name = input_str[0]
        if MAX_PRIORITY_NAME.intersection(set(name)) == MAX_PRIORITY_NAME:
            elite_arr.append(string_for_heap)
        else:
            score_result = 0
            for i in range(1, len(input_str)):
                if int(input_str[i]) > 0:
                    score_result += int(input_str[i])
            if name + str(score_result) in econom_priority:
                econom_heap.insert((score_result, name, k + 1, string_for_heap))
            else:
                econom_priority.add(name + str(score_result))
                econom_heap.insert((score_result, name, 1, string_for_heap))
        k += 1

    elite_arr.reverse()
    for elem in econom_heap.sort():
        elite_arr.append(elem[3])

    for elem in elite_arr:
        print(elem)

# Точно, повторение одного и того же кода, теперь смотрится хорошо! Спасибо! Ценно!