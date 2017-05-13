from django import forms
from .models import Room

class ŔoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('room_title','room_location','room_description',)