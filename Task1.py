def calculate_average(*args):
    if not args:
        return 0

    sum_args = 0
    count = 0

    for i in args:
        sum_args += i
        count += 1

    return sum_args / count

print(calculate_average(2, 4, 6))
print(calculate_average(1, 3, 5, 7, 9))
print(calculate_average())
