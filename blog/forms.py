from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            "title",
            "category",
            "content",
            "image",
            'status',
        ]

        widget = {
            'title':forms.TextInput(attrs={"placeholder": "Enter your post title..."}),
            'content':forms.Textarea(attrs={"placeholder": "Write your post here..."}),
            "status": forms.Select(),
            "category": forms.Select(),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={"placeholder": "Write your comment...", "rows": 4}),
        }