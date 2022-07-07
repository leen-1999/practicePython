import string
# 01


myName = "Ammy"
myAge = "30"
myCountry = 'UK'

print(f"Hello \'{myName}\', How You Doing \\\"\"\" Your Age Is \"{myAge}\"")

# 02
print(f"Hello \'{myName}\', How You Doing\\\n\"\"\" Your Age Is \"{myAge}\"\" +\nAnd Your Country Is: {myCountry}")


# 03
name = 'Elzero'
print(
    f"Second Letter Is \"{name[1]}\"\nThird Letter Is \"{name[2]}\"\nLast Letter Is \"{name[-1]}\"")
# 04
print(
    f" \"{name[1:4]}\"\n\"{name[0::2]}\"\n\"{name[-2::-2]}\"")
# 05
name = "#@#@Elzero#@#@"
print(name.strip("#@"))
# 06
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

# 07
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# 08
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

# 09
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))

# 10
name = "Elzero"
print(name.index('z'))

# 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))

# 12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))

# 13
myName = "Ammy"
myAge = 30
myCountry = 'UK'

print(
    f"My name Is {myName}, And My Age Is {myAge}, And My Country Is {myCountry}")
