#8 Write a Python program to check if the number provided by the user is a palindrome or not.15/2/22
n=int(input("Enter Numbers : "))
temp=n
rev=0
while n>0:
    d=n%10
    rev=(rev*10)+d
    n=n//10
if temp==rev:
    print("Palindrom")
else:
    print("Not Palindrom")

