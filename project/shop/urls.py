from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.item_list,name='item_list'),   
    path('account/',views.account_list,name='account_list'),   
]