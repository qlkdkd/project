from django.shortcuts import render, redirect
from .models import Item, Transaction, Employee
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404
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
def employee_list(request):
    department = request.GET.get('department', '')
    keyword = request.GET.get('keyword', '')

    employees = Employee.objects.all()
    if department:
        employees = employees.filter(department__icontains=department)
    if keyword:
        employees = employees.filter(name__icontains=keyword)

    return render(request, 'inventory/employees.html', {
        'employees': employees,
        'department': department,
        'keyword': keyword,
    })


# 직원 등록
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'inventory/employee_form.html', {'form': form})

# 직원 수정
def employee_update(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'inventory/employee_form.html', {'form': form, 'employee': employee})