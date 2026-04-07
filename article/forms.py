from django import forms
from .models import Commentaires  # ou Commentaire selon votre version
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaires
        fields = ["contenu"]
        widgets = {
            "contenu": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Écrivez votre commentaire...",
                }
            )
        }
