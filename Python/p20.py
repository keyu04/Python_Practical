#20.Write a program to process JSON and XML data.
import json as j
import xml.etree.ElementTree as x
n=0
while(n!=3):
    print("")
    print("1.Json file Read")
    print("2.Json file Read")
    print("3.Exit")
    print("")
    n=int(input("Enter Choice: "))
    if n==1:
        with open('data.json','r') as f:
            data=j.load(f)
            for i in data['tbl_student']:
                print(i)
        f.close()
    elif n==2:
        data=x.parse('data.xml')
        root=data.getroot()
        for i in root.findall('country'):
            year=i.find('year').text
            name=i.get('name')
            print(name,"->",year)
