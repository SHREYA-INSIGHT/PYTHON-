## declaring and assigning vriable 
age = 32
name ="karan"
height=4.2
is_student=True

## printing the variables 
print("age:",age)
print("name:", name)
print("height:",height)

## Naming convention
##variable name should be descriptive 
##they must always start with a letter or an '_' and contains letters , numbers and underscore.
##variable names case sensitive 

## valid variable name 
First_name= "shreya"
last_name="sharma"

## invalid variable name 
##@name="shreya"(you can't use @ )
##first-name="shreya"(you can't use -)
##90age=20(name can't start with a number )

## understanding variable types 
age=20#int
height=6.2#float
name="shreyaa"#str
is_student=True#bool

print(type(age))
print(type(height))
print(type(name))

## type checking and conversion 
age=25
print(type(age))
#type conversion 
age_str=str(age)
print(age_str)
print(type(age_str))

## dynamic typig 
## python allows the type of variable to change as the program executes 
var = 10  # int
print(var, type(var))

var = "Hello"
print(var, type(var))

var = 3.14
print(var, type(var))


