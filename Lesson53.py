import pickle
# try:
#     with open('my_file.txt', 'a+', encoding='utf-8') as file:
#         file.seek(0)
#         f = file.readlines()
#         print(f)
#         file.write('Hello\n')
#         file.write('Hello\n')
#         file.write('Hello\n')
# except:
#     print('Something went wrong')

books = [
    ('1984', 'Джордж Орвелл'),
    ('Майстер і Маргарита', 'Михайло Булгаков'),
    ('Гаррі Поттер і філософський камінь', 'Джоан Роулінг')
]

file = open('books.txt', 'rb')
bs = pickle.load(file)
print(bs)
file.close()
