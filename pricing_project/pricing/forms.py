from django import forms
from .models import PricingConfig

DAYS_OF_WEEK = [
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
]

class PricingConfigForm(forms.ModelForm):
    days_active = forms.MultipleChoiceField(
        choices=DAYS_OF_WEEK,
        widget=forms.CheckboxSelectMultiple,
        help_text="Select days this config is active"
    )

    class Meta:
        model = PricingConfig
        fields = '__all__'

    def clean_base_distance(self):
        value = self.cleaned_data['base_distance']
        if value <= 0:
            raise forms.ValidationError("Base distance must be greater than 0.")
        return value

    def clean_base_price(self):
        value = self.cleaned_data['base_price']
        if value < 0:
            raise forms.ValidationError("Base price cannot be negative.")
        return value
