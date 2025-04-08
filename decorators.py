from functools import wraps


def log_calls(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)

        logs = '\n' + '-' * 50 + '\n'
        logs += f'Функція {function.__name__} викликана з аргументами: {args}'
        if result:
            logs += f'\nРезультат: \n{result}'
        logs += '\n' + '-' * 50 + '\n'

        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(logs)
        return result
    return wrapper