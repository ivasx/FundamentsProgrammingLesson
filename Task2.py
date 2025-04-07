def greet_students(greeting, *names):
   if not names:
       print("Немає студентів для привітання")
       return


   for name in names:
       print(f"{greeting} {name}.")
   return


greet_students("Вітаю!", "Івас", "Лалала", "Оп оп оп")
