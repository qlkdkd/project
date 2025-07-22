from django.shortcuts import render, redirect
from .models import Item, Transaction
# Create your views here.

#홈페이지
def homepage(request):
    return render(request, 'inventory/home.html')

#재고 목록
def inventory_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/list.html', {'items': items})

#재고 추가
def add_stock(request, item_id):
    item = Item.objects.get(id=item_id)
    item.quantity += 1
    item.save()
    return redirect('inventory_list')

#재고 제거
def remove_stock(request, item_id):
    item = Item.objects.get(id=item_id)
    if item.quantity > 0:
        item.quantity -= 1
        item.save()
    return redirect('inventory_list')

#재무
def transaction_list(request):
    transactions = Transaction.objects.order_by('-date')
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expense')
    balance = total_income - total_expense

    return render(request, 'inventory/finance.html', {
        'transactions': transactions,
        'income': total_income,
        'expense': total_expense,
        'balance': balance,
    })

#직원
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all().order_by('department', 'position')
    return render(request, 'inventory/employees.html', {'employees': employees})
