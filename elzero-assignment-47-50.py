# 01
num = int(input("enter number"))
if num <= 0:
    print(f"Number {num} is not larger than zero")
else:
    counter = 0
    while num > 0:
        num -= 1
        if num == 0:
            break
        else:
            print(num)
            counter += 1
    print(f"{counter} Numbers Printed Successfully.")


# 02
maximumFriends = 5
friends = []
while maximumFriends > 0:
    take = input("add you friends")
    friends.append(take)
    maximumFriends -= 1

# 03
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    # pop(-1)= pop() get elements from last pop(0) gets elements from starrt
    print(skills.pop(0))

# 04
my_friends = []
maximum_friends = 4
while maximum_friends > 0:

    give = input("add you friends").strip()
    if give[0].isupper and give[1:].islower:
        my_friends.append(give)
        maximum_friends -= 1
        print(f"Friend {give} added ")
        print(f"Names Left in list is {maximum_friends}")
    elif give.isupper:
        print("invalid name")
    else:
        my_friends.append(give.capitalize())
        maximum_friends -= 1
        print(f"Friend {give.capitalize()} added => 1st letter become capital")
        print(f"Names Left in list is {maximum_friends}")
