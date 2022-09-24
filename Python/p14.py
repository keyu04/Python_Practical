#14 Write a program in python to implement Salary printing file read operation. (File 
#format:
#Employee No, name, deptno, basic, DA, HRA, Conveyance) should perform below operations.
#a) Print Salary Slip for given Employee Number
#b) Print Employee List for Given Department Number
import pickle
list=[]
with open('F:\\Mca-Sem-2\\Python\\Files\\employee.txt','ab') as f:
    #f.write("EmployeeNo name  deptno  basic  DA  HRA  Conveyance")
    no=input("Enter EmployeeNo ")
    name=input("Enter Name ")
    deptno=input("Enter deptno ")
    basic=input("Enter basic ")
    da=input("Enter da ")
    hra=input("Enter hra ")
    Con=input("Enter Conveyance ")
    list.append(["\n"+no+"\t",name+"\t",deptno+"\t",basic+"\t",da+"\t",hra+"\t",Con+"\t"])
    pickle.dump(list,f)
    f.close()
