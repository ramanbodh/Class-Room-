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
