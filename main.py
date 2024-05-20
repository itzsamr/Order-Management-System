from dao.OrderProcessor import OrderProcessor
from entity.Product import Product
from entity.User import User
from exception import UserNotFound, OrderNotFound


class OrderManagement:
    def __init__(self):
        self.orderProcessor = OrderProcessor()

    def display_menu(self):
        print("\nOrder Management System")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Orders by User")
        print("7. Exit")

    def create_user(self):
        userId = int(input("Enter User ID: "))
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role (Admin/User): ")
        user = User(userId, username, password, role)
        self.orderProcessor.createUser(user)

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.create_product()
            elif choice == "3":
                self.create_order()
            elif choice == "4":
                self.cancel_order()
            elif choice == "5":
                self.get_all_products()
            elif choice == "6":
                self.get_orders_by_user()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    orderManagement = OrderManagement()
    orderManagement.main()
