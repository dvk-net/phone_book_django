from django import forms

from .models import Persone


class CreatePersoneForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Persone
        fields = [
            'name',
            'phones'
        ]