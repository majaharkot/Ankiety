class UserLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login",
        max_length=20,
        widget=forms.TextInput()
    )