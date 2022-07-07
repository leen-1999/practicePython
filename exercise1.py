
def tell_year(age):
    '''
    year = 2022
    Create a program that asks the user to 
    enter their name and their age. 
    Print out a message addressed to them 
    that tells them the year that they will 
    turn 100 years old. Note: for this exercise,
    the expectation is that you explicitly write 
    out the year (and therefore be out of date
    the next year). If you want to do this in 
    a generic way, see exercise 39.

    '''
    year = 2022
    remain_years = 100-age
    target_year = year + remain_years
    # target_year2 = 2022-age +100 # gives the same result
    return target_year


name = input('Give me your name: ')
age = int(input("Give me your age: "))

print(f"{name} you will turn on 100 in {tell_year(age)} ")

print('#'*25)


def tell_year(age, current_year):
    '''
    for any year...
    Create a program that asks the user to 
    enter their name and their age. 
    Print out a message addressed to them 
    that tells them the year that they will 
    turn 100 years old. Note: for this exercise,
    the expectation is that you explicitly write 
    out the year (and therefore be out of date
    the next year). If you want to do this in 
    a generic way, see exercise 39.

    '''
    remain_years = 100-age
    target_year = current_year + remain_years
    # target_year2 = 2022-age +100 # gives the same result
    return target_year


name = input('Give me your name: ')
age = int(input("Give me your age: "))
current_year = int(input("Give me the current year: "))
print(f"{name} you will turn on 100 in {tell_year(age,current_year)} ")
