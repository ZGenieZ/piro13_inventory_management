from django import forms
from .models import Item,Accounter

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class AccounterForm(forms.ModelForm):
    class Meta:
        model = Accounter
        fields = '__all__'