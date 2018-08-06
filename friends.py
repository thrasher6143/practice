

def friend(x):
    frnd = []
    for i in x:
        if len(i) == 4:
            frnd.append(i)
    return frnd


def friendagain(x):
    return [f for f in x if len(f) == 4]


print(friend(["Ryan", "Kieran", "Mark",]))
print(friendagain(["Ryan", "Kieran", "Mark",]))


