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
        pass

    def getAllProducts(self):
        pass

    def getOrderByUser(self, user):
        pass
