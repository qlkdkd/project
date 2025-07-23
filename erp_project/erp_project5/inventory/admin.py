from django.contrib import admin
from .models import Item, Transaction, Employee, Partner, StockTransaction

admin.site.register(Item)
admin.site.register(Transaction) 
admin.site.register(Employee)
admin.site.register(Partner)
admin.site.register(StockTransaction)