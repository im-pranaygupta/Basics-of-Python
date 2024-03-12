#Global Variable
x = "Global Variable" 
def foo(): 
    print("Value of x: ", x) 
foo()

#Accessing global inside a function
x=1
def fun():
    global x
    x=x+1   
fun()
print(x)