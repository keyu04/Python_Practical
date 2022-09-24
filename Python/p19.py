#19 Write a program to process CSV file using CSV module.
import csv as c
n=0
while(n!=3):
    print("")
    print("1.Display Data To csv File..")
    print("2.Write Data To csv file..")
    print("3.Exit")
    print("")    
    n=int(input("Enter Choice: "))
    if n==1:
        with open('myfile_csv.csv','r') as f:
            r=c.reader(f)
            for i in r:
                print(i)
        f.close()
    elif n==2:
        
        role=input("Enter RollNo ")
        name=input("Enter Name ")
        list=[role,name]
        with open('myfile_csv.csv','a') as f:
            w=c.writer(f)
            w.writerow(list)
        f.close()

        
            
