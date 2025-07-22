from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),                         # 루트 주소는 메인 화면
    path('inventory/', views.inventory_list, name='inventory_list'),   # 재고 페이지는 /inventory/
    path('add/<int:item_id>/', views.add_stock, name='add_stock'),
    path('remove/<int:item_id>/', views.remove_stock, name='remove_stock'),
    path('finance/', views.transaction_list, name='transaction_list'), # 재무 페이지는 /finance/
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_create, name='employee_add'),
    path('employees/<int:emp_id>/edit/', views.employee_update, name='employee_edit'),
    path('partners/', views.partner_list, name='partner_list'),
    path('partners/add/', views.partner_add, name='partner_add'),
    path('partners/<int:partner_id>/edit/', views.partner_edit, name='partner_edit'),


]