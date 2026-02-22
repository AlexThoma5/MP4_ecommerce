from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    """
    Renders the contact page with the instance
    of :form:`contact.ContactForm`.
    **Context**
    ``contact_form``
        An instance of :form:`contact.ContactForm`.
    **Template**
        :template:`contact/contact.html`
    """
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            # Send email here
            messages.success(request,
                             "Your message has been received!"
                             " We will aim to respond within 3 days")
            return redirect('contact')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form,
        }

    return render(request, "contact/contact.html", context)
