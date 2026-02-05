from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile


# Récupération du modèle User personnalisé
User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage du modèle User
    dans l'interface d'administration Django.
    """

    # Champs affichés dans la liste des utilisateurs
    list_display = (
        'last_name',
        'first_name',
        'email',
        'classe',
        'is_staff',
        'is_active'
    )

    # Champs utilisables pour la recherche dans l'admin
    search_fields = ('email', 'first_name', 'last_name')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Configuration de l'affichage du modèle Profile
    dans l'interface d'administration Django.
    """

    # Champs affichés dans la liste des profils
    list_display = ('nom_complet', 'bio', 'avatar', 'ecole')

    # Champs utilisables pour la recherche dans l'admin
    search_fields = ('first_name', 'last_name', 'ecole')

    def nom_complet(self, obj):
        """
        Retourne le nom complet de l'utilisateur lié au profil.
        """
        return f"{obj.user.first_name} {obj.user.last_name}"
