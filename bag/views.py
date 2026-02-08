from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from services.models import Service
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
        messages.success(request, f'<strong>{service.name}</strong><br>Added to your bag')
    else:
        messages.info(request, f'<strong>{service.name}</strong><br>Is already in your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove the service item from the shopping bag """

    service = get_object_or_404(Service, pk=item_id)
    bag = request.session.get('bag', {})

    bag.pop(item_id, None)
    messages.success(request, f'<strong>{service.name}</strong><br>Has been removed from bag')

    request.session['bag'] = bag

    return redirect('view_bag')
