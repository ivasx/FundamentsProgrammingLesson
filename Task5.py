from functools import wraps


def uppercase(function):
   @wraps(function)
   def wrapper(*args):
       return function(*args).upper()

   return wrapper


def exclaim(function):
   @wraps(function)
   def wrapper(*args):
       return function(*args) + "!!!"
   return wrapper


@exclaim
@uppercase
def greet(name):
   return f"Привіт, {name}"


@exclaim
@uppercase
def farewell(name):
   return f"До побачення, {name}"


print(greet("Івас"))
print(farewell("Івас"))
