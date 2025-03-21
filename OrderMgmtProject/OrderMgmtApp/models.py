from django.db import models
from datetime import date

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=25, default='', null=False)
    last_name = models.CharField(max_length=25, default='', null=False)
    customer_since = models.DateField(default=date.today(), null=False)
    prime_customer = models.CharField(max_length=1, default='N', null=False)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    street = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, null=False)
    zipcode = models.CharField(max_length=10, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        ordering = ['street', 'city', 'state', 'zipcode']

    def __str__(self):
        return self.street + " - " + self.city


class Order(models.Model):
    order_number = models.IntegerField(null=False)
    order_date = models.DateField(default=date.today(), null=False)
    order_total = models.FloatField(default=0, null=False)
    payment_type = models.CharField(max_length=1, null=False)
    account_number = models.CharField(max_length=20, null=False)
    expiration_date = models.DateField(default=date.today(), null=False)
    #expiration_date = models.DateField(default=date.today().year + 1, null=False)  # DateAdd(Today(),1,Years)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        ordering = ['order_number']

    def __str__(self):
        return str(self.order_number)


class OrderItem(models.Model):
    item_description = models.CharField(max_length=25, null=False)
    item_quantity = models.IntegerField(null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')

    class Meta:
        ordering = ['item_description']

    def __str__(self):
        return (self.item_description)

