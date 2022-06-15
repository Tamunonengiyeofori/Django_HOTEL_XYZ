# import form class from django
from django import forms

# import models from models.py
from .models import HotelRecord

#create a ModelForm class
class HotelRecordForm(forms.ModelForm):
    # specify model name to create form
    class Meta:
        model = HotelRecord
        fields = "__all__"