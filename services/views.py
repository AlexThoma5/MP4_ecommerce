from django.shortcuts import render
from .models import Service


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

    **Template:**

    :template:`services/services.html`
    """

    services = Service.objects.all()

    initial_services = services.filter(service_type=1)
    follow_up_services = services.filter(service_type=2)
    package_services = services.filter(service_type=3)
    treatment_services = services.filter(service_type=4)

    context = {
        "services": services,
        "initial_services": initial_services,
        "follow_up_services": follow_up_services,
        "package_services": package_services,
        "treatment_services": treatment_services,
    }

    return render(request, 'services/services.html', context)
