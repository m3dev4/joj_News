from django import forms
from .models import Commentaires  # ou Commentaire selon votre version

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaires
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Écrivez votre commentaire...'
            })
        }