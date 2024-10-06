from django import forms

from .models import ContactModel, ReviewModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['image', 'full_name', 'address', 'rating', 'content']
