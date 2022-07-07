# 01
from functools import reduce
from os import remove


def remove_chars(name):
    return f"{name[1:len(name)-1]}"


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list:

    print(name)

print("#" * 50)

for name in map((lambda name: f"{name[1:len(name)-1]}"), friends_map):
    print(name)

print("#" * 50)

# 02


def get_names(name):
    return name.endswith("m")


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = filter(get_names, friends_filter)
for n in names:

    print(n)

print("#" * 50)
for n in filter(lambda name: name.endswith("m"), friends_filter):
    print(n)

print("#" * 50)

# 03

nums = [2, 4, 6, 2]


def multi(n1, n2):
    return n1 * n2


result = reduce(multi, nums)
print(result)
print("#" * 50)

result = reduce(lambda n1, n2: n1 * n2, nums)
print(result)


# 04
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skillsCopy = list(skills[:])
for e in skillsCopy:
    if isinstance(e, int):
        skillsCopy.remove(e)
rList = reversed(skillsCopy)
mySkillsWithCounter = list(enumerate(rList, 50))
for counter, skill in (mySkillsWithCounter):

    print(f"{counter} - {skill}")
