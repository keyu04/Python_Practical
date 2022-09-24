import pickle
f = open("F:\\Mca-Sem-2\\Python\\Files\\employee.txt","wb")
data = []
while("true"):
    print("Append Data")
    no=input("Enter EmployeeNo ")
    name=input("Enter Name ")
    deptno=input("Enter deptno ")
    basic=input("Enter basic ")
    da=input("Enter da ")
    hra=input("Enter hra ")
    Con=input("Enter Conveyance ")
    #list1=["\n"+no+"\t",name+"\t",deptno+"\t",basic+"\t",da+"\t",hra+"\t",Con+"\t"]
    list1=[no,name,deptno,basic,da,hra,Con]
    data.append(list1)
    ch=input("Enter Y for more Entry otherwise N to exit..")
    if ch=='N' or ch=='n':
        break;
pickle.dump(data,f)
f.close()

