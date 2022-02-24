from django import forms
from .models import ContactMe, UserProfile, Comment
from django.contrib.auth.forms import UserCreationForm

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = "__all__"

        labels = {
            "name" : "Your Name",
            "email" : "Your Email",
            "message" : "Your Message",
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required")

    class Meta:
        model = UserProfile
        fields = ["email", "name", "password1", "password2"]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["text"]

        labels = {
            "text" : "Comment"
        }

