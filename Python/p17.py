#17 Write a program which will implement decorators for functions and methods in 
#python.
def deco(identity):
    def inner():
        a,b=identity()
        return "my name is "+a+"\n"+"my ages is "+b
    return inner
@deco
def demo():
    n=input("Enter Name ")
    age=input("Enter age ")
    return n,age
print(demo())
