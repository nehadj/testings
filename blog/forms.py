from django import forms
from .models import Post
from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.ModelForm):
    class Meta:
        # class meta is keyword which is data about data which contain data about data that is data about parent class 
        model=Post
        fields=('author_name','title','content','create_date','publish_date')

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')
