from project.domain_layer.stores_managment.Product import Product


class Inventory:
    def __init__(self):
        # products = {"product name",(Product,amount,price,?discount?)}
        self.products = {}

    def add_product(self, product_name, product: Product, amount=0, price=0):
        """

        Args:
            product_name:
            product:
            amount:
            price:
        """
        self.products[product_name] = product

    # def remove_product(self, product_name):
    #     self.products.pop(product_name)

    def update_product(self, product_name, attribute, updated):
        if product_name in self.products.keys():
            if attribute == "discount":
                self.products.get(product_name).discount.append(updated)
            else:
                setattr(self.products.get(product_name), attribute, updated)
            return True
        return False

    def buy_product(self, product_name, amount):
        if product_name not in self.products.keys():
            return False
        if amount > self.products.get(product_name).amount or amount < 0:
            return False
        self.products.get(product_name).amount -= amount
        return True

    def get_products(self):
        return self.products

    def remove_product(self, product_name):
        if product_name in self.products.keys():
            self.products.pop(product_name)
            return True
        return False

    def add_discount_to_product(self, product_name, discount):
        if product_name in self.products.keys():
            self.products[product_name].add_discount(discount)
            return True
        return False

    def edit_product_discount(self, product_name, discount_id):
        pass
