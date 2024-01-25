from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Blogpost,BlogComment



class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title','head0','chead0','head1','chead1','head2','chead2','thumbnail']


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment']