from django import forms
from .models import Rating

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('value',)
        labels = {
            'value': 'Rating (1-5)',
        }
        widgets = {
            'value': forms.Select(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))),
        }