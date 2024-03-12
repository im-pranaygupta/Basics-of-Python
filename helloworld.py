#type function
b = 5 
print(b, "is of type", type(b)) 
b = 2.0 
print(b, "is of type", type(b)) 
b = 1+2j 
print(b, "is complex number?", isinstance(b,complex))


#id function
a = 5           #An object, "a" is created that has a unique ID/memory block which stores 5 as a variable 
b = 10          #An object, "b" is created that has a unique ID/memory block which stores 10 as a variable 
print(id(a))    #Printing the unique ID for "a"
print(id(b))    #Printing the unique ID for "b"

a=10
print(id(a))    #Printing the unique ID for "a"