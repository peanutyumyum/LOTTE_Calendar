from django.db import models
from shop.models import Product
from django.contrib.auth import get_user_model

# Create your models here.
class Cart(models.Model):
    cart_id = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="carts")
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table ='Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table ='CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product