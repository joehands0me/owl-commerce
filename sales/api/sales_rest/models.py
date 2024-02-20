from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField


class ProductVO(models.Model):
    item_number = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.PositiveSmallIntegerField()
    stock = models.PositiveSmallIntegerField()


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    contact_number = PhoneNumberField()
    address = AddressField(related_name="billing_address")
    shipping_address = AddressField(related_name="shipping_address")
