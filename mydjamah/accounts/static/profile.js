// Profile JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const avatarInput = document.getElementById('avatarInput');
    const avatarContainer = document.getElementById('avatarContainer');
    const uploadBtn = document.getElementById('uploadBtn');
    const removeBtn = document.getElementById('removeBtn');
    const bioTextarea = document.getElementById('bio');
    const charCount = document.getElementById('charCount');
    const form = document.querySelector('.profile-form');
    
    let currentAvatar = null;
    
    // Upload Avatar
    if (uploadBtn) {
        uploadBtn.addEventListener('click', function() {
            avatarInput.click();
        });
    }
    
    // Preview Avatar
    if (avatarInput) {
        avatarInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            
            if (file) {
                // Vérifier le type de fichier
                if (!file.type.startsWith('image/')) {
                    alert('Veuillez sélectionner une image valide.');
                    return;
                }
                
                // Vérifier la taille (max 5MB)
                if (file.size > 5 * 1024 * 1024) {
                    alert('L\'image ne doit pas dépasser 5MB.');
                    return;
                }
                
                const reader = new FileReader();
                
                reader.onload = function(event) {
                    // Supprimer l'icône par défaut
                    avatarContainer.innerHTML = '';
                    
                    // Créer et afficher l'image
                    const img = document.createElement('img');
                    img.src = event.target.result;
                    avatarContainer.appendChild(img);
                    
                    // Afficher le bouton supprimer
                    removeBtn.style.display = 'inline-block';
                    
                    currentAvatar = event.target.result;
                };
                
                reader.readAsDataURL(file);
            }
        });
    }
    
    // Remove Avatar
    if (removeBtn) {
        removeBtn.addEventListener('click', function() {
            // Réinitialiser l'input
            avatarInput.value = '';
            
            // Restaurer l'icône par défaut
            avatarContainer.innerHTML = '<i class="fas fa-user"></i>';
            
            // Cacher le bouton supprimer
            removeBtn.style.display = 'none';
            
            currentAvatar = null;
        });
    }
    
    // Character Count for Bio
    if (bioTextarea && charCount) {
        bioTextarea.addEventListener('input', function() {
            const length = this.value.length;
            const maxLength = 200;
            
            charCount.textContent = length;
            
            // Limiter à 200 caractères
            if (length > maxLength) {
                this.value = this.value.substring(0, maxLength);
                charCount.textContent = maxLength;
            }
            
            // Changer la couleur si limite atteinte
            if (length >= maxLength) {
                charCount.style.color = '#F44336';
            } else {
                charCount.style.color = '#00BFA6';
            }
        });
    }
    
    // Form Submission
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const lastname = document.getElementById('lastname').value;
            const firstname = document.getElementById('firstname').value;
            const school = document.getElementById('school').value;
            const bio = document.getElementById('bio').value;
            
            // Validation
            if (!lastname || !firstname || !school) {
                alert('Veuillez remplir tous les champs obligatoires.');
                return;
            }
            
            // Ici, vous ajouterez votre logique d'envoi au serveur
            const profileData = {
                lastname: lastname,
                firstname: firstname,
                school: school,
                bio: bio,
                avatar: currentAvatar
            };
            
            console.log('Données du profil:', profileData);
            
            alert('Profil enregistré avec succès !');
            
            // Optionnel: redirection
            // window.location.href = 'dashboard.html';
        });
    }
});