from django import forms
from .models import Post,Comment,Tag
from django.forms import ModelMultipleChoiceField, ChoiceField, Form
class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
            queryset=Tag.objects.all(),
            widget = forms.CheckboxSelectMultiple
        )
    class Meta:
        model = Post
        fields =('title','text','tags')
    
   


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields =('author','text',) 