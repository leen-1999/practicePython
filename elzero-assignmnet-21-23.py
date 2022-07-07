# 01
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print(friends[0])
print(friends[0:1])
print(friends[-1])
print(friends[-1:])

# 02
friends = ["Osama", "Ahmed", "Sayed", "Ali",
           "Mahmoud", "Ammy", "Lama", "David"]
odd = []
even = []
# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"

for element in friends:
    if (len(element) % 2) == 0:
        even.append(element)
    else:
        odd.append(element)
print(odd)
print(even)
print("#"*60)
# 03
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"

print(f"\"{friends[2-1]}\",\"{friends[3-1]}\",\"{friends[4-1]}\"")
print(f"\"{friends[-2]}\",\"{friends[-1]}\"")

# 04
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends[-1] = "Elzero"
friends[-2] = "Elzero"
print(friends)

# 05
friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.insert(0, "Nasser")
friends.append("Salem")
print(friends)
# 06
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

friends = friends[2:]
print(friends)
friends.pop()
print(friends)

# 07

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)
print("#"*60)
# 08
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
friends.sort()
print(friends)
friends.sort(reverse=1)
print(friends)

print("#"*60)
# 09

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# 6
print(len(friends))
print("#"*60)

# 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
# Web
print(technologies[4][0])
print(technologies[4][-1])
