# def counter(start = 0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#     return step
# if __name__ == '__main__':
#     c1 = counter(10)
#     c2 = counter()
#     print(c1())
#     print(c1())
#     print(c2())
#     print(c2())
#     print(c2())
#
#
# def strip_string(string_chars = " "):
#     def do_strip(string):
#         return string.strip(string_chars)
#     return do_strip
#
# if __name__ == '__main__':
#     strip1 = strip_string()
#     strip2 = strip_string(' !@#$%^&*()')
#
#     print(strip1("hello world!!!!!#$%"))
#     print(strip2("hello world!!!!!#$%"))
#
#
#
#
# #def counter_add():
# #    def step(param):
# #    param += 5
# #    return param
# #    return step
#
# #if __name__ == '__main__':
# #    cnt = counter_add()
# #    k = int(input())
# #    print(cnt(k))
#
# def counter_add(n):
#     def step(param):
#         param += n
#         return param
#     return step

# if __name__ == '__main__':
#     cnt = counter_add(2)
#     k = int(input())
#     print(cnt(k))






def tagging(tag='h1'):
    def wrapper(string):
        return f'<{tag}>{string}</{tag}>'
    return wrapper

if __name__ == '__main__':
    tagging = tagging()
    string = input()
    print(tagging(string))

