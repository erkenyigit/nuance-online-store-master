from django.db import models
from shopcart.models import Cart
# Create your models here.
ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded'),
)


class Order(models.Model):
    order_id = models.CharField(max_length=120,blank=True) #delivery_id
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    status = models.CharField(max_length=120,default='created',choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default = 5.99,max_digits = 100, decimal_places = 2 )
    total = models.DecimalField(default = 5.99,max_digits = 100, decimal_places = 2 )
    ### IN OUR ER DIAGRAM
    # customer_id
    # Quantity
    # is_delivered
    # total_price
    # delivery_adress
    # product_ud
    def __str__(self):
        return self.order_id
