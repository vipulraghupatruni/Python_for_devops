num = int(input("enter the number you want the table for "))

# string formatting "f"
name = input("enter your name ")
print(f"Hello {name} welcome to the table generator")


for i in range(1,11):
    print(f" {num} * {i} = {num*i}")