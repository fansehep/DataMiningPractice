#!/usr/lib/python3

a = 0
b = 1

while b < 10:
    print(b, end = " ")
    a, b = b, a + b


def hello():
    print("hello, world")


def Max(a, b):
    if a > b:
        return a
    else:
        return b

hello()


# print(Max("123", 1))
print(Max(1, 2))
