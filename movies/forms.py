from urllib import request
from django import forms
from django.contrib.auth import get_user_model

from movies.models import Movie

User = get_user_model()


class MovieForm(forms.ModelForm):
    created_by = forms.ModelChoiceField(
        User.objects.all(),
        widget=forms.HiddenInput(),
    )
    

    class Meta:
        model = Movie
        fields = ["name", "plot", "created_by"]
