from django import forms

class Contact(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    subject=forms.CharField(max_length=500)
    message = forms.CharField(widget=forms.Textarea)