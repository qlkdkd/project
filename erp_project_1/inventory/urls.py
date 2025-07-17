from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/<int:item_id>/', views.add_stock, name='add_stock'),
    path('remove/<int:item_id>/', views.remove_stock, name='remove_stock'),
]
