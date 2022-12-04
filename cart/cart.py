class Cart():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id]={
                "product_id": product.id,
                "name": product.name,
                "price": product.price,
                "quantity": 1,
                "image": product.image
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"]+1
                    break
        self.save_cart()

    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete(self, product):
        if str(product.id) in self.cart:
            del self.cart[product.id]
            self.save_cart()

    def decrement(self, product):
         for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"]-1
                    if value["quantity"] < 1:
                        self.delete(product)
                    break
                else:
                    print("El producto no existe en el carrito de compras")


    def clean_cart(self):
        self.session["cart"] = {}
        self.session.modified = True