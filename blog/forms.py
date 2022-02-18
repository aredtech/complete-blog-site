from django import forms
from .models import ContactMe

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = "__all__"

        labels = {
            "name" : "Your Name",
            "email" : "Your Email",
            "message" : "Your Message",
        }