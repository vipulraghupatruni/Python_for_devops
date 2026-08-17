# SCRIPTING = set of instructions
# function = work

def sum_of_num(): #fn definition (work)
num1 = int(input("enter num1 : "))  # steps
num2 = int(input("enter num2 : "))  # steps

sum = num1 + num2
print(sum)



env = input("enter the enviornment ") #taking input from user (keyboard)

    print("the user input env is: ",env)
    
    if env=="prod":
        
        sum_of_num() # fn calling
        
        

def take_backup():
    print("Backup script started ...")
    take_backup()