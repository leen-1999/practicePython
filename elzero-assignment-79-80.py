from datetime import datetime


# 01
# from datetime import datetime
# using .date() we remode the time from datetime objcet
# https://theprogrammingexpert.com/python-remove-time-from-datetime/
# another way is to use strftime()
start = datetime(2021, 6, 25).date()
end = datetime.now().date()
print(f"Days From {start} To {end} Is => {(end-start).days}")

print("#" * 30)
# 02

print(datetime.now().date())  # "2021-08-10"
print(datetime.now().strftime("%Y %B %d"))  # 2022 July 04
print(datetime.now().strftime("%b %d, %Y"))  # Jul 04, 2022
print(datetime.now().strftime("%d - %b - %Y"))  # 04 - Jul - 2022
print(datetime.now().strftime("%d / %b / %Y"))  # 04 / Jul / 2022
print(datetime.now().strftime("%a, %d %b %Y"))  # Mon, 04 Jul 2022
