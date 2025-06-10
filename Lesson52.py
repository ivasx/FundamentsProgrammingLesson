try:
    with open('text.txt', encoding='utf-8') as file:
        s = file.readlines()
        print(s)
    # file = open('text.txt', encoding='utf-8')
    # try:
    #     s = file.read()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print('File not found')
except:
    print('Something went wrong')
finally:
    print(file.closed)