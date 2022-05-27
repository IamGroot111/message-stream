Arr = [ (3,"you"), (2,"are"), (4,"?"), (1,"how")]
class messque:
    def __init__(self,):
        self.que=dict()
       
    def addtoque(self,x):
        for i,mess in x:
            self.que[i]=mess

    def printque(self):
        c=1
        while c:
            if(self.que.get(c,"rip")!="rip"):
                print(self.que.get(c,"rip"))
                c+=1
            else:
                break

mess1=messque()           
