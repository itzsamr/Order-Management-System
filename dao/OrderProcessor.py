from .IOrderManagementRepository import IOrderManagementRepository
from exception.UserNotFound import UserNotFound
from exception.OrderNotFound import OrderNotFound
from util.DBConnUtil import DBConnUtil
from entity.User import User


class OrderProcessor(IOrderManagementRepository):
    def createOrder(self, user, products):
        pass

    def cancelOrder(self, userId, orderId):
        pass

    def createProduct(self, user, product):
        pass

    def createUser(self, user):
        try:
            connection = DBConnUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM Users WHERE userId = ?", user.getUserId()
                )
                user_count = cursor.fetchone()[0]
                if user_count > 0:
                    print(f"User with ID {user.getUserId()} already exists.")
                    return
                cursor.execute(
                    "INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                    user.getUserId(),
                    user.getUsername(),
                    user.getPassword(),
                    user.getRole(),
                )
                connection.commit()
                print("User created successfully.")
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error creating user:", e)
        finally:
            if connection:
                connection.close()

    def getAllProducts(self):
        pass

    def getOrderByUser(self, user):
        pass
