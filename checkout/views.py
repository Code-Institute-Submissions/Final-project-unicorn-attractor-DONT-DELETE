from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from feature.models import Feature
import stripe

stripe.api_key = settings.STRIPE_SECRET
 
@login_required()
def checkout(request):
    
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():

            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            
            for id, quantity in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                total += quantity * feature.price
                order_line_item = OrderLineItem(
                    order = order,
                    feature = feature,
                    quantity = quantity
                    )
                order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )

            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                messages.success(request, "Your order has been completed, Thank you")

                for id, quantity in cart.items():
                    feature = get_object_or_404(Feature, pk=id)
                    feature.purchased += 1  
                    feature.save()

                request.session['cart'] = {} 
                return redirect(reverse("profile"))

            else:
                messages.alert(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Unable to take payment from card! ")
    else:
        MakePaymentForm(),
        OrderForm()
        
    context = {
        'payment_form' : MakePaymentForm(),
        'order_form' : OrderForm(),
        'publishable' : settings.STRIPE_PUBLISHABLE,
    }


    return render(request, "checkout.html", context)
