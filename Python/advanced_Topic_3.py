import pandas as p
n1=0
while n1!=8:
    print("1. Create a data frame from csv file, dictionary, List of tuples")
    print("2. Operations on Data Frame Shape, head, tail")
    print("3. Retrieving rows / columns from data frame")
    print("4. Finding maximum and minimum values")
    print("5. Displaying statistical information")
    print("6. Performing queries")
    print("7. Handling missing data")
    print("8. Exit")
    n1=int(input("Enter choices "))
    if n1==1:
        n=0
        while n!=4:
            print("1.csv file")
            print("2.dictionary")
            print("3.List of tuples")
            print("4.Exit")
            n=int(input("Enter Choice "))
            if n==1:
                df=p.read_csv("myfile_csv.csv")
                print(df)
            elif n==2:
                di={"name":["keyur","Keyu","keyu4"],"surname":"Halpati"}
                df=p.DataFrame(di)
                print(df)
            elif n==3:
                tup=[(1,"keyur",13000),(2,"xyz",12000)]
                df=p.DataFrame(tup,columns=["id","name","salary"])
                print(df)
            else:
                break
    elif n1==2:
        n=0
        while n!=4:
            tup=[(1,"keyur",13000),(2,"xyz",12000),(3,"zzz",14000),(4,"xyy",15000)]
            print("1.Data Frame Shape")
            print("2.Data Frame head")
            print("3.Data Frame tail")
            print("4.Exit")
            n=int(input("Enter Choice "))
            if n==1:
                df=p.DataFrame(tup,columns=["id","name","salary"])
                print(df)
                r,c=df.shape
                print("")
                print("rows id",r,"columns is",c)
            elif n==2:
                df=p.DataFrame(tup,columns=["id","name","salary"])
                print(df.head(2))
            elif n==3:
                df=p.DataFrame(tup,columns=["id","name","salary"])
                print(df.tail(2))
            else:
                break
        
    elif n1==3:
        tup=[(1,"keyur",13000),(2,"xyz",12000),(3,"zzz",14000),(4,"xyy",15000)]
        df=p.DataFrame(tup,columns=["id","name","salary"])
        print(df)
        r,c=df.shape
        print("")
        print("rows id",r,"columns is",c)
    elif n1==4:
         n=0
         while n!=4:
             tup=[(1,"keyur",13000),(2,"xyz",12000),(3,"zzz",14000),(4,"xyy",15000)]
             print("1.maximum values")
             print("2.minimum values")
             print("3.Exit")
             n=int(input("Enter Choice "))
             if n==1:
                 df=p.DataFrame(tup,columns=["id","name","salary"])
                 print(df.max())
             elif n==2:
                 df=p.DataFrame(tup,columns=["id","name","salary"])
                 print(df.min())
             else:
                 break
    elif n1==5:
        tup=[(1,"keyur",13000),(2,"xyz",12000),(3,"zzz",14000),(4,"xyy",15000)]
        df=p.DataFrame(tup,columns=["id","name","salary"])
        print(df.describe())
    elif n1==6:
        print("Inprogress...")
    elif n1==7:
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
    else:
        break
