# exc.1.a
x: tuple[int,] = (99,)

# exc.1.b
y: tuple[int, int, int] = (77, 88, 99)


# exc.1.c
def tup_len(x: tuple[str]):
    return len(x)


print("1c:", tup_len("ido"))  # to check


# exc.1.d
def tup_add(x: tuple[str], y: tuple[str]):
    return x + y


print("1d:", tup_add("ido ", "hamrani"))  # to check


# exc.1.e
def tup_common(tup1: tuple[int, ...], tup2: tuple[int, ...]):
    res: tuple = tuple()
    for i in tup1:
        if i in tup2:
            res += (i,)
    print("1e:", res)  # to check


tup_common((1, 2, 3, 4,), (3, 4, 5, 6,))  # to check


# exc.1.f
def tup_uncommon(tup1: tuple[int, ...], tup2: tuple[int, ...]):
    res: tuple = tuple()
    for i in tup1:
        if i not in tup2:
            res += (i,)
    for i in tup2:
        if i not in tup1:
            res += (i,)
    print("1f:", res)  # to check


tup_uncommon((1, 2, 3, 4,), (3, 4, 5, 6,))


# exc.1.g
def tup_index(x: tuple[int, ...], y: int):
    return x[y] if y < len(x) else None


print("1g:", tup_index((1, 2, 3), 1))  # to check
print("1g:", tup_index((1, 2, 3), 5))  # to check


# exc.1.h
def tup_rev(tup1: tuple[str]):
    return tup1[::-1]


print("1h:", tup_rev("Ido"))  # to check


# exc.1.i
def tup_mul(mul1: int, tup1: tuple[int, ...]):
    return mul1 * tup1


print("1i:", tup_mul(3, (1, 2, 4,)))  # to check


# exc.1.j
def tup_ret_without_num(num1: int, tup1: tuple[int, ...]):
    return tuple(x for x in tup1 if x != num1)


print("1j:", tup_ret_without_num(3, (3, 5, 4, 6, 3, 4, 5,)))  # to check


# exc.1.k
def tup_without_dup(tup1: tuple[int, ...]):
    tup2 = tuple()
    for i in tup1:
        if not i in tup2:
            tup2 += (i,)
    return tup2


print("1k:", tup_without_dup((5, 6, 43, 4, 3, 5, 6,)))  # to check


# exc.1.l
def ret_tup_index(num: int, tup1: tuple[int, ...]):
    return [x for x in range(len(tup1)) if tup1[x] == num]


print("1l:", ret_tup_index(5, (5, 6, 5, 2, 4, 53, 5, 3,)))  # to check

# exc.1.m
sentinal1: str = "done"
sentinal2: int = -999
name_list: list[str] = []
grade_list: list[int] = []
while True:
    name: str = input("enter your name")
    if name == sentinal1:
        break
    else:
        name_list.append(name)
while True:
    grade: int = int(input("enter your grade"))
    if grade == sentinal2:
        break
    else:
        grade_list.append(grade)
print("1m:", tuple(zip(name_list, grade_list)))  # to check

# exc.2
# The differences between tuple and list is that lists can be changed while taple cannot be changed.
# When you have a fixed set of data that you do not want to change, we will use taple

# exc.3
data_tuple = ({"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code")
data_tuple[0]["age"] = 31
data_tuple[0].clear()
# the code above does not crash because one of the items in the tuple is a complex data cell which we can change within it the information it contains but not the type for instance you can't change the dictionary into an int
