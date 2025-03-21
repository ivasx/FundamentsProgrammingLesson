def show_console(function):
   def wrapper(width, height):
       result = function(width, height)
       print(f"Площа прямокутника: {result}")
       return result
   return wrapper

@show_console
def get_rectangle_area(width, height):
   area = width * height
   return area

if __name__ == '__main__':
   width = int(input("Введіть ширину: "))
   height = int(input("Введіть висоту: "))
   get_rectangle_area(width, height)
