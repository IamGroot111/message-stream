Arr = [ (3,"you"), (2,"are"), (4,"?"), (1,"how")]
class messque:
    def __init__(self):
        self.que=dict()
       
    def addtoque(self,x):
        self.que[x[0]]=x[1]

    def printque(self):
        c=1
        while c:
            if(self.que.get(c,"rip")!="rip"):
                print(self.que.get(c,"rip"))
                c+=1
            else:
                break

mess1=messque()    

for i in Arr:
    mess1.addtoque(i)

mess1.printque()
