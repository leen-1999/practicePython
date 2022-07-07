# 01
def calculate(n1, n2, op="Unknown"):
    op = op.lower().strip()
    if op == "add" or op == "a" or op == "unknown":
        return n1 + n2
    elif op == "subtract" or op == "s":
        return n1 - n2
    elif op == "multiply" or op == "m":
        return n1 * n2
    else:
        print("WRONG OPERATION!!!")


print(calculate(10, 20))  # 30
print(calculate(10, 20, "AdD"))  # 30
print(calculate(10, 20, "a"))  # 30
print(calculate(10, 20, "A"))  # 30


print(calculate(10, 20, "S"))  # -10
print(calculate(10, 20, "subTRACT"))  # -10

print(calculate(10, 20, "Multiply"))  # 200
print(calculate(10, 20, "m"))  # 200


# 02

def addition(*param):
    total = 0
    for num in param:
        if num == 10:
            continue
        total += num
        if num == 5:
            total -= num
    return total


print(addition(10, 20, 30, 10, 15, 5, 100))  # 165
print(addition(10, 20, 30, 10, 15))  # 65


# 03

def show_skills(name, *skills):
    if not skills:
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Are: ")
        for skill in skills:
            print(f"- {skill}")


show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

# 04


def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your age is {age} and you live in {country}"


print(say_hello("Osama", 38, "Egypt"))
print(say_hello())
