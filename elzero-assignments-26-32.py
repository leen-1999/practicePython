# 01
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = []
for element in my_list:
    if element not in unique_list:
        unique_list.append(element)
print(unique_list)
print(type(unique_list))
print(unique_list[:len(unique_list)-1])
print("#"*60)
# 02
nums = {1, 2, 3}
letters = {"A", "B", "C"}
# 1st method # doesn't mutate the nums
print(nums | letters)
# 2nd method # union doesn't mutate the nums
print(nums.union(letters))
# 3rd method # update mutates nums
nums.update(letters)
print(nums)
# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
print("#"*60)
# 03
my_set = {1, 2, 3}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
# in order to not give an error don't use remove() instead use discard()
my_set.discard("C")
print("#"*60)
# 04
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("#"*60)
# 05
my_dic = {"HTML": "90%", "CSS": "80%", "Python": "30%"}
fstS = my_dic["HTML"]
print(f"HTML Progress Is {fstS}")
sndS = my_dic["CSS"]
print(f"CSS Progress Is {sndS}")
tndS = my_dic["Python"]
print(f"Python Progress Is {tndS}")
my_dic["AI"] = "20%"
fthS = my_dic["AI"]  # or we can use my_dic.update({"AI":"20%"})
print(f"AI Progress Is {fthS}")
