def solution(pasport_name, db_name, n, m):
    if abs(n - m) > 1:
        return "FAIL"
    elif n == m:
        k = 0
        for i in range(n):
            if pasport_name[i] != db_name[i]:
                k += 1
                if k > 1:
                    return "FAIL"
        return "OK"
    else:
        i = 0
        while i < min(n, m):
            if pasport_name[i] != db_name[i]:
                break
            i += 1

        if n > m:
            if pasport_name[i + 1:] == db_name[i:]:
                return "OK"
            return "FAIL"
        else:
            if pasport_name[i:] == db_name[i + 1:]:
                return "OK"
            return "FAIL"


if __name__ == "__main__":
    pasport_name = input()
    db_name = input()
    print(solution(pasport_name, db_name, len(pasport_name), len(db_name)))
