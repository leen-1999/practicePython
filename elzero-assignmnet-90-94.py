# 01

import string
alphabet_list1 = list(string.ascii_lowercase)
alphabet_list2 = list(string.ascii_uppercase)
# # NUM = input("Add Your Number ")

# # if NUM not in alphabet_list1 and NUM not in alphabet_list2:
# #     #int(NUM) == 0
# #     if len(NUM) > 1:
# #         raise IndexError("Only One Character Allowed")
# #     elif int(NUM) == 0:
# #         raise ValueError(f"Number Must Be Larger Than {NUM}")
# #     else:
# #         print("#"*10)
# #         print(f"The Number IS {NUM}")
# #         print("#"*10)
# # else:
# #     raise Exception("Only Numbers Allowed")


# 02

# # try:
# #     LETTER = input("Add Letter From A to Z")
# #     if len(LETTER) > 1:
# #         raise IndexError("You Must Write One Character Only")
# #     elif LETTER not in alphabet_list2:
# #         raise Exception("The Letter Not In A - Z")
# # except IndexError as ex1:
# #     print(ex1)
# # except Exception as ex2:
# #     print(ex2)
# # else:
# #     print(f"You Typed {LETTER}")


# 03

def calculate(num1, num2) -> int:
    return num1 + num2


print(calculate(20, 30))
