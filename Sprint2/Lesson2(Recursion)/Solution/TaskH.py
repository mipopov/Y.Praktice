f = open('input.txt')
n = int(f.read().strip()) * 2

result = [0] * n

def generate(balance, index, k, res):
    if (balance <= k - index - 2):
        res[index] = '('
        generate(balance + 1, index + 1, k, res)

    if balance > 0:
        res[index] = ')'
        generate(balance - 1, index + 1, k, res)
    if index == k:
        if balance == 0:
            for i in res:
                print(i, end= "")
            print()

generate(0, 0, n, result)