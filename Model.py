from typing import List
from datetime import datetime

class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int):
        if quantity > self.stock:
            raise ValueError("Insufficient stock.")
        self.stock -= quantity

    def __str__(self):
        return f"{self.name} (${self.price:.2f}) - Stock: {self.stock}"


class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > product.stock:
            raise ValueError(f"Not enough stock for {product.name}.")
        self.product = product
        self.quantity = quantity
        self.subtotal = product.price * quantity

    def apply_discount(self, discount_percent: float):
        if 0 < discount_percent < 100:
            discount = self.subtotal * (discount_percent / 100)
            self.subtotal -= discount

    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ${self.subtotal:.2f}"


class Order:
    TAX_RATE = 0.1  # 10% tax

    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.items: List[OrderItem] = []
        self.created_at = datetime.now()
        self.is_paid = False

    def add_item(self, product: Product, quantity: int):
        item = OrderItem(product, quantity)
        product.update_stock(quantity)
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.subtotal for item in self.items)

    def calculate_tax(self):
        return self.calculate_subtotal() * Order.TAX_RATE

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def apply_order_discount(self, discount_percent: float):
        for item in self.items:
            item.apply_discount(discount_percent)

    def mark_as_paid(self):
        self.is_paid = True

    def __str__(self):
        status = "Paid" if self.is_paid else "Pending"
        item_list = "\n".join(str(item) for item in self.items)
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()
        return (
            f"Order #{self.order_id} for {self.customer.name} [{status}]\n"
            f"{item_list}\n"
            f"Subtotal: ${subtotal:.2f}\n"
            f"Tax: ${tax:.2f}\n"
            f"Total: ${total:.2f}"
        )


class Inventory:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def list_products(self):
        return "\n".join(str(product) for product in self.products)

    def find_product_by_id(self, product_id: int) -> Product:
        for product in self.products:
            if product.product_id == product_id:
                return product
        raise ValueError("Product not found.")


class ECommerceSystem:
    def __init__(self):
        self.inventory = Inventory()
        self.customers: List[Customer] = []
        self.orders: List[Order] = []
        self.order_counter = 1

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def create_order(self, customer_id: int) -> Order:
        customer = self.find_customer_by_id(customer_id)
        order = Order(self.order_counter, customer)
        self.order_counter += 1
        self.orders.append(order)
        return order

    def find_customer_by_id(self, customer_id: int) -> Customer:
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        raise ValueError("Customer not found.")

    def get_order_summary(self, order_id: int) -> str:
        for order in self.orders:
            if order.order_id == order_id:
                return str(order)
        raise ValueError("Order not found.")

    def __str__(self):
        return (
            f"ECommerce System with {len(self.customers)} customers, "
            f"{len(self.inventory.products)} products, "
            f"and {len(self.orders)} orders."
        )


# Example usage (for testing, not production)
if __name__ == "__main__":
    # Initialize system
    system = ECommerceSystem()

    # Add products
    system.inventory.add_product(Product(1, "Laptop", 1200.00, 10))
    system.inventory.add_product(Product(2, "Smartphone", 800.00, 15))

    # Add customer
    customer = Customer(1, "Alice", "alice@example.com")
    system.add_customer(customer)

    # Create order
    order = system.create_order(1)
    order.add_item(system.inventory.find_product_by_id(1), 1)
    order.add_item(system.inventory.find_product_by_id(2), 2)

    # Apply discount and mark as paid
    order.apply_order_discount(10)
    order.mark_as_paid()

    # Print order summary
    print(system.get_order_summary(order.order_id))
