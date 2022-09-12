
class ShoppingCart:
    def __init__(self):
        self.products = []

    def cart_total(self):
        total = 0
        for product in self.products:
            total += product.price 
        return total
  
    def add_product_to_cart(self, product):
        self.products.append(product)
        print(f"\n\t{product.name} added to the shopping cart")

    def empty_shopping_cart(self):
        self.products.clear()
        print (f"The cart is now empty")

class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_item_to_cart (self, product):
        self.shopping_cart.add_product_to_cart(product)

    def view_items_in_cart (self):
        for product in self.shopping_cart.products:
            print(product.name)

class Product:

     def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

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

customer_one.view_items_in_cart()
print (len(customer_one.shopping_cart.products))
customer_one.shopping_cart.empty_shopping_cart()
customer_one.view_items_in_cart
print (len(customer_one.shopping_cart.products))

        



















