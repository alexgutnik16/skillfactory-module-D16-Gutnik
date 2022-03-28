from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Comment


@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    comment_author = instance.author_comment.username
    text = instance.text
    if created:
        subject = f'New comment from {comment_author}'
        to = instance.advert_comment.author.email
    else:
        if instance.accepted:
            subject = f'Your comment was accepted'
            to = instance.author_comment.email
        else:
            return
    send_mail(
        subject=subject,
        message=text,
        from_email='alexvgutnik@yandex.ru',
        recipient_list=[to],
    )
