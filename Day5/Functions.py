#Default argument:if actual parameter is not passed in function call , then in function defination pass Actual value
def myFun(x,y=50):
    print("x:",x)
    print("y:",y)
myFun(10)

#Keyword arguments
def student(firstname,lastname):
    print(firstname,lastname)

student(firstname='John',lastname='Snow')
student(lastname='snow',firstname='John')

#using args-non keyworded Variable length arguments

def myfun1(*argv):
    print(argv)

#Driver code

myfun1('Hello','welcome','to','India')

#using kwargs-keyworded variable length argument

def printKwargs(**kwargs):
    print(kwargs)

#driver code
printKwargs(a='Hello',b='World')

#Anonymous function 
def cube(x):
    return x*x*x

cube_v2=lambda x: x*x*x
print(cube(7))
print(cube_v2(7))