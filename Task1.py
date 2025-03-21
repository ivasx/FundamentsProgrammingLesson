def function_decorator(function):
   def wrapper():
       print("До виклику функції")
       function()
       print("Після виклику функції")

   return wrapper

@function_decorator
def addition():
   first_number = input("Введіть перше число: ")
   second_number = input("Введіть друге число: ")
   result = first_number + second_number
   print(f"{first_number} + {second_number} = {result}")
   return result

if __name__ == '__main__':
   addition()
