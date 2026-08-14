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
