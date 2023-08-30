from pymonad.tools import curry

#задание 2.3.1

@curry(2)
def string_carry(t1, t2):
    return t1 + t2

hello = string_carry("Hello, ")

print(hello("Mikhail"))

#задание 2.3.2

@curry(4)
def hello_fun(hello, zpt, vsc, name):
    return f"{hello}{zpt} {name}{vsc}"

final = hello_fun("Hello")(",")("!")
print(final("Mikhail"))