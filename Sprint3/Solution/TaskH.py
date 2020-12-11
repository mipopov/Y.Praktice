def coordinates_dict(n):
    coord_dict = {}
    for i in range(n):
        input_arr = input().split()
        first_value = int(input_arr[0])
        second_value = int(input_arr[1])
        if first_value < 0 or first_value > second_value:
            return
        elif coord_dict.get(first_value):
            old_value = coord_dict.get(first_value)
            if old_value < second_value:
                coord_dict.update({first_value: second_value})
        else:
            coord_dict.update({first_value: second_value})

    coord_arr = []
    for (key, value) in coord_dict.items():
        coord_arr.append((key, value))
    return coord_arr


def get_answer(coordinates, n):
    x_first, y_max = coordinates[0][0], coordinates[0][1]
    i = 1
    res_arr = []
    while i < n:
        if coordinates[i][0] <= y_max:
            if y_max < coordinates[i][1]:
                y_max = coordinates[i][1]
        else:
            res_arr.append((x_first, y_max))
            x_first = coordinates[i][0]
            y_max = coordinates[i][1]
        i += 1
    res_arr.append((x_first, y_max))
    return res_arr


if __name__ == "__main__":
    n = int(input())
    if 0 < n <= 1000:
        coordinates = coordinates_dict(n)
        coordinates.sort(key=lambda f: f[1])
        coordinates.sort(key=lambda f: f[0])
        for (st, end) in get_answer(coordinates, len(coordinates)):
            print(st, end)
