def greeting():
    print("hello")

print(greeting)#identity not exactly address
greeting()#execution of the function code
print(type(greeting))#type of the object greeting will be funct

hello=greeting#function object reference is passed to another variable"
hello()#fuction execution

print("passing function to another function")
def execute(func):
    print("startion...")
    func()
    print("ending....")

execute(greeting)

print("function returning another function..")
def creat_function():
    def greet():
        print("hello raman")
    return greet
my_funct=creat_function()#function returning another function
my_funct()#now it is refering to greet and it is executated 

print("comdination of above ideas \n1 Receiving a function \n2 creation another function \n3 returning new function")
def decorate(funct):
    def wrapper():
        print("Before..")
        funct()#it remembers the enclosed reference variable
        print("After..")
    return wrapper

greeting=decorate(greeting)
greeting()

print("introduction of @ symbol to declorator before passing function as parameter.")
@decorate
def HRYD():
    print("How Are You Doing !")

HRYD()