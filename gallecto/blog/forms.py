from django import forms
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(label="昵称", widget=forms.TextInput(attrs={"placeholder": "请输入昵称"}))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={"placeholder": "请输入邮箱"}))
    comment = forms.CharField(label="评论内容", widget=forms.Textarea(attrs={"rows": 4, "placeholder": "请输入评论内容"}))

    class Meta:
        model = Comment
