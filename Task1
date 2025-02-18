def greet_message(name, surname):
    name = validation(name)
    surname = validation(surname)
    print(f"Hello world! My name is {name} {surname}")

def validation(word):
    while not word.strip() or not any(char.isalpha() for char in word):
        word = input(f"The entered data ('{word}') is empty or does not contain any letters. Try again: ")
    while not all(char.isalpha() or char == ' ' or char == '-' for char in word):
        word = input(f"The entered data ('{word}') contains invalid characters. Only letters, spaces, and hyphens are allowed. Try again: ")
    
    if ' ' in word:
        word = ' '.join([part.capitalize() for part in word.split()])
    elif '-' in word:
        word = '-'.join([part.capitalize() for part in word.split('-')])
    else:
        word = word.capitalize()
        
    return word

def main():
    name = input("Enter name: ")
    surname = input("Enter surname: ")

    greet_message(name, surname)

main()

