import matplotlib.pyplot as p
labels = 'MCA', 'MBA', 'BSC', 'B.Com'
sizes = [30, 25, 45, 20]
fig1,a = p.subplots()
a.pie(sizes, labels=labels)
a.axis('equal')  
p.show()
