# E-commerce Order Management System (Python OOP)

This is a simple and clean **Object-Oriented Python** implementation of an E-commerce Order Management System.  
It models products, customers, orders, and inventory, using best practices for class design, data validation, and business logic.

---

## ✨ Features

✅ Add and manage products in inventory  
✅ Add and manage customers  
✅ Create orders and order items  
✅ Apply discounts to individual items or entire orders  
✅ Calculate subtotal, tax, and total  
✅ Update product stock automatically  
✅ Mark orders as paid  
✅ Provide order summaries  
✅ Extendable and easy to maintain

---

## 📦 Project Structure


---

## 🛠 Classes Overview

- **Product** → Represents a product with ID, name, price, and stock.
- **Customer** → Represents a customer with ID, name, and email.
- **OrderItem** → Represents a single product and its quantity in an order.
- **Order** → Represents a complete order with multiple items, taxes, and discounts.
- **Inventory** → Manages available products.
- **ECommerceSystem** → Manages customers, orders, and inventory at the system level.

---

## 🚀 Example Usage

```python
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
