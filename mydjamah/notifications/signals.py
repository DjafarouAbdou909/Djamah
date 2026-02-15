from django.db.models.signals import post_save
from django.dispatch import receiver
from publications.models import Comment
from .models import Notification

@receiver(post_save, sender=Comment)
def create_reply_notification(sender, instance, created, **kwargs):
    if created and instance.parent:
        parent_comment = instance.parent

        # éviter l'auto-notification
        if parent_comment.user != instance.user:
            Notification.objects.create(
                receiver=parent_comment.user,
                sender=instance.user,
                notification_type='comment',
                post=instance.post,
                message=f"{instance.user.first_name} a répondu à votre commentaire."
            )
