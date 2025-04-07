def tagging(tag="h1"):
   def tagging_decorator(function):
       def wrapper(*args, **kwargs):
           return f"<{tag}>{function(*args, **kwargs)}</{tag}>"


       return wrapper


   return tagging_decorator




@tagging()
def make_lowercase(string):
   return string.lower()




if __name__ == '__main__':
   print(make_lowercase("PYTHON"))
