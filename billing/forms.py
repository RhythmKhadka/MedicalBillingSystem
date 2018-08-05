from django import forms
from .models import Purchase

class AddPurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
