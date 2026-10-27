from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm

reihen = [
    [   
        {"breite": "m4", "bilder": [
            {"bild": "media/A.jpg", "hoehe": "medium-height", "titel": "Fitnessstudio", "text": "Da sieht man etwas"},
            {"bild": "media/F.jpg", "hoehe": "large-height", "titel": "Tancend", "text": "Jesnon wurde immernoch nicht auf ein Bier eingeladen"},
            
                    {"bild": "media/E.jpg", "hoehe": "small-height", "titel": "Abiball", "text": "Der Bre hat hoffentlich das abi bestanden"},
        ]},
        {"breite": "m8", "bilder": [
            {"bild": "media/G.jpg", "hoehe": "large-height", "titel": "Matti", "text": "Aura farming"},
            
            {"bild": "media/B.jpg", "hoehe": "large-height", "titel": "Total krasses Studio", "text": "sehr proffesionelle Arbeit"},
        ]},
    ],
    [   
        {"breite": "m4", "bilder": [
                ]},
        {"breite": "m4", "bilder": [
            {"bild": "media/C.jpg", "hoehe": "full-height", "titel": "Sänger", "text": "War das ein typ von Electric Callboy?"},
        ]},
        {"breite": "m4", "bilder": [
                            {"bild": "media/D.png", "hoehe": "large-height", "titel": "Skincare", "text": "High quality skincare producte"},
                ]},
        
        
    ],

]

# Create your views here.

class HomeView(FormView):
    form_class = ContactForm
    template_name = "index.html"
    success_url = reverse_lazy("home:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reihen"] = reihen
        return context

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
# views.py
