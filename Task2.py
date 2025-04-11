class Car:
    mark = 'Volkswagen'
    model = 'PassatB5'
    weight = 2500000
    price = 7000


if __name__ == '__main__':
    print('Car mark: ', getattr(Car, 'mark', False))
    print('Car model: ', getattr(Car, 'model', False))

    setattr(Car, 'color', 'green')
    print("Updated car color: ", getattr(Car, 'color'))

    if hasattr(Car, 'weight'):
        delattr(Car, 'weight')

    print()
    
    for key, value in Car.__dict__.items():
        if key[0] != '_':
            print(f'{key}: {value}')
