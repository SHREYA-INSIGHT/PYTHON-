## arithemthic operation 
a = 2
b = 4

add_result= a+b ## addition
sub_result= a-b ## subtraction
mul_result= a*b ## multiplication
div_result= a/b ## division
floor_div_result= a//b ## floor division
modulus_result= a%b ## modulus operation

exponentiation_result= a**b### exponentiation
print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(floor_div_result)
print(modulus_result)
print(exponentiation_result)    

## comparison operators 
a = 5
b =5
a==b ## equal to
a!=b ## not equal to
a>b ## greater than
a<b ## less than
a>=b ## greater than or equal to
a<=b ## less than or equal to
## comparison operators is also used to compare two values and return a boolean value (True or False) based on the comparison.
## comparison operators is also case sensitive, meaning that 'A' and 'a' are considered different values.for example
str1="Shreya"
str2="shreya"
print(str1!=str2) ## True


## logical operators (and, or, not)

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

## simple calculator using arithmetic operators
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

##perform arithmetic operations
addition = num1 + num2  
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

##display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
