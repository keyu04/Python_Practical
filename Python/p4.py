a=int(input("Enter Value 1: "))
b=int(input("Enter value 2: "))
print("")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.division")
print(" ")
n=int(input("Enter Your Choice : "))
if n==1:
    print("addition is ",a+b)
elif n==2:
    print("substraction is ",a-b)
elif n==3:
    print("Multiplication is ",a*b)
elif n==4:
    print("Division is ",a/b)
else:
    print("invalid Choice..!")
