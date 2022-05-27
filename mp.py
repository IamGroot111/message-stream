Arr = [ (3,"you"), (2,"are"), (4,"?"), (1,"how")]
class messque:
    def __init__(self):
        self.que=dict()
        self.k=1
       
    def addtoque(self,x):
        self.que[x[0]]=x[1]

    def printque(self):
        while(self.que.get(self.k,"rip")!="rip"):
            print(self.que.get(self.k,"rip"))
            self.k+=1
        

mess1=messque()    

for i in Arr:
    c=1
    mess1.addtoque(i)
    mess1.printque()
