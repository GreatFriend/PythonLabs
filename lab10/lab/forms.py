from django import forms
from .models import Citizen


class Form(forms.ModelForm):

    class Meta:
        model=Citizen
        fields=(
            'name','age','place_reg'
            )
