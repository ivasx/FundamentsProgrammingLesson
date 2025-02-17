def greet_message(name, surname):
    name = name.lower().capitalize()
    surname = surname.lower().capitalize()

    print(f"Hello world! My name is {name} {surname}")
def validation(word):
    if not word or not any(char.isalpha() for char in word):


def main():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    greet_message(name, surname)

main()