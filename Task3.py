class Person:
   first_name = 'Івас'
   last_name = 'Амброзяк'
   age = 17
   date_of_birth = '2 грудня'




if __name__ == '__main__':
   person = Person()
   if hasattr(person, 'first_name'):
       print(True)
   else:
       print(False)
