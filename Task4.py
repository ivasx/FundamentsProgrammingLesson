from functools import wraps


def sum_list(function):
   @wraps(function)
   def wrapper(*args):
       return sum(function(*args))
   return wrapper


@sum_list
def get_list(string):
   """
   Функція приймає обʼєкт рядка та повертає список з цілих чисел, які надходить на її вхід у вигляді рядка з цілих
   чисел, записаних через пробіл.
   

   Приклад такого рядка: "1 2 3 4 5"
   Результат: [1, 2, 3, 4, 5]
   """
   string_list = string.split()
   result = []

   for i in string_list:
       result.append(int(i))

   return result


print(get_list("1 2 3 4 5"))
