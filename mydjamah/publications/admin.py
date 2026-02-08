from django.contrib import admin
from .models import Posts, Comment, Like, Repost


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage des publications dans l'administration Django.
    Inclut colonnes visibles, filtres, champs recherchables et slug pré-rempli.
    """
    list_display = ('id', 'author', 'short_content', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    search_fields = ('content', 'author__email')
    prepopulated_fields = {'slug': ('content',)}
    ordering = ('-created_at',)

    def short_content(self, obj):
        """Aperçu du contenu pour l'affichage dans l'admin."""
        return obj.content[:40]

    short_content.short_description = "Contenu"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage des commentaires dans l'administration Django.
    Affiche la relation parent, le contenu et les filtres de date.
    """
    list_display = ('id', 'user', 'post', 'parent', 'short_content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'user__email')
    ordering = ('created_at',)

    def short_content(self, obj):
        """Aperçu du commentaire pour l'affichage dans l'admin."""
        return obj.content[:40]

    short_content.short_description = "Commentaire"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage des likes dans l'administration Django.
    Permet de visualiser qui a aimé quel post et quand.
    """
    list_display = ('user', 'post', 'created_at')
    search_fields = ('user__email',)
    list_filter = ('created_at',)


@admin.register(Repost)
class RepostAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage des repartages dans l'administration Django.
    Permet de visualiser les reposts et de filtrer par date.
    """
    list_display = ('user', 'original_post', 'created_at')
    search_fields = ('user__email',)
    list_filter = ('created_at',)

