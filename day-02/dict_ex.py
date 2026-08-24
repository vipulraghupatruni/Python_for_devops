info ={
    "name" : "Vipul", #str
    "city" : "Delhi", #str
    "Intrest" : ["Playing online games", "movies", 10], #str
    "fav no" : "15", #int
    "cost" : "36.5", #float
    "car"  : "True", #bool
}

print("I live in ",info["city"])
print("I love ",info.get("Intrest"))

info.update({"channel": "Tech Channel"})                     # update server details concept in devops
print(info)
print(dir(info))  #list of all methods in dict
print(info.get.__doc__)  #docstring of get method (Return the value for key if key is in the dictionary, else default)

# iterate a dictionary          v important

for key,value in info.items():  # items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
    print(key,":",value)  # prints keys and values
    
    
    