from article.models import Commentaires
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=Commentaires)
def notif_admin(sender, instance, created, **kwargs):
    if created:
        sujet = "Nouveau commentaire"
        message = f"Un nouveau commentaire a été ajouté par {instance.auteur.username} sur l'article {instance.article.titre}"

        send_mail(
            sujet,
            message,
            "no-reply@monsite.com",
            ["admin@monsite.com"],
            fail_silently=False,
        )
