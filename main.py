from task_manager import add_task, delete_task, show_tasks, done_task


def print_operations():
    print('Менеджер задач:')
    print('1. Додати нову задачу')
    print('2. Видалити задачу по ID')
    print('3. Відобразити всі задачі у списку')
    print('4. Позначити задачу як виконану')
    print('5. Вийти')


def main():
    while True:
        print_operations()
        choice = int(input('Виберіть операцію: '))

        match choice:
            case 1:
                description = input('Введіть опис задачі яку хочете додати: ').capitalize()
                add_task(description)
            case 2:
                task_id = int(input("Введіть ID задачі яку хочете видалити: "))
                delete_task(task_id)
            case 3:
                show_tasks()
            case 4:
                task_id = int(input("Введіть ID задачі яку хочете позначити як виконану: "))
                done_task(task_id)
            case 5:
                print("Роботу програми завершено.")
                break
            case _:
                print("Такої операції немає, спробуйте ще раз.")

if __name__ == '__main__':
    main()
