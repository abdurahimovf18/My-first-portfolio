from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from . import services
from .forms import ContactForm, ReviewForm
from .models import ContactModel, ReviewModel


class HomePageView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["info"] = services.get_current_info()
        data["skill_categories"] = services.get_skill_categories()
        data["reviews"] = services.get_reviews()

        return data


class CreateContactView(CreateView):
    form_class = ContactForm
    model = ContactModel
    success_url = reverse_lazy("pages:home")


class CreateReviewView(CreateView):
    form_class = ReviewForm
    model = ReviewModel
    success_url = reverse_lazy("pages:home")
