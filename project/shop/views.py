from django.shortcuts import render
from .models import Item,Accounter

def item_list(request):
    items = Item.objects.all()
    return render(request,'item_list.html',{
        'items' : items,
    })

def account_list(request):
    accounts = Accounter.objects.all()
    return render(request,'account_list.html',{
        'accounts' : accounts
    })