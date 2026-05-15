from article.models import Commentaires, Articles
from django.db.models.signals import post_save, pre_save    
from django.dispatch import receiver
from django.core.mail import send_mail
import ollama


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


@receiver(pre_save, sender=Articles)
def clear_resume_if__content_changed(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_article = Articles.objects.get(pk=instance.pk)
    except Articles.DoesNotExist:
        return
    
    if old_article.contenu != instance.contenu:
        instance.resume = None
        
        
@receiver(post_save, sender=Articles)
def generate_new_resume(sender, instance, created, **kwargs):
    if not instance.contenu:
        return
    
    if instance.resume:
        return
    
    content_limite = instance.contenu[:4000]
    prompt = f"Résume l'article suivant en quelques phrases : {content_limite}"
    response = ollama.chat(
        model="mistral", messages=[{"role": "user", "content": prompt}]
    )
    
    resume = response["message"]["content"]
    
    Articles.objects.filter(pk=instance.pk).update(resume=resume)