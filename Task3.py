from functools import wraps

def cache_results(function):
   cache = {}

   @wraps(function)
   def wrapper(*args):
       if args in cache:
           return cache[args]
       else:
           result = function(*args)
           cache[args] = result
           return result
   return wrapper

@cache_results
def add(a, b):
   print(f"Обчислення {a} + {b}")
   return a + b


print(add(2, 3))
print("----------------")
print(add(2, 3))
print("----------------")
print(add(4, 5))
