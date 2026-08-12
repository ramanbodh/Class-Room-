'''
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
@decorate#saves time 
def HRYD(): 
    print("How Are You Doing !")

HRYD()  

'''
print("A problem with current decorator it only works with function with no arguments \n for that we will be using *args(positional arguments)& \n**kwargs(Keyword arguments)\n the name args & kwargs is just community convention, the magic lies in asterisks(*,**)\n it allows function to  have variable number of arguments,meaning one can pass as many input as they can to the function,\*args will convert the inputs into single tuple and **kwargs will convert the key value into dictionary . ")

def decorator(funct):
    def wrapper(*args,**kwargs):
        print("Before...")
        funct(*args,**kwargs)
        print("After...")
    return wrapper

@decorator
def who(name):
    print("hi",name)
who("raman")       

print("now let code some simple decorator using *args and **kwargs ")
def decorator1(funct):
    def wrapper(*args,**kwargs):
        print("starting....")
        result=funct(*args,**kwargs)
        print("ending....")
        return result
    return wrapper
@decorator1
def add(a,b):
    return a+b

result=add(3,6)
print(result)

print("simple application of decorator of timing and ,model training for ai ml")

import time

def timer(funct):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=funct(*args,**kwargs)
        end=time.time()
        print("time taken:",end-start)
        return result
    return wrapper
@timer
def model_training():
    time.sleep(2)
    return "model trained"

print(model_training())