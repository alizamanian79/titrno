from django import forms  
from .models import Contact  , New

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'
        exclude=['slug']