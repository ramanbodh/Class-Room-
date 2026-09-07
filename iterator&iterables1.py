#here we will learn about iterator and iterables 
#An iterable is an object that can provide an iterator.
#An iterator is an object that gives you the next item when requested.
numbers=[10,20,30,40]
it=iter(numbers)
print(it)
print(next(it))
print(next(it))
print(it)# i think it prints the current iterable object
print(next(it))
print(next(it))    

#now here how it related to for loop or what conceptually does 
print("_---------------_")
num=[1,2,3,4,5,6]
it=iter(num)
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration:#stop iteration tell there is no more values
        break

#creating the you Own iterator for counting number to n the number
print("---------------------------")
class Count:
    def __init__(self,maximum):
        self.current=1
        self.maximum=maximum
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.maximum:
            raise StopIteration
        value=self.current
        self.current+=1

        return value

counter=Count(4)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh
#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh

#skljdfksdjflskjfk ksjdfkj sdfjkj
#skjdfk sj
#skjdflksj s
# jhaskdfjh a
# ashdfjhas 
# kajsdfkasjlf
#asdfjalskfj
#sdfhksjdfh


