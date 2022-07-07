# 01
# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
counter = 0
divByFive = []
for item in my_nums[::-1]:
    if item % 5 == 0:
        divByFive.append(item)

divByFive.sort(reverse=True)
for element in divByFive:
    counter += 1
    print(f"{counter} => {element}")
else:
    print("All Numbers Printed")

# 02
for num in range(1, 21):
    if num < 10:
        if num == 6 or num == 8:
            continue
        print(f"{str(num).zfill(2)}")
    elif num == 12:
        continue
    else:
        print(num)
else:
    print("All Numbers Printed")

# 03
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
total_points = 0
for keys, values in my_ranks.items():
    if values == 'A':
        print(f"My Rank in {keys} Is A And This Equal 100 Points")
        total_points += 100
    elif values == 'B':
        print(f"My Rank in {keys} Is B And This Equal 80 Points")
        total_points += 80
    else:
        print(f"My Rank in {keys} Is C And This Equal 40 Points")
        total_points += 40
else:
    print(f"Total Points Is {total_points}")

# 04

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}
total = 0
for main_keys, main_values in students.items():

    print("-"*10)
    print(f"Student Name => {main_keys}")
    for child_keys, child_values in main_values.items():
        
        if child_values == "A":
            print(f"{child_keys} => 100 Points")
            total += 100
        elif values == "B":
            print(f"{child_keys} => 80 Points")
            total += 80
        elif values == "C":
            print(f"{child_keys} => 40 Points")
            total += 40
        else:
            print(f"{child_keys} => 20 Points")
            total += 20
    else:
        print(f"Total Points For {main_keys} Is {total}")
        print("-"*10)
