import pandas as p
d=p.read_csv("myfile_csv.csv")
df=p.DataFrame(d)
print(df.groupby(['rollno','name']).mean())
