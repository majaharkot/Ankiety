from django import form
from django.forms import ModelForm
from formularze.models import Pytanie

class UserLoginForm(forms.Form):
    login = forms.Charfield(
        label="Twój login",
        max_length=20,
        widget=forms.TextInput()
    )

class PytaniaForm(forms.Form):
    pytanie = forms.Charfield(
        label="Pytanie Ankiety",
        max_length=100,
        widget=forms.TextInput()
    )

class PytaniaModelForm(ModelForm):
    class Meta:
        model = Pytanie
        fields = ('pytanie',)