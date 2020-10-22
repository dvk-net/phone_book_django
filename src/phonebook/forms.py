from django import forms

from .models import Persone, Phone


class CreatePersoneForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea(), help_text="separated by new line '\\n'")
    class Meta:
        model = Persone
        fields = [
            'name',
            'phones'
        ]