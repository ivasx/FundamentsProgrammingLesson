import json
import decorators



@decorators.log_calls
def add_task(*descriptions):
    """
    Функція приймає в себе опис завдання, та додає його в файл
    "task.json". Кожне завдання містить унікальний номер (ID),
    який створюється автоматично за допомогою функції create_id.
    А також інформацію про те, чи виконане воно. За замовчуванням - False.

    :param descriptions:
    """

    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    results = []
    used_ids = set()
    for task in tasks:
        used_ids.add(task['id'])

    for description in descriptions:
        new_id = 1
        while new_id in used_ids:
            new_id += 1

        task = {
            'description': description,
            'id': new_id,
            'done': False
        }

        tasks.append(task)
        used_ids.add(new_id)
        results.append(f'Завдання "{description}" додано.')

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

    result = '\n'.join(results)
    print(result)
    return result

@decorators.log_calls
def delete_task(*id):
    """
    Функція приймає один або декілька унікальних номерів завдань (ID)
    в якості параметру, та видаляє завдання з такими ID.
    :param id:
    """

    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    new_tasks = []
    results = []

    for task in tasks:
        if task['id'] in id:
            results.append(f'Завдання "{task["description"]}" видалено.')
        else:
            new_tasks.append(task)

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(new_tasks, file, indent=4, ensure_ascii=False)

    result = '\n'.join(results)
    print(result)
    return result

@decorators.log_calls
def show_tasks():
    """
    Функція відображає усі наявні завдання, які вже записані у файл.
    Не потребує жодних аргументів.
    """

    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    print('—' * 30)
    for task in tasks:
        for key, value in task.items():
            print(f'{key.capitalize()}: {value}')
        print('—' * 30)

    return 'Відображено всі завдання.'

@decorators.log_calls
def done_task(*id):
    """
    Функція приймає один або декілька унікальних номерів завдань (ID)
    в якості параметру, та позначає завдання з такими ID виконаними
    :param id:
    """

    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    results = []

    for task in tasks:
        if task['id'] in id:
            task['done'] = True
            results.append(f'Завдання "{task["description"]}" позначено як виконане.')

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

    result = '\n'.join(results)
    print(result)
    return result



if __name__ == '__main__':
    add_task('Поприбирати', 'поїсти', 'випити кави')
    show_tasks()
    delete_task(1, 3)
    done_task(2)
    show_tasks()


