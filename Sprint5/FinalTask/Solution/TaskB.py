# 14 окт 2020, 22:08:15 - ID - 36406401
MAX_TABLE_SIZE = 997
METHOD_PUT = "put"
METHOD_GET = "get"
METHOD_DEL = "delete"


class Node:
    def __init__(self, key, value, next_item=None):
        self.key = key
        self.value = value
        self.next_item = next_item


class Link_List:
    def __init__(self):
        self.head = None

    def put(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.key == key:
                    current_node.value = value
                    return
                current_node = current_node.next_item
            new_node = Node(key, value)
            new_node.next_item = self.head
            self.head = new_node

    def get(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next_item
        return -1

    def remove(self, key):
        if self.head is None:
            return "error"

        head_node = self.head
        if head_node.key == key:
            self.head = head_node.next_item
            return "ok"

        prev_node = None
        while head_node is not None:
            if head_node.key == key:
                break
            prev_node = head_node
            head_node = head_node.next_item
        if head_node is None:
            return "error"
        prev_node.next_item = head_node.next_item
        return "ok"

class Hash_Table_Chain:
    def __init__(self):
        self.table = [Link_List() for _ in range(MAX_TABLE_SIZE)]

    def hash_func(self, elem):
        return elem % MAX_TABLE_SIZE

    def input(self, key, value):
        new_index = self.hash_func(key)
        return self.table[new_index].put(key, value)

    def get(self, key):
        index = self.hash_func(key)
        return self.table[index].get(key)

    def delete(self, key):
        index = self.hash_func(key)
        return self.table[index].remove(key)


if __name__ == "__main__":
    new_hash_table = Hash_Table_Chain()
    n = int(input())
    while n > 0:
        input_arr = input().split()
        if input_arr[0] == METHOD_GET:
            print(new_hash_table.get(int(input_arr[1])))
        elif input_arr[0] == METHOD_DEL:
            print(new_hash_table.delete(int(input_arr[1])))
        elif input_arr[0] == METHOD_PUT:
            new_hash_table.input(int(input_arr[1]), input_arr[2])
        n -= 1

# Ууух, что-то тяжело идут задаче в финалах, там с 50 попытки и тут,