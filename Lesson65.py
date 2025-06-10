import random
import time

attempts = 0
st_time = time.time()
while True:

    val_list = [random.randint(0, 10) for i in range(7)]
    print(val_list)
    if all(x == 5 for x in val_list):
        end_time = time.time()
        break
    else:
        attempts += 1

print(attempts)
print('Час почвтку:', st_time)
print('Час закінчення:', end_time)
print(time.time() - st_time)


