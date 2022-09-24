class demo:
    def __init__(self):
        print("Your Are Fugo")
    def __init__(self,slist):
        self.list=slist
    def display(self):
        print("id\tname\tmarks")
        for i in self.list:
            print(i)

l=[[1,"keyur",50],[1,"mayuri",50],[1,"fugi",50],[1,"yogi",50]]
p=demo()
p=demo(l)
p.display()        
