"""
Database model for Speed Feed app.
"""
import uuid
from django.db import models
from django.utils import timezone

class Address(models.Model):
    """
    Represents addresses.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.TextField(null=False)

class Restaurant(models.Model):
    """
    Represents restaurants.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    photo = models.CharField(max_length=512)
    rating = models.DecimalField(1,2)
    currency = models.CharField(max_length=5, null=False)

class Customer(models.Model):
    """
    Represents customers.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False)
    billing_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    photo = models.CharField(max_length=512)

class Contractor(models.Model):
    """
    Represents contractors.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    photo = models.CharField(max_length=512, null=False)
    rating = models.DecimalField(1,2, null=False)
    ein = models.DecimalField(9, null=False)

class MenuItem(models.Model):
    """
    Represents menu items.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=128, null=False)
    photo = models.CharField(max_length=512)
    description = models.TextField()
    cost = models.DecimalField(1,2, null=False)

class Order(models.Model):
    """
    Represents orders.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    delivery_fee = models.DecimalField(1,2, null=False)
    currency = models.CharField(max_length=5, null=False)

class OrderEvent(models.Model):
    """
    Represents order events.
    """
    class EventType(models.IntegerChoices):
        """
        Enumerator representing the type of event logged.
        """
        CREATED = 1
        ACCEPTED = 2
        ABANDONED = 3
        PICKED_UP = 4
        DELIVERED = 5
        DISPUTED = 6
        RESOLVED = 7
        ARCHIVED = 8

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, null=False, editable=False)
    event_type = models.IntegerField(choices=EventType, null=False)
    photo = models.CharField(max_length=512)

class ItemInOrder(models.Model):
    """
    Junction table representing which items are in which orders.
    """
    class AddedBy(models.IntegerChoices):
        """
        Enumerator representing how an item was added to the order.
        """
        ORIGINAL = 1
        SUBSTITUTION = 2

    pk = models.CompositePrimaryKey("item_id", "order_id")
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    added_by = models.IntegerField(choices=AddedBy, null=False)
