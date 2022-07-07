# 01
print(100 < 300)
print(bool(True))
print(bool(3))
print(3 == 3)
print(334 > 500)
print(4 != 4)
print(bool(False))
print(bool(None))
print("#"*60)
# 02
html = 80
css = 60
javascript = 70
print(html > 50 and css > 50 and javascript > 50)
print("#"*60)
# 03
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)  # or = |
print(num > num_one & num > num_two)
print("#"*60)
# 04
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
print(result**3)
print((result**3) % 26000)
print(((result**3) % 26000)/5)
print(type(((result**3) % 26000)/5))
print(type(str(((result**3) % 26000)/5)))
