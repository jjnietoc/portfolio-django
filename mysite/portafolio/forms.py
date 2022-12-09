from .models import Portfolio
from django import forms

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"

