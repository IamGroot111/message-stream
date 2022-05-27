Arr = [ (3,"you"), (2,"are"), (4,"?"), (1,"how")]
class messque:
    def __init__(self):
        self.que=dict()
        self.current=1

    def __printque(self):
        while(self.que.get(self.current,"rip")!="rip"):
            print(self.que.get(self.current,"rip"))
            self.current+=1

    def addtoque(self,data):
        self.que[data[0]]=data[1]
        self.__printque()
    
        

mess1=messque()    

for i in Arr:
    mess1.addtoque(i)
