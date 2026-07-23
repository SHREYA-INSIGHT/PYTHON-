## if statement 
age=24
if age >= 18:
    print("you can vote")

    ## else statement 
## the esle statement is used to execute a block of code if the condition in the if statement is not true.
age=16
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")

    ##elif statement
## the elif statement is used to check multiple conditions. it stands for "else if"
age=20
if age < 18:
    print("you cannot vote")
elif age >= 18 and age < 21:
    print("you can vote but cannot drink")
else:
    print("you can vote and drink")

    ## nested conditional statement
### a nested conditional statement is a conditional statement that is contained within another conditional statement.
num=int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero or negative.")

    ## pratice problem
## dtermine if a year is a leap year or not. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
year=int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
