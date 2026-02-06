from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a single service to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    quantity = 1

    if item_id not in bag:
        bag[item_id] = quantity
        # message for successful addition to bag
        # else item already exists message

    request.session['bag'] = bag
    return redirect(redirect_url)
