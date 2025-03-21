def validate_input(function):
   def wrapper(username, password):
       if  type(username) != str or len(username) < 3:
           print("Ім'я користувача повинно бути довше ніж 3 символи та бути рядком.")
           return
       if  type(password) != str or len(password) < 6:
           print("Пароль повинен бути довше ніж 6 символів та бути рядком.")
           return

       if not any(char.isdigit() for char in password):
           print("Пароль повинен містити хоча б одну цифру.")
           return
       if any(char in "@$%^" for char in username):
           print("Ім'я користувача містить неприпустимі символи.")
           return
       if username[0] == ".":
           print("Ім'я користувача не може починатися з крапки.")
           return


       result = function(username, password)
       return result
   return wrapper

@validate_input
def create_user(username, password):
   new_user = {
       'username': username,
       'password': password
   }
   return new_user

if __name__ == '__main__':
   username = input("Введіть ім'я користувача: ")
   password = input("Введіть пароль: ")
   user = create_user(username, password)
   print(f"Username: {user['username']}")
   print(f"Password: {user['password']}")
