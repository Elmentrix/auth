from django import forms

class Resgister(forms.Form):
    first_name = forms.CharField(label="First Name")
    middle_name = forms.CharField(label="Middle Name")
    last_name = forms.CharField(label="Last Name")
    gender = forms.CharField(label='Gender')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    contact = forms.CharField(label='Contact')
    country = forms.CharField(label='Country')
    zipcode = forms.CharField(label='Zip Code')