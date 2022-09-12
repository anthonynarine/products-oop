from product import Product
from customer import Customer
from product import Product


customer_one = Customer("Julia")
print(f"\nThe customer's name is {customer_one.name}: \n")

product_one = Product("Apple", 1, "fruit")
product_two = Product("Grapes", 3, "fruit")
product_three = Product("bread", 2, "grain")
product_four = Product("cheese", 5, "dairy")

customer_one.add_item_to_cart(product_one)
customer_one.add_item_to_cart(product_two)
customer_one.add_item_to_cart(product_three)
customer_one.add_item_to_cart(product_four)

# customer_one.view_items_in_cart()
print (f"\nThe total price of the shopping carts items is :{customer_one.shopping_cart.cart_total()}\n")
print (f"Total items in shopping cart = {len(customer_one.shopping_cart.products)}")
customer_one.shopping_cart.empty_shopping_cart()
customer_one.view_items_in_cart
print (len(customer_one.shopping_cart.products))
print("\n")