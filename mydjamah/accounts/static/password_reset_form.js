
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form-container');
    const passwordInput = document.getElementById('password');
    const password1Input = document.getElementById('password1');
    
    const toggleButtons = document.querySelectorAll('.toggle-password');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetInput = document.getElementById(targetId);
            
            if (targetInput.type === 'password') {
                targetInput.type = 'text';
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');
            } else {
                targetInput.type = 'password';
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');
            }
        });
    });
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const password = passwordInput.value;
            const password1 = password1Input.value;
            
            // Validation
            if (password.length < 8) {
                alert('Le mot de passe doit contenir au moins 8 caractères.');
                return;
            }
            
            if (password !== password1) {
                alert('Les mots de passe ne correspondent pas.');
                return;
            }
            
            console.log('Nouveau mot de passe:', password);
            
            alert('Votre mot de passe a été réinitialisé avec succès !');
            
            window.location.href = 'signin.html';
        });
    }
});