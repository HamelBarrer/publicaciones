from django import forms

from .models import (
    Post,
    Commentary,
)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'image'
        )
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'image': 'Imagen',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'materialize-textarea',
                }
            )
        }


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = (
            'commentary',
        )
        labels = {
            'commentary': 'Comentario',
        }
