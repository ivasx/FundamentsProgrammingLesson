def descending_order(number):
    if not number.isdigit() or int(number) < 0:
        print("The passed argument does not meet the specified requirements.")
        return

    max_number = int(''.join(sorted(str(number), reverse=True)))
    return max_number

def main():
    print("To end the program, press enter.")
    number = "1"
    while number != "":
        number = input("Enter a number: ").strip()
        print(descending_order(number))

main()