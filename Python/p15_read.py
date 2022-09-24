import pickle
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
