import pandas as p
df=p.read_csv("myfile_csv.csv")
print("-----------------------------------------")
print("before Handling dirty data / missing data")
print("-----------------------------------------")
print(df)
print("-----------------------------------------")
print("after Handling dirty data / missing data")
print("-----------------------------------------")
df1=df.fillna({'rollno':0,'name':'Null'})
print(df1)