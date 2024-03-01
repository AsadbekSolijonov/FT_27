from django import forms

from blog_app.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'message']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', "rows": 3, "cols": 80, "placeholder": "Enter your message"})

        }
