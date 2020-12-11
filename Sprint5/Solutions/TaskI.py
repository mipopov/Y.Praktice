def count_polinom_cache(a, m, s):
    cache = 0
    my_dict = {}
    for elem in s:
        if my_dict.get(elem):
            cache = (cache * a + my_dict.get(elem)) % m
        else:
            my_dict.update({elem: ord(elem)})
            cache = (cache * a + my_dict.get(elem)) % m

    return cache % m


if __name__ == "__main__":
    a = int(input())
    if a > 0:
        m = int(input())
        if m > 0:
            s = input().strip()
            print(count_polinom_cache(a, m, s))