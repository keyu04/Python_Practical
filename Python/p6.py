#6 Write a program which will allow user to enter 10 numbers and display largest odd number from them. It will display appropriate message in case if no odd number is found.
print("Enter 10 Numbers : ")
modd=0
n=0
while n<10:
    i=int(input("Enter no "))
    if i%2!=0:
        if i > modd:
            modd = i
    n=n+1
print("Larger odd Numbers is",modd)

