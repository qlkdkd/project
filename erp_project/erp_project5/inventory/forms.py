from django import forms
from .models import Employee, Partner, StockTransaction

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'position', 'hire_date', 'phone', 'email']

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'type', 'contact_person', 'phone', 'email', 'address']

class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ['item', 'partner', 'transaction_type', 'quantity', 'note']

