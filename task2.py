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

class Menu:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def show(self):
        print(self.name)
        for dish in self.dishes:
            print(dish.name, dish.category, dish.price)

    def search(self, query):
        found = []
        for dish in self.dishes:
            if query in [dish.name, dish.category, str(dish.price)]:
                found.append(dish)
        return found

    def add(self, dish):
        self.dishes.append(dish)

    def update(self, dish):
        option = input('Enter issue you want to update. A number expected: ')
        if option == '1':
            dish.name = input('Please enter new dish name: ')
        elif option == '2':
            dish.category = input('Please enter new dish category: ')
        elif option == '3':
            dish.price = input('Please enter new dish price: ')

    def save_dishes(self):
        with open('dishes.txt', 'a') as f:
            for dish in self.dishes:
                f.write(dish.name + '\n')
                f.write(dish.category + '\n')
                f.write(str(dish.price) + '\n')

class Order:
    def __init__(self, status='done'):
        self.items = []
        self.status = status

    def total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    
    def save_order(self):
        with open('orders.txt', 'a') as f:
            f.write(self.status + '\n')
            for item in self.items:
                f.write(item.name + '\n')
                f.write(item.category + '\n')
                f.write(str(item.price) + '\n')

class User:
    def __init__(self, name, wallet):
        self.name = name
        self.orders = []
        self.wallet = wallet

    def save_user_data(self):
        with open('users.txt', 'a+') as f:
            f.write(self.name + '\n')
            f.write(str(self.wallet) + '\n')

class PaymentProcessor:
    def __init__(self, user, order):
        self.user = user.name
        self.wallet = user.wallet
        self.total = order.total()

    def pay(self):
        if self.total <= self.wallet:
            print('Payment successful!')
        else:
            raise Exception('Payment failed')

if __name__ == "__main__":
    dish1 = Dish("Spaghetti Carbonara", "Pasta", 12.99)
    dish2 = Dish("Margherita Pizza", "Pizza", 10.99)
    dish3 = Dish("Caesar Salad", "Salad", 8.99)

    menu = Menu("Restaurant Menu")
    menu.add(dish1)
    menu.add(dish2)
    menu.add(dish3)

    menu.show()

    search_result = menu.search("Pizza")
    if search_result:
        print("Search Result:")
        for dish in search_result:
            print(dish.name, dish.category, dish.price)
    else:
        print("No matching dish found.")

    user = User("John Doe", 50)

    order = Order()
    order.items = [dish1, dish2]

    user.save_user_data()
    order.save_order()
    payment_processor = PaymentProcessor(user, order)
    payment_processor.pay()

    user.save_user_data()
    