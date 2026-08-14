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
