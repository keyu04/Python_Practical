def countVowel():
    p=input("Enter String ")
    a=e=i=o=u=c=0
    for k in p:
        if k=='a':
            a=a+1
        
        if k=='e':
            e=e+1
        
        if k=='i':
            i=i+1
        
        if k=='o':
            o=o+1
        
        if k=='u':
            u=u+1
        
        if k=='a' or k=='e' or k=='i' or k=='o' or k=='u':
            c=c+1
        
    print("A =",a)
    print("E =",e)
    print("I =",i)
    print("O =",o)
    print("U =",u)
    print("total vowels =",c)

def countLength():
    i=input("Enter string ")
    s=0
    for p in i:
        s=s+1
    print("Length is ",s)

def reverseString():
    i=input("Enter string ")
    print("Reverse string ",i[::-1])

def replaceString():
    i=input("Enter string ")
    f=input("Enter Find String ")
    r=input("Enter Replace String ")
    print("Original String",i)
    print("Replaced String",i.replace(f,r))
def checkStringPaliorNot():
    i=input("Enter string ")
    if i==i[::-1]:
        print("string is a palindrome")
    else:
        print("string is not a palindrome")

while("true"):
    print("a. Count Number of Vowel in given string")
    print("b. Count Length of string")
    print("c. Reverse string ")
    print("d. Find and replace operation")
    print("e. check whether string entered is a palindrome or not")
    print("Enter choice :")
    c=input()
    cl=c.lower()

    if cl=='a':
        countVowel()
    elif cl=='b':
        countLength()
    elif cl=='c':
        reverseString()
    elif cl=='d':
        replaceString()
    elif cl=='e':
        checkStringPaliorNot()
    else:
        print("Invalid Choice")

    print("----------------------------------")
    ch=input("Do you Want To Exit press(Y or y) ")
    print("----------------------------------")
    if ch=='Y' or ch=='y':
        break




        
