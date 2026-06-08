from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'service', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Full Name'}),
            'email':   forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email Address'}),
            'phone':   forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}),
            'service': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Service Required'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Tell us about your project...', 'rows': 5}),
        }