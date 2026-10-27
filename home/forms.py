from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Vollständiger Name", max_length=150)
    company = forms.CharField(label="Firmenname", max_length=150, required=False)
    email = forms.EmailField(label="E-Mail")
    phone = forms.CharField(label="Telefonnummer", max_length=50)
    message = forms.CharField(
        label="Wie können wir helfen?",
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
    )