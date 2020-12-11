def solution(string):
        my_dict = {}
        for elem in string:
            if my_dict.get(elem):
                old_value = my_dict[elem]
                my_dict.update({elem: old_value + 1})
            else:
                my_dict[elem] = 1

        for (key, value) in my_dict.items():
            if value == 1:
                print("YES")
                return key
        return "NO"





if __name__ == "__main__":
    input_str = input()
    print(solution(input_str))