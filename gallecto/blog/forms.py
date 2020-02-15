from django import forms
from .models import Comment

class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment