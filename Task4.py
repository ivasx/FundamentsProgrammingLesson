class Cat:
    breed = ''
    age = 0
    name = ''
    color = ''


if __name__ == '__main__':
    cat1 = Cat()
    cat2 = Cat()
    cat3 = Cat()

    setattr(cat1, 'breed', 'Siamese')
    setattr(cat2, 'breed', 'Persian')
    setattr(cat3, 'breed', 'Maine Coon')

    setattr(cat1, 'age', 3)
    setattr(cat2, 'age', 5)
    setattr(cat3, 'age', 2)

    setattr(cat1, 'name', 'Rigik')
    setattr(cat2, 'name', 'Bobyk')
    setattr(cat3, 'name', 'Kapilot')

    setattr(cat1, 'color', 'Ginger')
    setattr(cat2, 'color', 'Black')
    setattr(cat3, 'color', 'White')

    print(f"Cat 1: Name: {cat1.name}, Breed: {cat1.breed}, Age: {cat1.age}, Color: {cat1.color}")
    print(f"Cat 2: Name: {cat2.name}, Breed: {cat2.breed}, Age: {cat2.age}, Color: {cat2.color}")
    print(f"Cat 3: Name: {cat3.name}, Breed: {cat3.breed}, Age: {cat3.age}, Color: {cat3.color}")
