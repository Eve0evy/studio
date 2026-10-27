from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import FormView, TemplateView
from .forms import ContactForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html" 


from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm

class HomeView(FormView):
    form_class = ContactForm
    template_name = "index.html"  # dein Template mit den Includes
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        d = form.cleaned_data
        body = (
            f"Name: {d['name']}\n"
            f"Firma: {d['company']}\n"
            f"E-Mail: {d['email']}\n"
            f"Telefon: {d['phone']}\n\n"
            f"{d['message']}"
        )
        EmailMessage(
            subject=f"Neue Anfrage von {d['name']}",
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_RECIPIENT],
            reply_to=[d["email"]],
        ).send()
        messages.success(self.request, "Danke! Wir melden uns bald bei dir.")
        return super().form_valid(form)
    form_class = ContactForm
    template_name = "index.html"
    success_url = reverse_lazy("home:home")
