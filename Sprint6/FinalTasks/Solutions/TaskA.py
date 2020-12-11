# 19 ноя 2020, 23:28:18 - ID - 42040424
class Node:
    char_a_code = 97
    chars_count = 26

    def __init__(self):
        self.index = -1
        self.children = [None for _ in range(self.chars_count)]
        self.suffix_palindrome = []

    def add_child(self, char, node):
        self.children[ord(char) - self.char_a_code] = node

    def get_child(self, char):
        return self.children[ord(char) - self.char_a_code]


class Trie:
    def __init__(self):
        self.root = Node()

    def put(self, word, index):
        node = self.root
        for i in range(len(word) - 1, -1, -1):
            if self.is_palindrome(word[:i+1]):
                node.suffix_palindrome.append(index)
            if not node.get_child(word[i]):
                node.add_child(word[i], Node())
            node = node.get_child(word[i])
        node.index = index

    def search(self, word, index):
        node = self.root
        pairs = []
        for j in range(len(word)):
            if node.index >= 0 and node.index != index and self.is_palindrome(word[j:]):
                pairs.append([index + 1, node.index + 1])
            node = node.get_child(word[j])
            if not node:
                return pairs
        for j in node.suffix_palindrome:
            if j != index:
                pairs.append([index + 1, j + 1])
        if node.index >= 0 and node.index != index:
            pairs.append([index + 1, node.index + 1])
        return pairs

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    n = int(input())
    if n >= 2:
        words = [input() for _ in range(n)]
        bor = Trie()
        for i in range(n):
            bor.put(words[i], i)

        res = []
        for i in range(n):
            res += bor.search(words[i], i)

        res.sort()
        for result in res:
            print(*result)