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
