# 8 авг 2020, 07:57:30 - ID - 33747747
# Функция, определяющая есть ли цикл в связном списке, используем два указателя

def hasCycle(head):
    if head == None:
        return False
    fastPointer = head.next
    slowPointer = head
    while fastPointer:
        if fastPointer == slowPointer:
            return True
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next
        if fastPointer == None:
            return False
        fastPointer = fastPointer.next
    return False
