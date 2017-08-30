from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Post, Category
from datetime import datetime
from tinymce.widgets import TinyMCE

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class PostForm(forms.ModelForm):
    title = forms.CharField(max _length=50, required=True)
    category = forms.ChoiceField(choices=[x for x in Category.objects.all()], required=True)
    contents = forms.CharField(widget=TinyMCE(), required=True)
    time_updated = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ['title', 'category', 'contents', 'time_updated']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [('', 'Please choose the category.'),] + list(self.fields['category'].choices)[1:]


