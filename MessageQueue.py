Arr = [ (3,"you"), (2,"are"), (4,"?"), (1,"how")]
class MessageQueue:
    def __init__(self):
        self.__queue=dict()
        self.__current=1

    def __check_and_print(self):
        while(self.__current in self.__queue):
            print(self.__queue[self.__current])
            self.__current+=1

    def add_to_queue(self,data):
        i,mess=data
        self.__queue[i]=mess
        self.__check_and_print()
    
        

mess1=MessageQueue()   
print(mess1.__dict__ )

for i in Arr:
    mess1.add_to_queue(i)
print(mess1.__dict__ )
