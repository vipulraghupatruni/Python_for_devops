for i in range(5):
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

