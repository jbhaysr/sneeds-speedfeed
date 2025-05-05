from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Contractor)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderEvent)
