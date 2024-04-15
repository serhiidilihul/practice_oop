# Завдання 1:
# Бібліотека керування проектами
#
# Опис:
# 	Створіть бібліотеку на Python, яка дозволяє керувати проектами та їх завданнями.
# Бібліотека повинна дозволяти створювати проекти, додавати завдання до проектів,
# визначати відповідальних осіб, статуси завдань та дедлайни. Кожен проект і завдання
# повинні зберігатися у файлах.
#
# Функції:
# 	Створення, оновлення, видалення проектів та завдань.
# Визначення відповідальних осіб і дедлайнів.
# Зберігання та завантаження даних проекту у файл.
#
# Потрібно створити:
# 	Окремі модулі для керування проектами, завданнями, винятками та файловими операціями.
# Обробка ситуацій, як-от спроба доступу до неіснуючого проекту або завдання.
# Використання Git для керування версіями коду бібліотеки.
import os
import unittest


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task, executor=None, status=None, deadline=None):
        new_task = {
            'task': task,
            'executor': executor,
            'status': status,
            'deadline': deadline
        }
        self.tasks.append(new_task)

    def edit(self):
        print(f'Edit project \'{self.name}\'\nTasks:')
        count = 0
        for task in self.tasks:
            count += 1
            print(f'{count}. {task["task"]}')
        option = int(input('Choose task you want to edit. A number expected: '))
        count = 0
        for k, v in self.tasks[option-1].items():
            count += 1
            print(f'{count}. {k}: {v}')
        option = int(input('Enter issue you want to edit. A number expected: '))
        if option == 1:
            self.tasks[option-1]['task'] = input('Enter a task: ')
        elif option == 2:
            self.tasks[option-1]['executor'] = input('Enter an executor: ')
        elif option == 3:
            self.tasks[option-1]['status'] = input('Enter a status: ')
            if self.tasks[option-1]['status'] == 'done':
                self.tasks[option-1]['deadline'] = None
        elif option == 4:
            self.tasks[option-1]['deadline'] = input('Enter a deadline: ')

    def save_data(self):
        with open(f'task1_{self.name}.txt', 'w') as f:
            for task in self.tasks:
                for issue in task.items():
                    f.write(str(issue))
                f.write('\n')

    def delete(self):
        confirmation = input(f'Are you sure you want to delete project \'{self.name}\'? (yes/no): ')
        if confirmation.lower() == 'yes':
            file_name = f'task1_{self.name}.txt'
            try:
                os.remove(file_name)  # Delete the file containing project data
            except FileNotFoundError:
                pass  # If the file doesn't exist, continue with deletion
            print(f'Project \'{self.name}\' and its tasks have been deleted.')
        else:
            print('Deletion cancelled.')


class TestProject(unittest.TestCase):
    def setUp(self):
        # Create a sample project for testing
        self.project = Project("Test Project")
        self.project.add_task("Task 1", "John Doe", "in progress", "2024-04-15")
        self.project.add_task("Task 2", "Jane Smith", "pending", "2024-04-20")

    def test_delete_project(self):
        # Ensure the project is deleted successfully
        self.project.delete()
        # Assert that the project no longer exists (tasks list should be empty)
        self.assertEqual(len(self.project.tasks), 0)

    def tearDown(self):
        # Clean up any resources if needed
        pass

if __name__ == '__main__':
    unittest.main()
