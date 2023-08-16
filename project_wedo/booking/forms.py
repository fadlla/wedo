from django import forms

class ContactForm(forms.Form):
    wedding_id = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    customer_need = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    

class InquiryForm(forms.Form):
    wedding_id = forms.IntegerField()

