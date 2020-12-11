def count_polinom_cache(s, a=93):
    i = 0
    cache = ord(s[0])
    while i < len(s) - 1:
        cache = cache * a + ord(s[i + 1])
        i += 1
    return cache


if __name__ == "__main__":
    n = int(input())
    input_str = [count_polinom_cache(sorted(elem)) for elem in input().split()]
    our_dict = {}
    for i in range(n):
        if our_dict.get(input_str[i]):
            old_value = our_dict.get(input_str[i])
            our_dict.update({input_str[i]: old_value + " " + str(i)})
        else:
            our_dict.update({input_str[i]: str(i)})

    for elem in our_dict.values():
        print(elem)
