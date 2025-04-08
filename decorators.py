import json
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

def existence(function):
    @wraps(function)
    def wrapper(*args):
        with open('tasks.json', 'a+', encoding='utf-8') as file:
            file.seek(0)
            content = file.read()
            if not content.strip():
                file.write('[]')
                tasks = []
            else:
                tasks = json.loads(content)

        valid_ids = []

        for task_id in args:
            found = False
            for task in tasks:
                if task['id'] == task_id:
                    found = True
                    break

            if found:
                valid_ids.append(task_id)
            else:
                result = (f'Завдання з ID {task_id} не знайдено.')

        return function(*args)
    return wrapper