from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(models.Model):
    """
    Publication créée par un utilisateur.
    Peut contenir texte, image, PDF ou lien externe.
    """
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    content = models.TextField(verbose_name="Contenu")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    pdf = models.FileField(upload_to='post_pdf/', blank=True, null=True)
    url = models.URLField(blank=True, null=True, verbose_name="Lien externe")
    slug = models.SlugField(max_length=60, blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            # Génération automatique d'un slug lisible à partir du contenu
            self.slug = slugify(self.content[:50])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.content[:50]


class Like(models.Model):
    """
    Like d'un utilisateur sur un post.
    Un utilisateur ne peut liker un post qu'une seule fois.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user} aime {self.post.id}"


class Comment(models.Model):
    """
    Commentaire associé à un post.
    Supporte les réponses via une relation auto-référencée.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name="Commentaire")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user} : {self.content[:30]}"


class Repost(models.Model):
    """
    Repartage d'un post par un utilisateur.
    Un post ne peut être repartagé qu'une seule fois par utilisateur.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='reposts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'original_post')

    def __str__(self):
        return f"{self.user} a repartagé {self.original_post.id}"


