# 01
name = input('what is your name').strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")
print("#"*60)
# 02
age = int(input("what is your age"))
if age < 16:
    print(f"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
print("#"*60)
# 03
first_n = input("what is your first name").strip().capitalize()
second_n = input("what is your second name").strip().capitalize()
print(f"Hello {first_n} {second_n[0]}.")
print("#"*60)
# 04
email = input("what is you email").strip().lower()
userName = email[:email.index("@")]
print(f"your name is {userName.capitalize()}")
ISP = email[(email.index("@"))+1:email.index(".")]
print(f"Email Service Provider Is {ISP}")
Domain = email[(email.index("."))+1:]
print(f"Top Level Domain Is {Domain}")
