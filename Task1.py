def get_initial_balance():
    balance = round(float(input("Enter the initial account balance. The balance must be a positive number: ")), 2)
    if balance < 0:
        print("The balance cannot be negative. Try again.")
        return get_initial_balance()
    return balance

def show_menu():
    print("\n[1] Deposit")
    print("[2] Withdraw")
    print("[3] Check your balance")
    print("[4] Exit")

def deposit(balance):
    depos = round(float(input("Enter the desired deposit amount: ")), 2)
    if depos < 0:
        print("The deposit cannot be negative. Try again.")
        return deposit(balance)
    balance += depos
    return balance

def withdraw(balance):
    withdrawing = round(float(input("Enter the amount you want to withdraw: ")), 2)
    if withdrawing > balance:
        print("Insufficient funds. Try again.")
        return withdraw(balance)
    balance -= withdrawing
    return balance

def check_balance(balance):
    print("\n" + "="*30)
    print(" " * 6 + "💰 Account balance 💰")
    print("="*30)
    print(f" Current balance: ${balance:.2f}")
    print("="*30 + "\n")

def check_new_balance(balance):
    print(f"Your new balance: ${balance:.2f}")

def atm():
    initial_balance = get_initial_balance()
    balance = initial_balance
    while (True):
        show_menu()
        choice = input("\nChoose the option: ")
        match choice:
            case "1":
                balance = deposit(balance)
                check_new_balance(balance)
            case "2":
                balance = withdraw(balance)
                check_new_balance(balance)
            case "3":
                check_balance(balance)
            case "4":
                print("The ATM  has completed its operation. Have a nice day!")
                break
            case _:
                print("Invalid option. Try again.")

atm()