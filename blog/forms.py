from django import forms
from .models import Post


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