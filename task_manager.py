import json


def create_id():
    with open('tasks.json', 'r', encoding='utf-8') as file:
        all_tasks = json.load(file)
    tasks_id = len(all_tasks) + 1
    return tasks_id

def add_task(*descriptions):
    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    for description in descriptions:
        task = {
            'description': description,
            'id': len(tasks) + 1,
            'done': False
        }
        tasks.append(task)
        print(f'Завдання "{description}" додано.')

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def delete_task(*id):
    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    new_tasks = []
    for task in tasks:
        if task['id'] in id:
            print(f'Завдання "{task["task_description"]}" видалено.')
        else:
            new_tasks.append(task)

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(new_tasks, file, indent=4, ensure_ascii=False)

def show_tasks():
    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    print('—' * 30)
    for task in tasks:
        for key, value in task.items():
            print(f'{key.capitalize()}: {value}')
        print('—' * 30)

def done_task(*id):
    with open('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)

    for task in tasks:
        if task['id'] in id:
            task['done'] = True
            print(f'Завдання "{task["description"]}" позначено як виконане.')

    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)




if __name__ == '__main__':
    show_tasks()
    done_task(1, 2, 3)
    show_tasks()

