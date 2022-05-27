Arr = [ (3,"you"), (2,"are"), (4,"?"), (1,"how")]
class messque:
    def __init__(self):
        self.que=dict()
        self.current=1

    def __check_and_print(self):
        while(self.current in self.que):
            print(self.que[self.current])
            self.current+=1

    def add_to_que(self,data):
        self.que[data[0]]=data[1]
        self.__check_and_print()
    
        

mess1=messque()    

for i in Arr:
    mess1.add_to_que(i)
