            ########################################################
                        #TODO make sure that each method actually does what its
#supposed to like if supposed to remove first make sure first is not in the result
            ########################################################
class Deque(object):
    def __init__(self,head_idx=None,tail_idx=None):
        self.itms = [None,None]
        self.head_idx = head_idx
        self.tail_idx = tail_idx

    def isEmpty(self):
        return self.head_idx == None

    def size(self):
        if self.head_idx == None:
            return 0
        elif self.head_idx == self.tail_idx:
            return 1
        if self.head_idx < self.tail_idx:
            return self.tail_idx - self.head_idx + 1
        return len(self.itms) - self.head_idx + self.tail_idx + 1

    def addFirst(self,itm):
        if self.head_idx == None:
            self.itms[0] = itm
            self.head_idx = 0
            self.tail_idx = 0
        elif self.head_idx == 0:
            if self.tail_idx < len(self.itms) - 1:
                self.itms[-1] = itm
                self.head_idx = len(self.itms) - 1
            else:
                #need to copy to a new array
                #and might as well make the new array have the new head
                #itm at index 0
                new_array = [None for i in range(len(self.itms)*2)]
                new_array[0] = itm
                for i in range(self.tail_idx+1):
                    new_array[i+1] = self.itms[i]
                self.tail_idx += 1
                self.itms = new_array
                self.head_idx = 0
        else:
            #self.head_idx > 0
            if self.tail_idx > self.head_idx:
                #no wraparound yet
                #no elts at beginning are empty
                #can add there
                self.itms[self.head_idx-1] = itm
                self.head_idx -= 1
            else:
                #already have wraparound
                #need to check if have room
                if self.head_idx > self.tail_idx + 1:
                    #room to add before head
                    self.itms[self.head_idx-1] = itm
                    self.head_idx -= 1
                else:
                    #need to make new array
                    #might as well put the stuff in order
                    new_array = [None for i in range(2*len(self.itms))]
                    new_array[0] = itm
                    current_idx = 1
                    for i in range(self.head_idx,len(self.itms)):
                        new_array[current_idx] = self.itms[i]
                        current_idx += 1
                    for i in range(self.tail_idx+1):
                        new_array[current_idx] = self.itms[i]
                        current_idx += 1
                    self.itms = new_array
                    self.head_idx = 0
                    self.tail_idx = current_idx - 1

    def addLast(self,itm):
        if self.head_idx == None:
            self.itms[0] = itm
            self.head_idx = 0
            self.tail_idx = 0
        elif self.head_idx == self.tail_idx and self.tail_idx < len(self.itms) - 1:
            self.itms[self.tail_idx+1] = itm
            self.tail_idx += 1
        elif self.head_idx == self.tail_idx and self.head_idx > 0:
            self.itms[0] = itm
            self.tail_idx = 0
        #elif self.head_idx == self.tail_idx
        elif self.head_idx < self.tail_idx and self.tail_idx < len(self.itms)-1:
            print("#no wraparound yet and still room at end")
            self.itms[self.tail_idx+1] = itm
            self.tail_idx += 1
        elif self.head_idx > self.tail_idx and self.tail_idx < self.head_idx - 1:
            print("#yes wraparound and still room at end")
            self.itms[self.tail_idx+1] = itm
            self.tail_idx += 1
        elif (self.head_idx == 0 and self.head_idx < self.tail_idx) and (self.tail_idx == len(self.itms) - 1):
            print("#no wraparound and no room")
            #need to make a new array
            #might as well put it in order
            new_array = [None for i in range(len(self.itms)*2)]
            current_idx = 0
            for i in range(self.tail_idx+1):
                new_array[current_idx] = self.itms[i]
                current_idx += 1
            new_array[current_idx] = itm
            self.itms = new_array
            self.head_idx = 0
            self.tail_idx = current_idx
        elif (self.head_idx > 0 and self.head_idx < self.tail_idx) and self.tail_idx == len(self.itms)-1:
            print("#no wraparound yet and room but need to wraparound to have room")
            self.itms[0] = itm
            self.tail_idx = 0
            
    def removeFirst(self):
        if self.head_idx == None:
            #no itms
            return "Deque underflow error!"
        else:
            #some itms
            if (self.head_idx != None) and (self.head_idx == self.tail_idx):
                #1 itm
                #then need to make self.head_idx None
                ret = self.itms[self.head_idx]
                self.itms[self.head_idx] = None
                self.head_idx = None
                self.tail_idx = None
            else:
                #more than one itm left
                if (self.head_idx < self.tail_idx) and (self.size()-1 > 0.25*len(self.itms)):
                #no wraparound and more than 1/4 elts full
                    ret = self.itms[self.head_idx]
                    self.itms[self.head_idx] = None
                    self.head_idx += 1
                elif (self.head_idx < self.tail_idx):
                #no wraparound and will be 1/4 elts full
                    #copy elts into smaller array
                    ret = self.itms[self.head_idx]
                    new_array = [None for i in range(int(len(self.itms)*0.5))]
                    current_idx = 0
                    for i in range(self.head_idx+1, self.tail_idx+1):
                        new_array[current_idx] = self.itms[i]
                        current_idx += 1
                    self.itms = new_array
                    self.head_idx = 0
                    self.tail_idx = current_idx - 1
                elif (self.size()-1 > 0.25*len(self.itms)):
                #wraparound and more than 1/4 elts full
                    ret = self.itms[self.head_idx]
                    self.itms[self.head_idx] = None
                    if self.head_idx < len(self.itms) - 1:
                        self.head_idx += 1
                    else:
                        self.head_idx = 0
                else:
                #wraparound and will be 1/4 elts full
                    ret = self.itms[self.
                                    head_idx]
                    #copy elts into new smaller array
                    new_array = [None for i in range(len(self.itms)*0.5)]
                    current_idx = 0
                    for i in range(self.head_idx+1,len(self.itms)):
                        new_array[current_idx] = self.itms[i]
                        current_idx += 1
                    for i in range(self.tail_idx+1):
                        new_array[current_idx] = self.itms[i]
                        current_idx += 1
                    self.itms = new_array
                    self.head_idx = 0
                    self.tail_idx = current_idx - 1
        return ret

    def removeLast(self):
        #similar to remove first
        if self.head_idx == None:
            #no itms
            return "Deque empty!"
        else:
            #some itms
            if self.head_idx == self.tail_idx:
                #1 itm
                ret = self.itms[self.tail_idx]
                self.itms[self.tail_idx] = None
            else:
                #more than 1 itm
                if self.head_idx < self.tail_idx:
                    #no wraparound
                    if (self.size()-1 > 0.25*len(self.itms)):
                    #will be more than 1/4 full
                        ret = self.itms[self.tail_idx]
                        self.itms[self.tail_idx] = None
                        self.tail_idx -= 1

                    else:
                        #will not
                        #need to copy into new smaller array
                        ret = self.itms[self.tail_idx]
                        new_array = [None for i in range(int(0.5*len(self.itms)))]
                        current_idx = 0
                        for i in range(self.head_idx,self.tail_idx):
                            new_array[current_idx] = self.itms[i]
                            current_idx += 1
                        self.itms = new_array
                        self.head_idx = 0
                        self.tail_idx = current_idx - 1

                    
                else:
                    #yes wraparound
                    if (self.size()-1 > 0.25*len(self.itms)):
                    #will be more than 1/4 full
                        ret = self.itms[self.tail_idx]
                        if self.tail_idx > 0:
                            self.itms[self.tail_idx] = None
                            self.tail_idx -= 1
                        else:
                            self.itms[self.tail_idx] = None
                            self.tail_idx = len(self.itms)

                    else:
                        #will not
                        ret = self.itms[self.tail_idx]
                        #need to copy into new smaller array
                        new_array = [None for i in range(0.5*len(self.itms))]
                        current_idx = 0
                        for i in range(self.head_idx,len(self.itms)):
                            new_array[current_idx] = self.itms[i]
                            current_idx += 1
                        if self.tail_idx > 0:
                            for i in range(self.tail_idx):
                                new_array[current_idx] = self.itms[i]
                                current_idx += 1
                        self.itms = new_array
                        self.head_idx = 0
                        self.tail_idx = current_idx - 1
        return ret
                    

    def peekFirst(self):
        if self.head_idx == None:
            return "Deque empty!"
        return self.itms[self.head_idx]

    def peekLast(self):
        if self.tail_idx == None:
            return "Deque empty!"
        return self.itms[self.tail_idx]

    def getItems(self):
        string = ""
        if self.head_idx == None:
            string += "Deque empty!"
        else:
            if self.head_idx == self.tail_idx:
                string += str(self.itms[self.head_idx])
            elif self.head_idx < self.tail_idx:
                for i in range(self.head_idx,self.tail_idx + 1):
                    string += str(self.itms[i]) + " "
            else:
                for i in range(self.head_idx,len(self.itms)):
                    string += str(self.itms[i]) + " "
                for i in range(self.tail_idx+1):
                    string += str(self.itms[i]) + " "
        print(string)
                

