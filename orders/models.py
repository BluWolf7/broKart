from django.db import models
from customers.models import Customer
from products.models import Product
# Create your models here.
# an order is an order status 
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE = (
                    (ORDER_CONFIRMED, "ORDER_CONFIRMED"),
                    (ORDER_PROCESSED, "ORDER_PROCESSED"),
                    (ORDER_DELIVERED, "ORDER_DELIVERED"),
                    )
    order_status= models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)

    # a single customer can have multiple orders (for example, if they start a new order after completing an old one without checking out).
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders',null=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# an order can have multiple OrderedItems
class OrderedItem(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    #a single Product may be present as many OrderedItems (ie; an order can have multiple copies of same product as OrderedItem)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,related_name='added_carts',null=True)
    quantity = models.IntegerField(default=1)
    #a single order contains multiple orderedItems
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
