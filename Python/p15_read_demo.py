import pickle
f = open("F:\\Mca-Sem-2\\Python\\Files\\Railway_Reservation_System.txt","rb+")
r = pickle.load(f)
for i in r:
    if i[4]=='2022-05-02':
        print(i)
