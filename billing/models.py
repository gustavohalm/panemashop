from django.contrib.auth.models import User
from django.db import models

# Create your models here
from portal.models import Product


class Order(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='order_user')
    merchant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_merchant')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_product')
    commission = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    creat_at = models.DateField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Refused', 'Refused'),
        ('Pendind', 'Pending'),
        ('Aproved', 'Aproved')
    )
    SHIPMENT_STATUS_CHOIES = (
        ('Packing', 'Packing'),
        ('Pendind', 'Pending'),
        ('Posted', 'Posted'),
        ('Delivered', 'Delivered')
    )
    status = models.CharField(choices=STATUS_CHOICES, default='Pending',max_length=58)
    shipment = models.CharField(choices=SHIPMENT_STATUS_CHOIES, default='Pending' , max_length=58)

    def __str__(self):
        return '#' + str( self.id )

