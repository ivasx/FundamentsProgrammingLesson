class Money:
    def __init__(self, money):
        self.set_money(money)

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money
        else:
            self.__money = 0

    def get_money(self):
        return self.__money

    def add_money(self, money):
        self.__money += money.get_money()

    @staticmethod
    def __check_money(money):
        if isinstance(money, int) and money >= 0:
            return True
        else:
            return False

if __name__ == '__main__':
    money1 = Money(10)
    money2 = Money(20)
    money1.set_money(100)
    money2.add_money(money1)
    print(money1.get_money())  # Output: 100
    print(money2.get_money())  # Output: 120