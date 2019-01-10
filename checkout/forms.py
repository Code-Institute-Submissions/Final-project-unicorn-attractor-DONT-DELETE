from django import forms
from .models import Order

class Make_payment_form(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1,13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = {
            'full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2'
        }