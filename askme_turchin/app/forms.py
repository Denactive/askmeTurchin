from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = form.CharField(request=False)


