if __name__ == "__main__":
    n = int(input())
    max_count = 1
    max_word = input()
    my_dict = {max_word: 1}
    i = 1
    while i < n:
        inp_str = input()
        if my_dict.get(inp_str):
            old_value = my_dict[inp_str]
            if max_count < old_value + 1:
                max_count = old_value + 1
                max_word = inp_str
            elif max_count == old_value + 1 and max_word > inp_str:
                max_word = inp_str
            my_dict.update({inp_str: old_value + 1})
        else:
            my_dict[inp_str] = 1
        i += 1

    print(max_word)