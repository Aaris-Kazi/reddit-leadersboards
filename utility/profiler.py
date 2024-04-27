from functools import wraps
import time

def fucntionProfiler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        _exec = end - start

        print(f"The execution time for {func.__name__} is : {_exec:.4f}")
        return res
        
    return wrapper