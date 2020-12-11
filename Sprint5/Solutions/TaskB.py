def get_count_primes(num):
    pr = []
    lp = [0]*(num + 1)
    for i in range(2, num):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        j = 0
        while j < len(pr) and pr[j] <= lp[i] and i * pr[j] <= num:
            lp[i * pr[j]] = pr[j]
            j += 1
    return len(pr)

if __name__ == "__main__":
    n = int(input())
    print(get_count_primes(n))







