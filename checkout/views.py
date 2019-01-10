from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Make_payment_form, OrderForm
from django.conf import settings
import stripe

stripe_api_key = settings.STRIPE_SECRET
 
@login_required()
def checkout(request):

    context = {
        'Make_payment_form' : Make_payment_form,
        'OrderForm' : OrderForm,
    }
    return render(request, "checkout.html", context)

