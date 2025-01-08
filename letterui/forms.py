from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class LatexLetterForm(forms.Form):
    sender_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field ', 'placeholder': 'Name'}))
    sender_streetaddress = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field ', 'placeholder': 'Street and Number'}))
    sender_zipcity = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field ', 'placeholder': 'Zip Code and City'}))
    sender_phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field ', 'placeholder': 'Phone Number'}))
    sender_phonename = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field ', 'placeholder': 'Phone Name'}))
    sender_email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control input-field ', 'placeholder': 'Email'}))
    business_yourref = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field '}))
    business_yourmailfrom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field '}))
    business_customernumber = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field '}))
    business_invoicenumber = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field '}))
    business_place = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field '}))
    recipient_addrfield = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control input-field ', 'placeholder': 'Receiver'}))
    content_subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field subject-field', 'placeholder': 'Subject'}))
    content_opening = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field', 'placeholder': 'Opening'}))
    content_text = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control input-field content-field', 'placeholder': 'Text...'}))
    content_closing = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field', 'placeholder': 'Closing'}))
    content_ps = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field', 'placeholder': 'PS'}))
    content_enclosing = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field', 'placeholder': 'Enclosing'}))
    content_cc = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control input-field', 'placeholder': 'CC'}))

    