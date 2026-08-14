print("this is factory decorator , where we having 3 or more layers of function forming a decorator , where first layer can be pass some configuration value .")
def repeat(times):
    def decorator(funct):
        def wrapper(*args,**kwargs):
            print("before....")
            for _ in range(times):
                print(funct(*args,**kwargs))
            print("after....")
        return wrapper
    return decorator

@repeat(3)
def greeting(name):
    return f"hello {name}"  

greeting("raman")

print ("equivalient code without @ , will be ")

def greeting1(name):
    return f"hey how are you,  {name}"

greeting1=repeat(4)(greeting1)
greeting1("RAM")

print("minimum value validator program\n\n")
def minimum(number):
    def decorator(funct):
        def wrapper(value):#here value is passed directly without storing it in tuple and dictionary like *args,**kwargs
            if value < number:
                print("to small value")
                return
            return funct(value)
        return wrapper
    return decorator

print(" lets try without using @ symbol first")

def num1(value):
    return f"value is {value}"
num1=minimum(5)(num1)
result=num1(10)
print(result)