from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from notifications.models import Notification
from .models import Like

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        receiver = post.author
        sender_user = instance.user

        if receiver != sender_user:
            Notification.objects.create(
                receiver=receiver,
                sender=sender_user,
                notification_type='comment',
                post=post
            )


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        receiver = post.author
        sender_user = instance.user

        if receiver != sender_user:
            Notification.objects.create(
                receiver=receiver,
                sender=sender_user,
                notification_type='like',
                post=post,
                message=f"{sender_user.first_name} {sender_user.last_name} a aimé votre post."

            )
