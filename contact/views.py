from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from .models import CompanyDetails


def contact_view(request):
    """
    Renders the contact page with the instance
    of :form:`contact.ContactForm` and the latest
    instance of :model:`contact.CompanyDetails`.
    **Context**
    ``contact_form``
        An instance of :form:`contact.ContactForm`.
    ``company_details``
        The most recently updated instance of
        :model:`contact.CompanyDetails`.
    **Template**
        :template:`contact/contact.html`
    """
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            instance = contact_form.save()
            send_mail(
                subject='Thanks for contacting us!',
                message=f'Hi {instance.full_name},\n\n'
                        f'Thanks for reaching out. We have received your '
                        f'message and will respond within 3 days.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=False,
            )
            messages.success(
                request,
                "Your message has been received! "
                "We will aim to respond within 3 days"
            )
            return redirect('contact')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        company_details = CompanyDetails.objects.all().order_by(
            '-updated_on').first()
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form,
        "company_details": company_details,
        }

    return render(request, "contact/contact.html", context)
