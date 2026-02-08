# Application Publications - Djamah

## Description

L'application **Publications** permet aux utilisateurs de :  
- Créer des posts (texte, image, PDF, lien externe)  
- Aimer et retirer leur like sur les posts  
- Commenter et répondre à des commentaires (imbriqués)  
- Repartager des publications  

Cette application constitue le **cœur social** de la plateforme Djamah.


## Installation & Configuration

1. Assurez-vous que le projet Django principal est installé.  
2. Ajouter `publications` à `INSTALLED_APPS` dans `settings.py` :  
```python
INSTALLED_APPS = [
    # autres apps
    'publications',
]
