import matplotlib.pyplot as p
 
x = [1,9,3,5,7,3,7,6,4,8,9]

p.hist(x, bins=10)
p.title("Example of Histogram")
p.xlabel("X")
p.ylabel("Y")
p.show()
