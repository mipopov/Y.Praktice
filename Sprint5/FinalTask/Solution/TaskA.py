# 7 окт 2020, 22:01:00 - ID - 35480016
CONST_BASE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CONST_LEN = 62
CONST_METHOD_GET = "get"
CONST_METHOD_POST = "post"

def decode(srting):
    decoded_string = 0

    for char in srting:
        position = CONST_BASE.find(char)
        decoded_string = CONST_LEN * decoded_string + position

    return decoded_string

def encode(number):
    r = number % CONST_LEN
    encoded_string = CONST_BASE[r]
    q = number // CONST_LEN
    while q > 0:
        r = q % CONST_LEN
        encoded_string = CONST_BASE[int(r)] + encoded_string
        q = q // CONST_LEN
    return encoded_string

def get_sort_url(url, current_hash_size):
    short_domen = encode(current_hash_size)
    return "{0}{1}{2}".format(url[:url.rindex("/") + 1], short_domen, url[url.rindex("."):])


if __name__ == "__main__":
    hash_dict = {}
    n = int(input())
    while n > 0:
        input_arr = input().split()
        method = input_arr[0]
        if method == CONST_METHOD_GET:
            short_url = input_arr[1]
            if hash_dict.get(short_url):
                print(hash_dict[short_url])
            else:
                print("error")
        elif method == CONST_METHOD_POST:
            url = input_arr[1]
            content = " ".join(input_arr[2:])
            new_url = get_sort_url(url, len(hash_dict))
            hash_dict[new_url] = content
            print(new_url)
        else:
            print("error in input")
        n -= 1
