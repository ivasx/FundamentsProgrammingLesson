class Car:
    def __init__(self, brand, model, year, speed, power, color):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__power = power
        self.__color = color
        self.__driver = None

    def add_driver(self, driver):
        self.__driver = driver

    def get_speed(self):
        return self.__speed

    def get_power(self):
        return self.__power

    def get_driver(self):
        return self.__driver

    def get_info(self):
        return f"{self.__brand} {self.__model} ({self.__year}), колір: {self.__color}"

class Driver:
    def __init__(self, name, age, driving_experience):
        self.__name = name
        self.__age = age
        self.__experience = driving_experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

class Race:
    @staticmethod
    def start_race(car1, car2):
        driver1 = car1.get_driver()
        driver2 = car2.get_driver()

        if driver1 is None or driver2 is None:
            print("Обидва автомобілі повинні мати призначених водіїв!")
            return None

        score1 = car1.get_speed() + car1.get_power() * driver1.get_experience()
        score2 = car2.get_speed() + car2.get_power() * driver2.get_experience()

        if score1 > score2:
            return car1
        elif score2 > score1:
            return car2
        else:
            return None  # Нічия

    @staticmethod
    def print_winner(winner):
        if winner:
            driver = winner.get_driver()
            print(f"Переможець: {driver.get_name()} на {winner.get_info()}")
        else:
            print("Гонка завершилась внічию!")

if __name__ == '__main__':
    car1 = Car("BMW", "X5", 2022, 250, 300, "Black")
    car2 = Car("Audi", "A6", 2023, 240, 280, "White")
    driver1 = Driver("John", 35, 15)
    driver2 = Driver("Alice", 28, 10)
    car1.add_driver(driver1)
    car2.add_driver(driver2)
    race = Race()
    winner = race.start_race(car1, car2)
    race.print_winner(winner)
