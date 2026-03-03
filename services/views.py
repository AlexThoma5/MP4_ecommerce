from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Service
from .forms import ServiceForm


# Create your views here.
def all_services(request):
    """
    Display services page with all :model:`services.Service` objects,
    grouped by service type.

    **Context**

    ``services``
        All instances of :model:`services.Service`.
    ``initial_services``
        All initial appointment services.
    ``follow_up_services``
        All follow-up appointment services.
    ``package_services``
        All package deal services.
    ``treatment_services``
        All treatment services.
    ``service_form``
        An instance of :form:`services.ServiceForm`


    **Template:**

    :template:`services/services.html`
    """

    services = Service.objects.all()

    initial_services = services.filter(service_type=1)
    follow_up_services = services.filter(service_type=2)
    package_services = services.filter(service_type=3)
    treatment_services = services.filter(service_type=4)

    service_form = ServiceForm()

    context = {
        "services": services,
        "initial_services": initial_services,
        "follow_up_services": follow_up_services,
        "package_services": package_services,
        "treatment_services": treatment_services,
        'service_form': service_form,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """
    Display an individual :model:`services.Service`.

    **Context**

    ``service``
        An instance of :model:`services.Service`.
    ``on_service_detail_page``
        Boolean flag indicating the service detail page is being rendered.
        Used to provide context to toasts.

    **Template:**

    :template:`services/service_detail.html`
    """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
        'on_service_detail_page': True,
    }

    return render(request, 'services/service_detail.html', context)


@login_required
def add_service(request):
    """
    Allow the superuser to add a new :model:`services.Service`.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added service!')
        else:
            messages.error(
                request, 'Failed to add service.'
                ' Please ensure the form is valid.')

    return redirect('services')


@login_required
def edit_service(request, service_id):
    """
    Allow superuser to edit an existing service
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    service = get_object_or_404(Service, pk=service_id)

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            redirect('services')
        else:
            messages.error(
                request,
                'Failed to update service. Please ensure the form is valid.')

    return redirect('services')


@login_required
def delete_service(request, service_id):
    """ Delete a service from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('home')

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Deleted service!')
    return redirect('services')
