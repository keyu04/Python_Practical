def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

while("true"):
    print(" ")
    a=int(input("Enter Value 1: "))
    b=int(input("Enter value 2: "))
    print("-------------------------")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.division")
    print("-------------------------")
    n=int(input("Enter Your Choice : "))
    if n==1:
        print("addition is ",add(a,b))
    elif n==2:
        print("substraction is ",sub(a,b))
    elif n==3:
        print("Multiplication is ",mul(a,b))
    elif n==4:
        print("Division is ",div(a,b))
    else:
        print("invalid Choice..!")
    print(" ")
    y=input("You want to leave..? press( y or Y ) Otherwise give Enter... ")
    if y=='y' or y=='Y':
        break
    else:
        continue
