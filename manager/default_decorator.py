

time_dec = """
import time

def get_execution_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time() - start
        print(f"Время выполнения функции =  {end}c.")
        return end-start
    return wrapper


"""


