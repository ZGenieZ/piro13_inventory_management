from django.shortcuts import get_object_or_404,render,redirect
from .models import Item,Accounter
from .forms import ItemForm,AccounterForm
import json
from django.http import HttpResponse

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

def item_new(request,item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm(instance=item)
    
    return render(request,'item_new.html',{
        'form' : form,
    })

def item_edit(request, pk):
    item = get_object_or_404(Item,pk=pk)
    return item_new(request,item)

def item_detail(request, pk):
    item = get_object_or_404(Item,pk=pk)
    return render(request,'item_detail.html',{
        'item': item,
    })

def item_delete(request, pk):
    item = get_object_or_404(Item,pk=pk)
    item.delete()
    return redirect('shop:item_list')


def account_new(request,account=None):
    if request.method == 'POST':
        form = AccounterForm(request.POST,instance=account)
        if form.is_valid():
            account = form.save()
            return redirect(account)
    else:
        form = AccounterForm(instance=account)
    
    return render(request,'account_new.html',{
        'form' : form,
    })
    
def account_edit(request, pk):
    account = get_object_or_404(Accounter,pk=pk)
    return account_new(request,account)

def find_item(account):
    items = Item.objects.all()
    for item in items:
        if str(item.account) == str(account.name):
            return item   

def account_detail(request, pk):
    account = get_object_or_404(Accounter,pk=pk)
    item = find_item(account)  
    return render(request,'account_detail.html',{
        'account': account,
        'item':item,
    })

def account_delete(request, pk):
    account = get_object_or_404(Accounter,pk=pk)
    account.delete()
    return redirect('shop:account_list')

def ajax_plus(request):
    if request.is_ajax():
        data = int(request.GET['number']) + 1 
        item_instance = Item.objects.get(pk=request.GET['pk'])
        item_instance.amount = data
        item_instance.save()
        return HttpResponse(json.dumps({'data':data}),'application/json')

def ajax_minus(request):
    if request.is_ajax():
        data = int(request.GET['number']) - 1 
        item_instance = Item.objects.get(pk=request.GET['pk'])
        item_instance.amount = data
        item_instance.save()
        return HttpResponse(json.dumps({'data':data}),'application/json')