from django.shortcuts import render, reverse, redirect
from django.contrib import messages


def view_cart(request):
    return render(request, "cart.html")


def add_to_cart(request, id):
    if request.method == "POST":
        quantity = 1
        cart = request.session.get('cart', {})
        cart[id] = cart.get(id, quantity)
        request.session['cart'] = cart
        messages.success(request, "Basket Updated!")

        return redirect(reverse('home'))


def delete_cart(request, id):
    cart = request.session.get('cart', {})
    if id in cart:
        cart.pop(id)

    request.session['cart'] = cart
    messages.info(request,
                  "Item removed!")

    return redirect(reverse(view_cart))
