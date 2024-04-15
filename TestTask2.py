import unittest
from task2 import Dish, Menu, Order, User, PaymentProcessor

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu("Test Menu")
        self.dish1 = Dish("Spaghetti Carbonara", "Pasta", 12.99)
        self.dish2 = Dish("Margherita Pizza", "Pizza", 10.99)
        self.menu.add(self.dish1)
        self.menu.add(self.dish2)

    def test_show_menu(self):
        self.assertEqual(self.menu.dishes, [self.dish1, self.dish2])

    def test_search_menu(self):
        search_result = self.menu.search("Pizza")
        self.assertEqual(len(search_result), 1)
        self.assertEqual(search_result[0].name, "Margherita Pizza")

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.dish1 = Dish("Spaghetti Carbonara", "Pasta", 12.99)
        self.dish2 = Dish("Margherita Pizza", "Pizza", 10.99)
        self.order = Order()
        self.order.items = [self.dish1, self.dish2]

    def test_order_total(self):
        self.assertEqual(self.order.total(), 23.98)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("John Doe", 50)

    def test_user_save_data(self):
        self.user.save_user_data()

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.user = User("John Doe", 50)
        self.order = Order()
        self.dish1 = Dish("Spaghetti Carbonara", "Pasta", 12.99)
        self.dish2 = Dish("Margherita Pizza", "Pizza", 10.99)
        self.order.items = [self.dish1, self.dish2]

    def test_payment_success(self):
        payment_processor = PaymentProcessor(self.user, self.order)
        with self.assertRaises(Exception):
            payment_processor.pay()
if __name__ == '__main__':
    unittest.main()