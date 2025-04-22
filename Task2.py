import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(self.brand, self.model, self.year, "Вік:", self.calculate_age())

    def change_model(self, new_model):
        self.model = new_model
        print("Нове значення моделі", self.model)

    def calculate_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        return age

if __name__ == '__main__':
    car = Car("Audi", "A4", 2016)
    car.display_info()
    car.change_model("A5")
    print(car.calculate_age())
    car.display_info()