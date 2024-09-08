from django import forms
from .models import Teacher,Event,Comment,Contact

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'image', 'job_title', 'subject', 'bio', 'facebook', 'twitter', 'google_plus', 'linkedin']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'