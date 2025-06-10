import time
v = 100 ** 10000000
a = (x for x in range(10**100))  # 10 мільйонів
t_s = time.time()
for i in a:
    continue
t_e = time.time()

print(f'Старт програми: {t_s}\n'
      f'Завершення програми: {t_e}\n'
      f'Пройшло часу {t_e-t_s}.')
