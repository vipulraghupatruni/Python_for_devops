# Get the Enviornment from User and Print it
env = input("enter the enviornment ") #taking input from user (keyboard)

print("the user input env is: ",env)

# conditional statement
if env == "prod":
    print("Don't deploy on friday")
elif env == "stg":
    print("take backup & test well")
elif env == "test":
    print("Test is well")
else:
    print("safe to deploy on anyday")



# Type casting - converting one data type to another data type
a = int(input("enter the num1 "))
b = int(input("enter the num2 "))
print(type(a))

print("multiplication is: " ,a*b)
print("additition is: " ,a+b)
print("substraction is: " ,a-b)
print("division is:" ,a/b)