# 01

values = (0, 1, 2)

if any(values):  # true

    my_var = 0  # my_var now is zero

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):  # true or false or false => true

    print("Good")  # will print

else:

    print("Bad")  # won't print


# 02
v = 40
my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# 03

n = 21

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

    print("Good")

# Output => Good

# 04


def my_all(list):
    for member in list:
        if not member:
            return False
        return True


print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False


def my_min(li):
    min = 0
    for e in li:
        if e < min:
            min = e
    return min


print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100


def my_max(li):
    max = 0
    for e in li:
        if e > max:
            max = e
    return max


# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
