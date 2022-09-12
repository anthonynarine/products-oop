
from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_item_to_cart (self, product):
        self.shopping_cart.add_product_to_cart(product)

    def view_items_in_cart (self):
        for product in self.shopping_cart.products:
            print(product.name)

