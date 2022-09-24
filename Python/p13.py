#13 Write a program in Python to implement readline, readlines, write line and writelines file handling mechanisms.
while("True"):
    f=open('F:\Mca-Sem-2\Python\Files\data.txt','r+')    
    print("select any one opration from below list")
    print("1.readline")
    print("2.readlines")
    print("3.writeline")
    print("4.writelines")
    print("5.Exit")
    choice = input("Enter choice between 1 to 4:")
    if choice == '1':
        print("reading file content using readline..")
        ln = f.readline()
        while ln != "":
            ln = f.readline()
            print(ln)
        
    elif choice == '2':
        print("reading file content using readlines..")
        print(f.readlines())
        
    elif choice == '3':
        f.write("file opration \n in programming in python")
        
    elif choice == '4':
        print("writting line using writelines..")
        f.writelines(["programming in ", "python"," \nhello"," python"])
    elif choice == '5':
        break;
        
f.close()
