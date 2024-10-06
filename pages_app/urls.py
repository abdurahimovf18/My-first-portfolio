from django.urls import path
from . import views


app_name = "pages"


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("contact/", views.CreateContactView.as_view(), name="contact"),
    path("review/", views.CreateReviewView.as_view(), name="review"),
]
