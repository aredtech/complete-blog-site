from re import template
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from .models import Post, ContactMe
from .forms import ContactMeForm, RegistrationForm
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
class RegisterPageView(FormView):
    template_name = "blog/register.html"
    fields = "_all_"
    form_class = RegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = "blog/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("index")

class IndexListView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

class PostDetailView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context

class ContactMeView(CreateView):
    model = ContactMe
    form_class = ContactMeForm
    template_name = "blog/contact_me.html"
    success_url = "/thank-you-for-messaging-us/"


class ThankYouView(TemplateView):
    template_name = "blog/thanks_for_message.html"

class AboutMeView(TemplateView):
    template_name = "blog/aboutme.html"
    

