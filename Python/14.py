import pickle
while("true"):
    print("1.Enter Data")
    print("2.Print Salary Slip for given Employee Number")
    print("3.Print Employee List for Given Department Number")
    print("4.Print All Employee")
    ch=int(input("Enter Your Choice"))
    if ch==1:
        f = open("F:\\Mca-Sem-2\\Python\\Files\\employee.txt","ab")
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
            list1=[no,name,deptno,basic,da,hra,Con+"\n"]
            data.append(list1)
            ch=input("Enter Y for more Entry otherwise N to exit..")
            if ch=='N' or ch=='n':
                break;
        pickle.dump(data,f)
        f.close()
    elif ch==2:
        f = open("F:\\Mca-Sem-2\\Python\\Files\\employee.txt","rb")
        empno=input("Enter Employee Number :")
        r=pickle.load(f)
        f=0
        print()
        print("Basic"+"\t"+"DA"+"\t"+"HRA"+"\t"+"Conveyance")
        for i in r:
            if i[0]==empno:
                print(i[3]+"\t",i[4]+"\t",i[5]+"\t",i[6])
                f=1
                break
        if f==0:
            print("Not")

    elif ch==3:
        f = open("F:\\Mca-Sem-2\\Python\\Files\\employee.txt","rb")
        deptno=input("Enter Department Number :")
        r=pickle.load(f)
        f=0
        print()
        print("EmpNo"+"\t"+"name"+"\t"+"deptno"+"\t"+"Basic"+"\t"+"DA"+"\t"+"HRA"+"\t"+"Conveyance")
        for i in r:
            if i[2]==deptno:
                print(i)
                f=1
                break
        if f==0:
            print("Not")
    elif ch==4:
        f = open("F:\\Mca-Sem-2\\Python\\Files\\employee.txt","rb")
        r=pickle.load(f)
        print()
        print("EmpNo"+"\t"+"name"+"\t"+"deptno"+"\t"+"Basic"+"\t"+"DA"+"\t"+"HRA"+"\t"+"Conveyance")
        for i in r:
            print(i)
    else:
        print("Invalid Choices")
    ch=input("Do u Want to Continue..?(Y/n)")
    if ch=='N' or ch=='n':
        break
