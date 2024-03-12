# Function Overloading
from multipledispatch import dispatch

@dispatch(int,int)
def mult(a, b):
    print(a * b)
    
@dispatch(int,int,int)    
def mult(a, b, c):
    print(a * b * c)
    
    
mult(2, 3, 5)
mult(2, 3)


# Passing Variable-length arguments
# 1. *args
def sum(*args):
    sm = 0
    for i in args:
        sm += i
    print(sm)

sum(2,3,4,5)

# 2. **kwargs
def fun(**kwargs):
    for key,value in  kwargs.items():
        print(key,value)
    
    
fun(name = "saif", roll = 101)
fun(name = "saif", roll = 101)



# Default Parameters
def greet(person, wish="Happy Birthday"):
    """This function prints the provided message in wish. If        
    wish is empty, it defaults to "Happy Birthday" """
    print("Hello", person + ', ' + wish)
    
greet("Rita")
greet("Hardik", "Happy New Year")