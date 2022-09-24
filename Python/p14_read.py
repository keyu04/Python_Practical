import pickle
f = open("F:\\Mca-Sem-2\\Python\\Files\\employee.txt","rb")
deptno=input("Enter Department Number :")
r=pickle.load(f)
f=0
print()
print("EmpNo"+"\t"+"name"+"\t"+"deptno"+"\t"+"Basic"+"\t"+"DA"+"\t"+"HRA"+"\t"+"Conveyance")
for i in r:
    if i[0]==deptno:
        print(i)
        f=1
        break
if f==0:
    print("Not")
