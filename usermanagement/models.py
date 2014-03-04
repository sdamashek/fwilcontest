from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    entry_type = "customer"

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Category(models.Model):
    name = models.CharField(max_length=50)
    entry_type = "category"

    def __unicode__(self):
        return self.name


class Item(models.Model):
    price = models.DecimalField(max_digits=16, decimal_places=2)
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    entry_type = "item"

    def __unicode__(self):
        return "%s" % (self.name)
