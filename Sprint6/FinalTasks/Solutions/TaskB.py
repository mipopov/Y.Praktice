# from collections import deque
#
#
# class Node:
#     def __init__(self, char):
#         # For Trie
#         self.char = char
#         self.children = {}
#         self.is_terminal = False
#
#         # For Aho-Korasik
#         self.go_to = {}
#         self.suff_link = None
#
#     def get_child(self, char):
#         return self.children.get(char)
#
#
# class Bor:
#     def __init__(self):
#         self.head = Node("")
#
#     def insert(self, new_string: str):
#         curr_node = self.head
#         for elem in new_string:
#             if curr_node.get_child(elem):
#                 curr_node = curr_node.get_child(elem)
#             else:
#                 new_node = Node(elem)
#                 curr_node.children[elem] = new_node
#                 curr_node = new_node
#         curr_node.is_terminal = True
#
#     def bfs(self):
#         dummy = Node("")
#         dummy.children = self.head.children
#         dummy.go_to = self.head.go_to
#         self.head.suff_link = dummy
#
#         deq = deque([self.head])
#         while deq:
#             vertex = deq.popleft()
#             for (char, node) in vertex.children.items():
#                 if vertex.children.get(char):
#                     vertex.go_to[char] = vertex.children[char]
#                     vertex.children[char].suff_link = vertex.suff_link.go_to[char]
#                     deq.append(node)
#                 else:
#                     vertex.go_to[char] = vertex.suff_link.go_to[char]
#
#     def check(self):
#         print(self.head.children["a"].children["b"].suff_link.char)
#
#
# new_Bor = Bor()
# new_Bor.insert("abaa")
# new_Bor.insert("cbaa")
# new_Bor.bfs()
# new_Bor.check()
# В общем я бил задачу долго и жестко, но пока без успехов, я не понимаю как сделать конечный автомат из Бора, пересмотрел видосы,
# ребята на словах объясняют легко, понятно, а как это сделать при помощи bfs не знаю, я сделал фиктивную вершину, но в ней указал не то скорее всего
# и дальше тоже странные вещи

class AhoNode:
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None


def aho_create_forest(patterns):
    root = AhoNode()

    for path in patterns:
        node = root
        for symbol in path:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append(path)
    return root


def aho_create_statemachine(patterns):
    root = aho_create_forest(patterns)
    queue = []
    for node in root.goto.values():
        queue.append(node)
        node.fail = root

    # Инициализируем остальные узлы:
    # 1. Берем очередной узел (важно, что проход в ширину)
    # 2. Находим самую длинную суффиксную ссылку для этой вершины - это и будет fail-функция
    # 3. Если таковой не нашлось - устанавливаем fail-функцию в корневой узел
    while len(queue) > 0:
        rnode = queue.pop(0)

        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out

    return root


def aho_find_all(s, root, callback):
    node = root

    for i in range(len(s)):
        while node is not None and s[i] not in node.goto:
            node = node.fail
        if node is None:
            node = root
            continue
        node = node.goto[s[i]]
        for pattern in node.out:
            callback(i - len(pattern) + 1, pattern)

def on_occurence(pos, patterns):
    print ("At pos %s found pattern: %s" % (pos, patterns))

patterns = ['doloremipsumquiadolorsitamet']
s = "dolor"
root = aho_create_statemachine(patterns)
aho_find_all(s, root, on_occurence)