# 01
# Needed Output

# "Osama"
# <class 'tuple'>
myTuple = "Osama",
print(myTuple)
print(type(myTuple))
print("#"*60)
# 02
friends = ("Osama", "Ahmed", "Sayed")
f = friends[1:]
n = ("Elzero",)
print(n+f)
print(type(n+f))
print(len(n+f))
print("#"*60)
# 03
nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
nums_and_letters_one = nums+letters
print(nums_and_letters_one)
print(len(nums_and_letters_one))
print("#"*60)
# 04
my_tuple = (1, 2, 3, 4)

# Needed Output

# 1
# 2
# 4
a, b, _, c = my_tuple
print(a)
print(b)
print(c)
print("#"*60)
