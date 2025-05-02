class User:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__accounts = []

    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname
    def get_age(self):
        return self.__age
    def get_accounts(self):
        return self.__accounts
    def set_name(self, name):
        self.__name = name
    def set_surname(self, surname):
        self.__surname = surname
    def set_age(self, age):
        self.__age = age
    def add_account(self, account):
        self.__accounts.append(account)


class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        return self.__balance
    def get_owner(self):
        return self.__owner
    def set_account_number(self, account_number):
        self.__account_number = account_number
    def set_balance(self, balance):
        self.__balance = balance


class BankSystem:
    def __init__(self):
        self.__users = []
        self.__accounts = []

    def create_user(self, name, surname, age):
        user = User(name, surname, age)
        self.__users.append(user)
        return user

    def create_account(self, user, initial_balance, account_number):
        account = BankAccount(account_number, initial_balance, user)
        user.add_account(account)
        self.__accounts.append(account)
        return account


    @staticmethod
    def deposit(account, amount):
        if amount > 0:
            new_balance = account.get_balance() + amount
            account.set_balance(new_balance)

    @staticmethod
    def withdraw(account, amount):
        if amount <= 0:
            print("Сума повинна бути більшою за 0.")
            return
        balance = account.get_balance()
        if balance >= amount:
            account.set_balance(balance - amount)
        else:
            print("Недостатньо коштів.")

    @staticmethod
    def transfer(sender_account, receiver_account, amount):
        sender_balance = sender_account.get_balance()
        if sender_balance >= amount:
            sender_account.set_balance(sender_balance - amount)
            receiver_balance = receiver_account.get_balance()
            receiver_account.set_balance(receiver_balance + amount)

if __name__ == '__main__':
    bank_system = BankSystem()
    user1 = bank_system.create_user("John", "Doe", 35)
    account1 = bank_system.create_account(user1, 1000, "4214 1242 1244 4124")
    bank_system.deposit(account1, 500)
    bank_system.withdraw(account1, 200)
    user2 = bank_system.create_user("Alice", "Smith", 28)
    account2 = bank_system.create_account(user2, 1500, "2144 1244 5523 2355")
    print(f"Баланс {user1.get_name()} {user1.get_surname()}: {account1.get_balance()}")
    print(f"Баланс {user2.get_name()} {user2.get_surname()}: {account2.get_balance()}")
    bank_system.transfer(account1, account2, 300)
    print(f"Баланс {user1.get_name()} {user1.get_surname()}: {account1.get_balance()}")
    print(f"Баланс {user2.get_name()} {user2.get_surname()}: {account2.get_balance()}")

