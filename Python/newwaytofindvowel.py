#a) Count Number of Vowel in given string
p=input("Enter String ")
s=p.lower()
t=c=0
for i in "aeiou":
    c=s.count(i)
    t=t+c
print("Total vowel=",t)
