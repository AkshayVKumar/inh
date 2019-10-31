from app.models import *
from django import forms

class from_demo(forms.ModelForm):
    class Meta:
        model=Model_img
        fields='__all__'