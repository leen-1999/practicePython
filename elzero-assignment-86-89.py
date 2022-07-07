# # # 01

# # from PIL import Image
# # my_list = ["E", "Z", "R", 1, 2, 3]
# # my_tuple = ("L", "E", "O")
# # my_data = []
# # final_tuple = ()
# # for data in zip(my_list, my_tuple):
# #   # Write Your Code Here
# #     final_tuple += data
# # final_string = ''.join(final_tuple).capitalize()
# # print(final_string)  # Elzero

# # # 02

# # my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# # my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# # my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# # my_data = []
# # final_string = ""
# # for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
# #   # Write Your Code Here
# #     if type(item1) == str:
# #         final_string += item1
# # final_string = final_string.capitalize()
# # print(final_string)

# # # 03

# # # Open The Image
# # myImage = Image.open(
# #     "/Users/dunyakoyuncu/Documents/GitHub/practicepython/practicePython/elzero-pillow.png")

# # # Show The Image
# # myImage.show()

# # # My Cropped Image
# # myBox = (400, 65, 800, 399)  # 399 low elde edilecek resme dahil edilir
# # myNewImage = myImage.crop(myBox).convert("L")

# # # Show The New Image
# # myNewImage.show()

# # myBox2 = (0, 400, 1200, 800)
# # myNewImage2 = myImage.crop(myBox2).convert("L").rotate(180, expand=True)
# # myNewImage2.show()


# # # 04

# # # Write Function With Help To Get The Output

# # def say_hello_to(name):
# #     '''IT Is a Function made To Say Hello  '''
# #     print(f"Hello {name}")


# # print(say_hello_to("Osama"))  # "Hello Osama"
# # print(help(say_hello_to))
# # print(say_hello_to.__doc__)
# # # Write Doc String Line For The Function Here

# 05
