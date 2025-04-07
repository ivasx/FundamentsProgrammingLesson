def create_student_report(*students, **subjects):
   print("Звіт успішності:")
   for student in students:
       print(f"Student: {student}")


   print("Marks:")
   for key, value in subjects.items():
       print(f"{key.capitalize()}: {value}")


if __name__ == '__main__':
   create_student_report("Іван", "Марія", math=12, physics=11, history=10)
