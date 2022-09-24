#7 Write a Python program to check if the number provided by the user is an Armstrong number.15/2/22
n=int(input("Enter Number: "))
temp=n
s=0
while n>0:
    d=n%10;
    s=s+d*d*d
    n=n//10
if temp==s:
    print("Armstrong")
else:
    print("Not Armstrong")
