#18 Write a program to read CSV file and generate output using HTML table.
import pandas as p
d=p.read_csv("myfile_csv.csv")
d.to_html("record.html")
with open("record.html","r") as f:
    print(f.read())
