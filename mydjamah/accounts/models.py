from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):
    """
    Manager personnalisé pour le modèle User
    utilisant l'adresse e-mail comme identifiant principal.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Crée et enregistre un utilisateur avec une adresse e-mail
        et un mot de passe.
        """
        if not email:
            raise ValueError("L'email est obligatoire")

        # Normalisation de l'adresse e-mail
        email = self.normalize_email(email)

        # Création de l'utilisateur
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crée et enregistre un superutilisateur avec
        toutes les permissions nécessaires.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Vérifications de sécurité
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superuser doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superuser doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Modèle utilisateur personnalisé basé sur AbstractUser
    avec suppression du champ username et utilisation de l'e-mail
    comme identifiant principal.
    """

    # Suppression du champ username par défaut
    username = None

    # Champ e-mail unique
    email = models.EmailField(unique=True)

    # Liste des niveaux scolaires / universitaires
    NIVEAU_STUDENT = [
        ('2ndeA', '2nde A'),
        ('2ndeC', '2nde C'),
        ('1ereA', '1ère A'),
        ('1ereC', '1ère C'),
        ('1ereD', '1ère D'),
        ('TleA', 'Terminale A'),
        ('TleC', 'Terminale C'),
        ('TleD', 'Terminale D'),
        ('L1_INFO', 'Licence 1 Informatique'),
        ('L2_INFO', 'Licence 2 Informatique'),
        ('L3_INFO', 'Licence 3 Informatique'),
    ]

    # Classe / niveau de l'utilisateur
    classe = models.CharField(
        max_length=20,
        choices=NIVEAU_STUDENT,
        blank=True
    )

    # Configuration de l'authentification par e-mail
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Association du manager personnalisé
    objects = UserManager()

    def __str__(self):
        """
        Représentation textuelle de l'utilisateur.
        """
        return f"{self.email}, {self.classe}, {self.last_name}, {self.first_name}"


class Profile(models.Model):
    """
    Modèle de profil lié à l'utilisateur
    pour stocker des informations complémentaires.
    """

    # Relation OneToOne avec le modèle User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Biographie de l'utilisateur
    bio = models.TextField(blank=True)

    # Photo de profil
    avatar = models.ImageField(
        upload_to="profile_images",
        default='image.png',
        blank=True,
        null=True
    )

    # École de l'utilisateur
    ecole = models.CharField(max_length=200, blank=True)

    def __str__(self):
        """
        Représentation textuelle du profil.
        """
        return f"{self.user.first_name}, {self.user.last_name}"

