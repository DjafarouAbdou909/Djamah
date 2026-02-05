# App Accounts - DJAMAH

Cette application gère tout ce qui concerne les utilisateurs sur DJAMAH :  
inscription, connexion, profils, et administration. Elle utilise un **User personnalisé** basé sur l'email comme identifiant principal.

---

## Fonctionnalités principales

- **Inscription et activation par e-mail**
- **Connexion et déconnexion sécurisée**
- **Gestion du profil utilisateur**
  - Photo de profil (avatar)
  - Bio
  - École
  - Classe / Niveau
- **Admin Django pour User et Profile**
- **Système de messages pour informer l'utilisateur**

---

## Modèles

### User
Modèle personnalisé basé sur `AbstractUser` :

- `email` : identifiant unique pour l’authentification
- `classe` : niveau scolaire ou universitaire
- `first_name` et `last_name`
- `is_active`, `is_staff`, `is_superuser` pour la gestion des droits
- **Manager personnalisé** (`UserManager`) pour créer des users et superusers

### Profile
Profil associé à chaque utilisateur :

- `user` : relation OneToOne avec User
- `avatar` : image de profil
- `bio` : description personnelle
- `ecole` : école ou établissement de l'utilisateur

---

## Forms

- **UpdateUserForm** : pour modifier le prénom et le nom
- **UpdateProfileForm** : pour modifier la photo, la bio et l’école

---

## Vues

- `home` : page d'accueil
- `signup` : inscription avec validation et envoi d'e-mail d'activation
- `signin` : connexion sécurisée
- `profile` : affichage et mise à jour du profil (login requis)
- `logOut` : déconnexion
- `activate` : activation du compte via lien envoyé par email

---

## Admin Django

- **UserAdmin**
  - Affiche : nom, prénom, email, classe, droits staff et actif
  - Recherche : email, nom, prénom
- **ProfileAdmin**
  - Affiche : nom complet, bio, avatar, école
  - Recherche : nom, prénom, école

---

## Instructions d'installation

1. Ajouter l’app `accounts` à `INSTALLED_APPS` dans `settings.py`.
2. Configurer `AUTH_USER_MODEL` :  
   ```python
   AUTH_USER_MODEL = 'accounts.User'
