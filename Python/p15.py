#15 Write a program in python to implement Railway Reservation System using file 
#handling technique. System should perform below operations.
#a. Reserve a ticket for a passenger.
#b. List information all reservations done for today’s trains.
import pickle
from datetime import date
today=str(date.today())
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
