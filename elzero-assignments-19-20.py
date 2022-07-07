# 01

print(f"{type(1)}\n{type(2.3)}\n{type(5+6j)}")

# 02
num = 1+2j

# Print Imaginary Part Here
# Print Real Part Here
print(f"Real Part: {num.real}")
print(f"Imaginary Part: {num.imag}")

# 03
num = 10
print("My Number is: {:.10f}".format(num))

# 04
num = 159.650

# Needed Output
# 159
# <class 'int'>
conv = int(num)
print(conv)
print(type(conv))

# 05

# 100 ? 115 = -15
# 50 ? 30 = 1500
# 21 ? 4 = 1
# 110 ? 11 = 10
# 97 ? 20 = 4

print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 // 11)
print(97 // 20)
