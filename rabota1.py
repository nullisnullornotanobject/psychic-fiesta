def func(c):
    answ = 1
    check = False
    for i in c:
        if i.isdigit():
            check = True
        if not i.isdigit():
            if check:
                answ += 1
            check = False
    return answ


a = input("str")
b = func(a)
print(b)
