from xml.etree.ElementInclude import include
from django.urls import path
from  . import views


urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path("all-posts", views.AllPostsView.as_view(), name="all-posts"),
    path("thank-you-for-messaging-us/", views.ThankYouView.as_view()),
    path("all-posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail"),
    path("contact-me", views.ContactMeView.as_view(), name = "contact-me" ),
    path("about-me", views.AboutMeView.as_view(), name="about-me"),
]
