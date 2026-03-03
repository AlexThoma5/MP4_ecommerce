from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    Display and allow editing of the current user's profile.

    Handles GET and POST requests:
    - GET: Display the user's profile form pre-filled with existing data.
    - POST: Validate and save updates to the user's profile, providing success
    or error messages.

    **Context**

    ``form``
        An instance of :form:`profiles.UserProfileForm` bound to the current
        user's profile.
    ``orders``
        All orders associated with the user's profile.

    **Template:**

    :template:`profiles/profile.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your details have been updated!')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    """
    Display a past order confirmation for a given order number.

    Retrieves the specified :model:`checkout.Order` and shows
    the checkout success page with a message indicating
    that this is a historical confirmation.

    **Context**

    ``order``
        The :model:`checkout.Order` instance corresponding to ``order_number``.
    ``from_profile``
        Boolean flag indicating the view was accessed from the user's profile.

    **Template:**

    :template:`checkout/checkout_success.html`
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
