from django.contrib import admin
from .models import Item, Transaction, Employee, Partner

admin.site.register(Item)
admin.site.register(Transaction) 
admin.site.register(Employee)
admin.site.register(Partner)