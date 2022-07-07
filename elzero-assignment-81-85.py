# 01
def reverse_string(my_string):
    for i in my_string[::-1]:
        yield i

# or


def reverse_string(my_string):
    for i in range(len(my_string)-1, -1, -1):
        yield my_string[i]


# or

def reverse_string(my_string):
    for i in reversed(my_string):
        yield i


########################
for c in reverse_string("Elzero"):
    print(c)

print("#" * 30)

# 02


def decorator(func):
    def nFunc():
        print("Sugar Added From Decorators")
        func()
        print("#"*10)
    return nFunc


@decorator
def make_tea():
    print("Tea Created")


@decorator
def make_coffe():
    print("Coffe Created")


make_tea()
make_coffe()
