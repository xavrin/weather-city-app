from django import forms
from django.core import validators
from main_app import countries_api

alpha = validators.RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')

class SearchForm(forms.Form):
    country = forms.CharField(max_length=50, validators=[alpha])

    def clean_country(self):
        country = self.cleaned_data['country']
        if not countries_api.is_country_valid(country):
            raise forms.ValidationError("Invalid country name")
        return country
