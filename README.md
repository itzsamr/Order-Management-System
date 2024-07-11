# Order Management System

The `Order Management` system is a Python-based application for managing users, products, and orders. It provides a console interface to create users, add products, place orders, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Features

- **Create User**: Add new users with an ID, username, password, and role (Admin/User).
- **Create Product**: Add new products with details like ID, name, description, price, quantity, and type.
- **Create Order**: Place orders for users with a list of products.
- **Cancel Order**: Cancel existing orders.
- **Get All Products**: Retrieve and display all available products.
- **Get Orders by User**: Retrieve and display all orders for a specific user.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/itzsamr/Order-Management-System.git
    cd Order-Management-System
    ```

2. **Set up the Python environment** (optional but recommended):
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Interact with the system**:
    Follow the console prompts to create users, products, and orders. 

### Example:

- **Creating a User**:
    ```
    Enter User ID: 1
    Enter Username: john_doe
    Enter Password: password123
    Enter Role (Admin/User): User
    ```

- **Creating a Product**:
    ```
    Enter User ID: 1
    Enter Product ID: 101
    Enter Product Name: Laptop
    Enter Product Description: High-performance laptop
    Enter Product Price: 999.99
    Enter Product Quantity: 10
    Enter Product Type (Electronics/Clothing): Electronics
    ```

- **Creating an Order**:
    ```
    Enter User ID: 1
    Enter Product ID (0 to finish): 101
    Enter Product ID (0 to finish): 0
    ```

## Dependencies

- Python 3.x
- Other dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


