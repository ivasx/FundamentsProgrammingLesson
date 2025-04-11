class Good:
    name = 'Cheese'
    weight = 156
    category = 'Foods'
    price = 450


Good.price = 1000
Good.count = 10

if __name__ == '__main__':
    good = Good()
    print(good.name)
    print(good.weight)
    print(good.category)
    print(good.price)
    print(good.count)
