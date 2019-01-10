from django.shortcuts import render, reverse, redirect, get_object_or_404

def view_cart(request):
    """
    View all items in your cart
    """

    return render(request, "cart.html")

def add_to_cart(request, id):
    """ 
    Add a feature to your shopping cart
    """
    quantity = 1
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart

    return redirect(reverse('home'))

def delete_cart(request, id):
    cart = request.session.get('cart', {})
    if id in cart:
        cart.pop(id)
        
    request.session['cart'] = cart

    return redirect(reverse(view_cart))
