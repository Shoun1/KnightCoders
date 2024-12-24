from django import forms

class AdmissionForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    fathername = forms.CharField(max_length=255, required=True)
    mothername = forms.CharField(max_length=255, required=True)
    mobile_number = forms.CharField(max_length=15, required=True)
    email=forms.EmailField(max_length=100,required=True)
    jee_marks = forms.IntegerField()
    country = forms.CharField(max_length=25,required=True)
    city = forms.CharField(max_length=25,required=True)
    state = forms.CharField(max_length=25,required=True)
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)