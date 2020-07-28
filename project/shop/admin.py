from django.contrib import admin
from .models import Accounter,Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['title','content']
    list_display_links=['title']
    search_fields = ['title']

@admin.register(Accounter)
class AccounterAdmin(admin.ModelAdmin):
    list_display=['name','call']
    list_display_links=['name']
    search_fields = ['name']
