import time


def some_fun(func):
    def wrapper(*args, **kwargs):
        print(f'Something Before Something')
        d = func(*args, **kwargs)
        return d
    return wrapper


@some_fun
def function(title):    
    return title


d= function('Amega') 
print(d)