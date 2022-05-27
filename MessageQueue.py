Arr = [ (3,"you"), (2,"are"), (4,"?"), (1,"how")]
class MessageQueue:
    def __init__(self):
        self.__que=dict()
        self.__current=1

    def __check_and_print(self):
        while(self.__current in self.__que):
            print(self.__que[self.__current])
            self.__current+=1

    def add_to_que(self,data):
        i,mess=data
        self.__que[i]=mess
        self.__check_and_print()
    
        

mess1=MessageQueue()   
print(mess1.__dict__ )

for i in Arr:
    mess1.add_to_que(i)
print(mess1.__dict__ )
