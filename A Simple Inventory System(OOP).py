class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_quantity(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                return
        print("Product not found.")

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]

    def display_products(self):
        for product in self.products:
            print(product)

    def total_value(self):
        return sum(product.price * product.quantity for product in self.products)

inventory = Inventory()
inventory.add_product(Product(1, "Laptop", 1200, 10))
inventory.add_product(Product(2, "Mouse", 25, 50))
inventory.display_products()
inventory.update_quantity(1, 15)
print("Updated Inventory:")
inventory.display_products()
print(f"Total Inventory Value: ${inventory.total_value()}")
inventory.remove_product(2)
print("Inventory after removal:")
inventory.display_products()