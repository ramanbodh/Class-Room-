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
