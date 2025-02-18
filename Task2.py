def greet_message(name, surname, language = "en"):
    name = validation(name)
    surname = validation(surname)
    greeting = ""

    if language == 'en':
        greeting = f"Hello world! My name is {name} {surname}"
    elif language == 'ua':
        greeting = f"Привіт, світ! Мене звуть {name} {surname}"
    elif language == 'pl':
        greeting = f"Witaj świecie! Nazywam się {name} {surname}"
    elif language == 'de':
        greeting = f"Hallo Welt! Mein Name ist {name} {surname}"
    else:
        print("Incorrect language. English is used..")
        greeting = f"Hello world! My name is {name} {surname}"

    print(greeting)

def validation(word):
    while not word.strip() or not any(char.isalpha() for char in word):
        word = input(f"The entered data ('{word}') is empty or does not contain any letters. Try again: ")
    while not all(char.isalpha() or char == ' ' or char == '-' for char in word):
        word = input(
            f"The entered data ('{word}') contains invalid characters. Only letters, spaces, and hyphens are allowed. Try again: ")

    if ' ' in word:
        word = ' '.join([part.capitalize() for part in word.split()])
    elif '-' in word:
        word = '-'.join([part.capitalize() for part in word.split('-')])
    else:
        word = word.capitalize()

    return word


def main():
    language = input("Enter language (en, ua, pl, de): ")

    while language not in ['en', 'uk', 'pl', 'de']:
        print("Incorrect language. Try again, or use default (Just press enter).")

        language = input()
        if not language:
            break

    name = input("Enter name: ")
    surname = input("Enter surname: ")

    greet_message(name, surname, language)

main()

