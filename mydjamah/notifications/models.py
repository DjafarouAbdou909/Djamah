from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('comment', 'Commentaires'),
        ('like', 'Like')
    )
    
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='notifications'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='sent_notifications'
    )
    notification_type = models.CharField(
        max_length=10, 
        
        choices=NOTIFICATION_TYPES
    )
    post = models.ForeignKey(
        'publications.Posts', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def sender_name(self):
        return f"{self.sender.first_name} {self.sender.last_name}"
   
    
    class Meta:
        ordering = ['-created_at']  
    
    def __str__(self):
        return f"{self.sender} - {self.receiver} - {self.notification_type}"
    
    