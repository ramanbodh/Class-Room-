print("putting all the topics together , function ,function as argument, returning function,closure,decorator ,factory decorator and try and except ")

def repeat(times):
    def decorator(fucnt):
        def wrapper(*args,**kwargs):
            for _ in range(times):
                try:
                    return fucnt(*args,**kwargs)# return will  skip the whole loop so there for we only have one retunr and print for the except Exception to keep in the loop
                except Exception:
                    print("Failed try again!")
        return wrapper
    return decorator

attempts=0

@repeat(3)
def test():
    global attempts
    attempts+=1
    print(f"Attempts:{attempts}")
    if attempts < 3:
        raise ValueError ("Failed")
    return "Success"          

result=test()
print(result)              