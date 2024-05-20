INSERT INTO Products (productId, productName, description, price, quantityInStock, type) VALUES
(1, 'Laptop', '15-inch display, 8GB RAM, 256GB SSD', 999.99, 50, 'Electronics'),
(2, 'Smartphone', '6-inch display, 128GB storage', 699.99, 200, 'Electronics'),
(3, 'Headphones', 'Noise-cancelling, wireless', 199.99, 150, 'Accessories'),
(4, 'Office Chair', 'Ergonomic, adjustable height', 149.99, 75, 'Furniture'),
(5, 'Desk Lamp', 'LED, dimmable', 29.99, 300, 'Lighting'),
(6, 'Coffee Maker', '12-cup, programmable', 89.99, 120, 'Appliances'),
(7, 'Backpack', 'Water-resistant, 20L capacity', 49.99, 250, 'Accessories'),
(8, 'Running Shoes', 'Size 10, breathable mesh', 79.99, 100, 'Footwear'),
(9, 'Electric Kettle', '1.7L, auto shut-off', 39.99, 180, 'Appliances'),
(10, 'Wireless Mouse', 'Bluetooth, ergonomic design', 24.99, 500, 'Electronics');

INSERT INTO Users (userId, username, password, role) VALUES
(1, 'admin1', 'adminpassword1', 'Admin'),
(2, 'user1', 'userpassword1', 'User'),
(3, 'user2', 'userpassword2', 'User'),
(4, 'admin2', 'adminpassword2', 'Admin'),
(5, 'user3', 'userpassword3', 'User'),
(6, 'user4', 'userpassword4', 'User'),
(7, 'admin3', 'adminpassword3', 'Admin'),
(8, 'user5', 'userpassword5', 'User'),
(9, 'user6', 'userpassword6', 'User'),
(10, 'user7', 'userpassword7', 'User');

INSERT INTO [Order] (UserId) VALUES
(2),
(3),
(5),
(6),
(8),
(9),
(10),
(2),
(4),
(7);

INSERT INTO OrderProduct (OrderId, ProductId, Quantity) VALUES
(1, 1, 1),
(1, 3, 2),
(2, 2, 1),
(2, 6, 1),
(3, 5, 3),
(3, 7, 2),
(4, 4, 1),
(4, 9, 2),
(5, 10, 4),
(5, 8, 1),
(6, 1, 1),
(6, 2, 1),
(7, 3, 2),
(7, 5, 1),
(8, 4, 1),
(8, 6, 1),
(9, 7, 3),
(9, 9, 1),
(10, 10, 2),
(10, 8, 1);