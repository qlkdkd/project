from django.db import models

#재고 데이터베이스
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

#재무 데이터베이스
class Transaction(models.Model):
    TYPE_CHOICES = (
        ('income', '수입'),
        ('expense', '지출'),
    )
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)
    amount = models.IntegerField()
    memo = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.category} : {self.amount}원"
    
from django.db import models

class Employee(models.Model):
    POSITION_CHOICES = [
        ('staff', '사원'),
        ('manager', '대리'),
        ('director', '과장'),
        ('executive', '임원'),
    ]
    
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    hire_date = models.DateField()
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_position_display()}, {self.department})"

#거래처
from django.db import models

class Partner(models.Model):
    TYPE_CHOICES = [
        ('customer', '고객'),
        ('supplier', '공급처'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

# 입출고 관리 
class StockTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('in', '입고'),
        ('out', '출고'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"[{self.get_transaction_type_display()}] {self.item.name} - {self.quantity}개"

    def apply_to_inventory(self):
        if self.transaction_type == 'in':
            self.item.quantity += self.quantity
        elif self.transaction_type == 'out':
            self.item.quantity -= self.quantity
        self.item.save()