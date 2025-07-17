from django.shortcuts import render, redirect
from .models import Item
# Create your views here.

def inventory_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/list.html', {'items': items})


def add_stock(request, item_id):
    item = Item.objects.get(id=item_id)
    item.quantity += 1
    item.save()
    return redirect('inventory_list')

def remove_stock(request, item_id):
    item = Item.objects.get(id=item_id)
    if item.quantity > 0:
        item.quantity -= 1
        item.save()
    return redirect('inventory_list')