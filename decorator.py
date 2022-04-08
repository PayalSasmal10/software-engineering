
def decor(func):
    def inner(a,b):
        if a < b:
            a,b = b, a
        return func(a,b)
    return inner
@decor
def add1(a,b):
    return a/b

at = add1(10,20)
print(at)
