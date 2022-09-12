
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
















