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
