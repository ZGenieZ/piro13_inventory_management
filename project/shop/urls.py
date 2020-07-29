from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.item_list,name='item_list'),   
    path('item/new/',views.item_new,name='item_new'),   
    path('item/<int:pk>/',views.item_detail,name='item_detail'),   
    path('item/<int:pk>/edit/',views.item_edit,name='item_edit'),   
    path('item/<int:pk>/delete/',views.item_delete,name='item_delete'),   
    path('account/',views.account_list,name='account_list'),   
    path('account/new',views.account_new,name='account_new'),   
    path('account/<int:pk>/',views.account_detail,name='account_detail'),   
    path('account/<int:pk>/edit',views.account_edit,name='account_edit'),   
    path('account/<int:pk>/delete',views.account_delete,name='account_delete'),   
]