from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'url', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }