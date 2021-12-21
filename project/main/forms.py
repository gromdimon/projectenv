from django import forms
from .models import item_model

class ItemForm(forms.ModelForm):
    class Meta:
        model= item_model
        fields= ["name", "description", "price", "quantity"]