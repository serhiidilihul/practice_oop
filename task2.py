# Завдання 2: Система замовлення їжі онлайн
#
# Опис:
# 	Створіть систему для замовлення їжі онлайн, яка включає у себе керування меню ресторану,
# замовленнями користувачів та обробкою платежів. Система повинна дозволяти користувачам
# переглядати меню, робити замовлення, перевіряти статус свого замовлення та оплачувати онлайн.
#
# Функції:
# 	Перегляд меню ресторану з можливістю пошуку за категоріями та стравами.
# Додавання та оновлення страв у меню рестораном.
# Робота з кошиком: додавання страв, видалення страв, оформлення замовлення.
# Обробка платежів (симуляція, без реальних транзакцій).
# Відстеження статусу замовлень користувачем.
# Потрібно створити:
# Модулі для керування меню, замовленнями, користувачами та обробкою платежів.
# Класи для представлення страв, меню, замовлень, користувачів та платежів.
# Винятки для обробки помилок, наприклад, недостатньо коштів для платежу або замовлення недоступної страви.
# Зберігання даних про меню, замовлення та користувачів у файлах.
# Використання Git для керування версіями коду системи.
#
# Тестування:
# 	Написання модульних тестів для перевірки кожної частини системи, включаючи логіку замовлення,
# платежі та управління меню.
# ! Як результат потрібно надіслати посилання на репозиторії.

class Dish:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    # Represents a dish with attributes like name, category, price, etc.

class Menu:
    def show(self):
        print(self.name)
        print(self.category)
        print(self.price)

    def search(self, query):
        if query in any(self.name, self.category, self.price):
            print(self.name, self.category, self.price)

    def add(self, dish):
        self.name = dish.name
        self.category = dish.category
        self.price = dish.price

    def update(self, dish):
        option = input('Enter issue you want to update. A number expected: ')
        if option == '1':
            dish.name = input('Please enter new dish name: ')
        elif option == '2':
            dish.category = input('Please enter new dish category: ')
        elif option == '3':
            dish.price = input('Please enter new dish price: ')

    def save_dish(dish):
        with open('dishes.txt', 'a') as f:
            f.write(dish.name + '\n')
            f.write(dish.category + '\n')
            f.write(dish.price + '\n')
    # Manages the restaurant's menu: display, search, add, and update dishes.

class Order:
    def __init__(self, status='done'):
        self.items = []
        self.status = status

    def total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    
    def save_order(self, order):
        with open('orders.txt', 'a') as f:
            f.write(self.status + '\n')
            for item in self.items:
                f.write(item.name + '\n')
                f.write(item.category + '\n')
                f.write(item.price + '\n')

    # Represents a user's order with items, status, and payment details.

class User:
    def __init__(self, name, price):
        self.name = name
        self.orders = []
        self.price = price

    def save_user_data(self):
        with open('users.txt', 'a') as f:
            f.write(self.user + '\n')
            f.write(self.price + '\n')

class PaymentProcessor:
    def __init__(self, user, order):
        self.user = user.name
        self.price = user.price
        self.total = order.total

    def pay(self):
        if self.total <= self.price:
            print('Payment successful!')
        else:
            raise Exception('Payment failed')
        
    # Simulates payment processing.

# Exceptions for error handling

# File management module for data storage

# Test modules for each component


    