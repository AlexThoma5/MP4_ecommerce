from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('services'))

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout/checkout.html', context)
