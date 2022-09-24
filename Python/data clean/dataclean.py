import pandas as p
df=p.read_csv("myfile_csv.csv")
print(df)
print("")
print("Available Total Missing Data")
print(df.isnull().sum())
print("")
print("Missing Value Available: ",df.isnull().values.any())
df['rollno'].fillna(4, inplace=True)

