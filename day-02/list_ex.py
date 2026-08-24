a = [100,200,300,400, True, 4.6]
print(type(a))
a.append(500)
print(a)

clouds = list() #list
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("ibm")
clouds.append("oracle")

print(clouds)

print("length of list is : ",len(clouds))
print("cloud service provider is : ",clouds[0])

print("cloud service provider is : ",clouds[-1])   #last
print("cloud service provider is : ",clouds[-2])     #second last



print(dir(clouds))  #list of all methods in list
print(clouds.count.__doc__)  #Return number of occurrences of value.
print(clouds.reverse.__doc__) #Reverse *IN PLACE*
print(clouds.append.__doc__)  #Append object to the end of the list.
print(clouds.extend.__doc__)  #Extend list by appending elements from the iterable.




print("````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")


for i in clouds:
    print(i)
    
    
    
 # iterate a list                           v.important

for cloud in clouds:
    if cloud == "aws":
        print("Market Leader + covered cloud")
    elif cloud == "ibm":
        print("ibm cloud")
    elif cloud == "azure" or cloud =="gcp":
        print("DevOps Multi cloud")
    else:
        print("we'll covered all multi cloud")
        
        
        #DICTIONARY