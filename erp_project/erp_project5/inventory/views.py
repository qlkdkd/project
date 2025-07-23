from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Transaction, Employee, Partner, StockTransaction
from .forms import EmployeeForm, PartnerForm, StockTransactionForm
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

#거래처 리스트
def partner_list(request):
    keyword = request.GET.get('keyword', '')
    partners = Partner.objects.all()
    if keyword:
        partners = partners.filter(name__icontains=keyword)
    return render(request, 'inventory/partner_list.html', {'partners': partners, 'keyword': keyword})

def partner_add(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'inventory/partner_form.html', {'form': form})

def partner_edit(request, partner_id):
    partner = get_object_or_404(Partner, id=partner_id)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'inventory/partner_form.html', {'form': form, 'partner': partner})

# 입출고
def stock_transaction_list(request):
    transactions = StockTransaction.objects.all().order_by('-date')
    return render(request, 'inventory/stock_transactions.html', {'transactions': transactions})

def stock_transaction_add(request):
    if request.method == 'POST':
        form = StockTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            transaction.apply_to_inventory()
            return redirect('stock_transaction_list')
    else:
        form = StockTransactionForm()
    return render(request, 'inventory/stock_transaction_form.html', {'form': form})