# 8 авг 2020, 13:10:19 - ID 33748541
# Реализация класса Стэк
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[- 1]

    def size(self):
        return len(self.items)


class Calculator:
    def __init__(self):
        self.numberStack = Stack()

    # Возвращает результат операции или ошибку
    # opertation: - знак операции *, +, -, /
    # firstNumber, secondNumber - числа к которым применяется операция
    def doOperation(self, operation, firstNumber, secondNumber):
        if operation == "+": return firstNumber + secondNumber
        elif operation == "-": return firstNumber - secondNumber
        elif operation == "*": return firstNumber * secondNumber
        elif operation == "/" and secondNumber != 0: return firstNumber // secondNumber
        else:
            return "error in operation"

    # Проверка на то является ли строка числом
    # string - строка, которую надо проверить
    def is_digit(self, string):
        if string.isdigit():
            return True
        else:
            try:
                float(string)
                return True
            except ValueError:
                return False
    # Функция калькулятор, вычисляет значение из входного массива
    #inputArray - входной массив
    def calculate(self, inputArray):
        for i in inputArray:
            if self.is_digit(i):
                self.numberStack.push(int(i))
            elif self.numberStack.size() > 1:
                firstDigit = int(self.numberStack.pop())
                secondDigit = int(self.numberStack.pop())
                self.numberStack.push(self.doOperation(i, secondDigit, firstDigit))
            else:
                return "error in stack"
        return self.numberStack.peek()


inputArray = input().split()
calculator = Calculator()
print(calculator.calculate(inputArray))
