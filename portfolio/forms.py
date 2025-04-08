from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email *'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'placeholder': 'Message *'}),
        }
