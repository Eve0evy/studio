from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm
from django.views.generic import TemplateView

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
        {"breite": "m4", "bilder": []},
        {"breite": "m4", "bilder": [
            {"bild": "media/C.jpg", "hoehe": "full-height", "titel": "Sänger", "text": "War das ein typ von Electric Callboy?"},
        ]},
        {"breite": "m4", "bilder": [
            {"bild": "media/D.png", "hoehe": "large-height", "titel": "Skincare", "text": "High quality skincare producte"},
        ]},
    ],
]

SERVICES = [
    {"img": "eins", "title": "Image-Filme & Support", "packages": [
        {"name": "Recruiting Spotlight", "price": "1.750,00", "items": [
            "1 Hauptfilm (60-90 Sek.)",
            "3 Social-Media-Clips (15-30 Sek.)",
            "15 bearbeitete Fotos",
            "1 Drehtag vor Ort (bis zu 4 Std.)",
        ]},
        {"name": "Imagefilm Compact", "price": "3.650,00", "items": [
            "1 Hauptfilm (90-150 Sek.)",
            "3-5 Kurzfassungen (15-60 Sek.)",
            "30 bearbeitete Fotos",
            "1 Drehtag vor Ort (bis zu 8 Std.)",
        ]},
        {"name": "Imagefilm Plus", "price": "5.250,00", "items": [
            "Mehrere maßgeschneiderte Fassungen (Messen/Kino/TV)",
            "50 bearbeitete Fotos",
            "2 Drehtage vor Ort (je 8 Std.)",
        ]},
        {"name": "Laufendes Content-Paket", "price": "1.350,00", "items": [
            "4-8 Social-Media-Assets pro Monat (je 15-60 Sek.)",
            "1 Drehtag vor Ort (bis zu 4 Std.)",
        ]},
    ]},
    {"img": "zwei", "title": "Artist Releases", "packages": [
            {"name": "Performance Video", "price": "1.340,00", "items": [
                "Volle Songlänge (2.5-4 Min.)",
                "3 Hochkant-Teaser (15-30 Sek.)",
                " 1 feste Location, 1 Drehtag (bis zu 6 Std.)",
            ]},
            {"name": "Imagefilm Compact", "price": "2.650,00", "items": [
                "Volle Songlänge inkl. Intro/Outro (3-5 Min.)",
                "3-5 Teaser-Clips",
                "20 bearbeitete Artist-Fotos",
                "Mehrere Sets/Locations, 1 Drehtag (bis zu 8 Std.)",
            ]},
            {"name": "Release Campaign", "price": "4.500,00", "items": [
                "1 Haupt-Musikvideo• 6-10 Shortform-Clips",
                "Umfassendes Presse- / Release-Fotopaket",
                "Mehrere Drehsessions",
            ]},
        ]},
    {"img": "drai", "title": "Event-Support", "packages": [
                {"name": "Event Essentials", "price": "910,00", "items": [
                    "240 bearbeitete Fotos (optimiert für Web & Social Media)",
                    "Ca. 2 Stunden Begleitung vor Ort",
                ]},
                {"name": "Event Compact", "price": "1.650,00", "items": [
                    "500 bearbeitete Fotos",
                    "2 Social-Media-Clips (je 15-30 Sek.)",
                    "Bis zu 4 Stunden Begleitung vor Ort",
                ]},
                {"name": "Event Premium", "price": "2.950,00", "items": [
                    "1000 bearbeitete Fotos",
                    "1 Event-Highlight-Film (60-90 Sek.)",
                    "2 Social-Media-Clips (je 15-30 Sek.)",
                    "Voller Einsatztag vor Ort (bis zu 8 Std.)",
                ]},
            ]},
    {"img": "vier", "title": "Individuell",
     "text": "Du brauchst kein Paket? Dein Wunschprojekt wird auch flexibel von uns umgesetzt und berechnet."},
]

class HomeView(FormView):
    form_class = ContactForm
    template_name = "index.html"
    success_url = reverse_lazy("home:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reihen"] = reihen
        context["services"] = SERVICES
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

class DatenschutzView(TemplateView):
    template_name = "datenschutz.html"

class ImpressumView(TemplateView):
    template_name = "impressum.html"