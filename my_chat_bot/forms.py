from django import forms
from .models import genaiSetting


class ModelParametersForm(forms.ModelForm):
    class Meta:
        model = genaiSetting
        fields = ['temperture', 'max_length', 'top_p', 'top_k']

    temperture = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'type': 'range', 'min': 0, 'max': 1, 'step': 0.01}
        ),
        label="temperture"

    )

    top_p = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'type': 'range', 'min': 0, 'max': 1, 'step': 0.1}
        ),
        label="top_p"
    )

    top_k = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'type': 'range', 'min': 0, 'max': 1000, 'step': 1}
        ),
        label="top_k"
    )

    max_length = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'type': 'range', 'min': 0, 'max': 1000, 'step': 1}
        ),
        label="max_length"
    )
