def print_student_info(**kwargs):
  if not kwargs:
      print("Немає переданих аргументів функції.")
  for key, value in kwargs.items():
      print(f'{key.capitalize()} = {value}')




print_student_info()
print_student_info(імя = "Івас", прізвище = "Амброзяк")
print_student_info(студент = "Опа")
