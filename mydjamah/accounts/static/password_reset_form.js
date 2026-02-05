document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggle-password');

    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetInput = document.getElementById(targetId);

            if (targetInput) {
                if (targetInput.type === 'password') {
                    targetInput.type = 'text';
                    this.classList.replace('fa-eye', 'fa-eye-slash');
                } else {
                    targetInput.type = 'password';
                    this.classList.replace('fa-eye-slash', 'fa-eye');
                }
            }
        });
    });
});
