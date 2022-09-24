import pickle
from datetime import date
today=str(date.today())
while("true"):
    print("1. Enter Data")
    print("2. Reserve a ticket for a passenger")
    print("3. List information all reservations done for today’s trains.")
    n=input("Enter Choice: ")
    if n=='1':
        f = open("F:\\Mca-Sem-2\\Python\\Files\\Railway_Reservation_System.txt","ab+")
        data = []
        while("true"):
            print("Append Data")
            name=input("Enter Name ")
            no=input("Enter phone ")
            s1=input("Enter Source ")
            s2=input("Enter Destination ")
            ticket=input("Enter Ticket ")
            list1=[name,no,s1,s2,today,ticket]
            data.append(list1)
            ch=input("Enter Y for more Entry otherwise N to exit..")
            if ch=='N' or ch=='n':
                    break;
        pickle.dump(data,f)
        f.close()
    elif n=='2':
        book=input("Enter passenger Name for Reserve a ticket ")
        f = open("F:\\Mca-Sem-2\\Python\\Files\\Railway_Reservation_System.txt","rb+")
        r = pickle.load(f)
        flag=0
        l1=[]
        for i in r:
            if i[0]==book:
                flag=1
                i[5]="Done"
                l1.append(i)
        if flag==1:
            f.seek(0)
            pickle.dump(l1,f)
            print("Update Record..")
        else:
            print("Not Update..")
        f.close()
    elif n=='3':
        f = open("F:\\Mca-Sem-2\\Python\\Files\\Railway_Reservation_System.txt","rb+")
        r = pickle.load(f)
        for i in r:
            if i[4]=='2022-07-05':
                print(i)
    else:
        print("Invalid Choices")
    ch=input("Do u want to Continue..(y/n)")
    if ch=='N' or ch=='n':
        break;