deque = Deque()
print("Should print true:")
print(deque.isEmpty())
print()
deque.addFirst(17)
print("should be [17,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 0")
print(deque.tail_idx)
print()
deque.addFirst(12)
print("should be [17,12]")
print(deque.itms)
print()
print("should be 17")
print(deque.peekLast())
print()
print("should be 12")
print(deque.peekFirst())
print()
print("should be 12")
print(deque.removeFirst())
print()
print("should be [17,None]")
print(deque.itms)
print()
deque.addLast(8)
print("should be [17,8]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 1")
print(deque.tail_idx)
print()
deque.addFirst(227)
print("should be [227,17,8,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 2")
print(deque.tail_idx)
print()
print("should be true")
print(deque.tail_idx < len(deque.itms) - 1)
print()
deque.addFirst(9)
print("should be [227,17,8,9]")
print(deque.itms)
print()
print("should be 3")
print(deque.head_idx)
print()
print("should be 2")
print(deque.tail_idx)
print()
deque.removeLast()
print("should be [227,17,None,9]")
print(deque.itms)
print()
print("should be 3")
print(deque.head_idx)
print()
print("should be 1")
print(deque.tail_idx)
print()
deque.addFirst(3)
print("should be [227,17,3,9]")
print(deque.itms)
print()
print("should be 2")
print(deque.head_idx)
print()
print("should be 1")
print(deque.tail_idx)
print()
deque.removeFirst()
print("should be [227,17,None,9]")
print(deque.itms)
print()
print("should be 3")
print(deque.head_idx)
print()
print("should be 1")
print(deque.tail_idx)
print()
deque.removeFirst()
print("should be [227,17,None,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 1")
print(deque.tail_idx)
print()
deque.addFirst(1)
print("should be [227,17,None,1]")
print(deque.itms)
print()
print("should be 3")
print(deque.head_idx)
print()
print("should be 1")
print(deque.tail_idx)
print()
deque.addFirst(2)
print("should be [227,17,2,1]")
print(deque.itms)
print()
print("should be 2")
print(deque.head_idx)
print()
print("should be 1")
print(deque.tail_idx)
print()
deque.addFirst(3)
print("should be [3,2,1,227,17,None,None,None,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 4")
print(deque.tail_idx)
print()
deque.addLast(18)
print("should be [3,2,1,227,17,18,None,None,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 5")
print(deque.tail_idx)
print()
deque.addLast(19)
print("should be [3,2,1,227,17,18,19,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 6")
print(deque.tail_idx)
print()
deque.addFirst(20)
print("should be [3,2,1,227,17,18,19,20]")
print(deque.itms)
print()
print("should be 7")
print(deque.head_idx)
print()
print("should be 6")
print(deque.tail_idx)
print()
deque.addFirst(21)
print("should be [21,20,3,2,1,227,17,18,19,None,None,None,None,None,None,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 8")
print(deque.tail_idx)
print()
deque.addFirst(22)
print("should be [21,20,3,2,1,227,17,18,19,None,None,None,None,None,None,22]")
print(deque.itms)
print()
print("should be 15")
print(deque.head_idx)
print()
print("should be 8")
print(deque.tail_idx)
print()
deque.removeFirst()
print("should be [21,20,3,2,1,227,17,18,19,None,None,None,None,None,None,None]")
print(deque.itms)
print()
print("should be 0")
print(deque.head_idx)
print()
print("should be 8")
print(deque.tail_idx)
print()
deque.removeLast()
print(deque.itms)
print()
deque.removeLast()
print(deque.itms)
print()
deque.removeLast()
print(deque.itms)
print()
deque.removeLast()
print(deque.itms)
print()
deque.removeLast()
print(deque.itms)
print()
deque.removeFirst()
print(deque.itms)
print()
deque.removeFirst()
print(deque.itms)
print()
deque.removeFirst()
print(deque.itms)
print()


        
