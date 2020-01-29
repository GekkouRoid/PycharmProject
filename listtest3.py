stu1 = ['101', 'man', 'John', 20]


def comp(x):
    if type(x) != str:
        return '0'
    else:
        return x

stu1.sort(key=comp)
print(stu1)


def bracket(data):
    return data


a = bracket
print(a)
b = bracket(6)
print(b)
