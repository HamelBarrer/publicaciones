from django import forms

from .models import Post


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
