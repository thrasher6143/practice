

a = [1, 2, 3]
b = [3, 4, 5]

#set_a = set(a)
#set_b = set(b)

#in_both_set = set_a & set_b
#unique_set = set_a | set_b

#print(in_both_set)
#print(unique_set)


def in_both_set(list1, list2):
    return list(set(list1) & set(list2))


def unique_set(list1, list2):
    return list(set(list1) | set(list2))


def is_it_in(x, list):
    return x in set(list)


if __name__ == '__main__':
    print(unique_set(a, b))
    print(in_both_set(a, b))
    print(is_it_in(7, a))


