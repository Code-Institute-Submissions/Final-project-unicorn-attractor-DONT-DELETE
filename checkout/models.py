from django.db import models
from feature.models import Feature
from django.contrib.auth.models import User


class Order(models.Model):
    full_name = models.CharField(
        max_length=50, blank=False)
    street_address1 = models.CharField(
        max_length=40, blank=False)
    street_address2 = models.CharField(
        max_length=40, blank=True)
    town_or_city = models.CharField(
        max_length=40, blank=False)
    country = models.CharField(
        max_length=50, blank=False)
    postcode = models.CharField(
        max_length=20, blank=True)
    phone_number = models.CharField(
        max_length=40, blank=False)
    date = models.DateField()
    customer_username = models.CharField(max_length=20, null=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(
            self.id, self.full_name, self.date)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,
                              null=False)
    feature = models.ForeignKey(Feature,
                                null=False)
    quantity = models.IntegerField(blank=False)
    purchased = models.ForeignKey(User, null=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity,
            self.feature.title,
            self.feature.price)
