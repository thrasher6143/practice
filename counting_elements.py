import random


def list_count(c_list):
    counted_dict = {}
    for i in c_list:
        if i in counted_dict:
            counted_dict[i] += 1
        else:
            counted_dict[i] = 1
    return counted_dict


def create_list(n):
    created_list = []
    i = 0
    print(n)
    while i < n:
        created_list.append(random.randint(1, 10))
        i += 1
    return created_list


def odd_ball(c_dict):
    first_odd = {}
    for k, v in c_dict.items():
        if v % 2 == 0:
            pass
        else:
            first_odd[k] = v
            break
    return first_odd


def rand_str(s, f, n):
    r_str = ''
    dict_key = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j'}
    d = [random.randint(s, f) for i in range(n)]
    print(d)
    for x in d:
        r_str += ''.join(dict_key[x])
        print(r_str)
    return r_str


# print(odd_ball(list_count(create_list(15))))
# print(odd_ball(list_count(create_list(25))))
# print(odd_ball(list_count(create_list(100))))
# print(odd_ball(list_count(create_list(365))))
# print(odd_ball(list_count(create_list(random.randint(37, 721)))))
# 
# 
# print(list_count(create_list(15)))
# print(list_count(create_list(25)))
# print(list_count(create_list(100)))
# print(list_count(create_list(365)))
# print(list_count(create_list(1500)))
# print(list_count(create_list(random.randint(1, 1000))))
