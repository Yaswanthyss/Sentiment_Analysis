from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    mobile_number = forms.CharField(label='Mobile Number', max_length=15)
