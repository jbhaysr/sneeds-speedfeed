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
    location = models.TextField()

    def __str__(self):
        return f"{self.location}"

class Restaurant(models.Model):
    """
    Represents restaurants.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    photo = models.CharField(max_length=512, null=True, blank=True)
    rating = models.DecimalField(max_digits=3,decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name}, {self.rating}/10" if self.rating else f"{self.name}"

class Customer(models.Model):
    """
    Represents customers.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    billing_address = models.ForeignKey(Address, related_name='customer_billing_address', on_delete=models.CASCADE, null=True, blank=True)
    delivery_address = models.ForeignKey(Address, related_name='customer_delivery_address', on_delete=models.CASCADE, null=True, blank=True)
    photo = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Contractor(models.Model):
    """
    Represents contractors.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    photo = models.CharField(max_length=512)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    ein = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}, {self.rating}/10"

class MenuItem(models.Model):
    """
    Represents menu items.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    photo = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name}, {self.cost} {self.restaurant.currency}"

class Order(models.Model):
    """
    Represents orders.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True)
    billing_address = models.ForeignKey(Address, related_name='order_billing_address', on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(Address, related_name='order_delivery_address', on_delete=models.CASCADE)
    delivery_fee = models.DecimalField(max_digits=3, decimal_places=2)
    currency = models.CharField(max_length=5)
    items = models.ManyToManyField(MenuItem, through='ItemInOrder')

    def __str__(self):
        return f"Order {self.id} from {self.customer.name}"

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
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    event_type = models.IntegerField(choices=EventType)
    photo = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f"[OrderEvent] {self.order} has had event {self.event_type} {self.photo}"

class ItemInOrder(models.Model):
    """
    Junction table representing which items are in which orders.
    
        def __str__(self):
            return f""
    """
    class AddedBy(models.IntegerChoices):
        """
        Enumerator representing how an item was added to the order.
        """
        ORIGINAL = 1
        SUBSTITUTION = 2

    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    added_by = models.IntegerField(choices=AddedBy)

    def __str__(self):
        return f"Order {self.order} contains {self.item.name}"
