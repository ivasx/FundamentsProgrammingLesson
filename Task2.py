from functools import wraps
def log_calls(filename):
   def log_decorator(function):
       @wraps(function)
       def wrapper(*args):
           with open(filename, 'a', encoding='utf-8') as file:
               file.write(f"Функція {function.__name__} викликана з аргументами {args}, результат: {function(*args)}")
               file.write("\n")


       return wrapper
   return log_decorator




@log_calls("log.txt")
def multiply(first_number, second_number):
   return first_number * second_number




multiply(3, 4)
multiply(5, 2)
