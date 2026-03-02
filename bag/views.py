from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Service
from checkout.models import Discount
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a single service to the shopping bag """

    service = get_object_or_404(Service, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    quantity = 1

    if item_id not in bag:
        bag[item_id] = quantity
        messages.success(
            request, f'<strong>{service.name}</strong><br>Added to your bag'
        )
    else:
        messages.info(
            request,
            f'<strong>{service.name}</strong><br>Is already in your bag'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove the service item from the shopping bag """

    service = get_object_or_404(Service, pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id, None)
    messages.success(
        request,
        f'<strong>{service.name}</strong><br>Has been removed from bag'
    )

    request.session['bag'] = bag

    return redirect('view_bag')


def apply_discount_code(request):
    """Apply discount code and store in session"""

    if request.method == 'POST':
        code = request.POST.get('discount_code', '')

        if code:
            code = code.upper().strip()
        else:
            messages.error(request, "Invalid or inactive discount code.")
            return redirect('view_bag')

        try:
            # Gets object where code is a match and currently active
            discount = Discount.objects.get(code=code, active=True)
            # Store the PK-ID in session
            request.session['discount_id'] = discount.id
            messages.success(request, f"{discount.code} applied!")
        except Discount.DoesNotExist:
            messages.error(request, "Invalid or inactive discount code.")

    return redirect('view_bag')
