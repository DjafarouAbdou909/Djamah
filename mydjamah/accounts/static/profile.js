document.addEventListener('DOMContentLoaded', function () {

    const avatarInput = document.getElementById('avatarInput');
    const avatarContainer = document.getElementById('avatarContainer');
    const uploadBtn = document.getElementById('uploadBtn');
    const removeBtn = document.getElementById('removeBtn');
    const bioTextarea = document.getElementById('bio');
    const charCount = document.getElementById('charCount');

    if (uploadBtn && avatarInput) {
        uploadBtn.addEventListener('click', () => {
            avatarInput.click();
        });
    }

    // Preview avatar
    if (avatarInput) {
        avatarInput.addEventListener('change', function () {
            const file = this.files[0];

            if (!file) return;

            if (!file.type.startsWith('image/')) {
                alert('Veuillez sélectionner une image valide.');
                avatarInput.value = '';
                return;
            }

            if (file.size > 5 * 1024 * 1024) {
                alert('L’image ne doit pas dépasser 5MB.');
                avatarInput.value = '';
                return;
            }

            const reader = new FileReader();
            reader.onload = function (e) {
                avatarContainer.innerHTML = '';
                const img = document.createElement('img');
                img.src = e.target.result;
                avatarContainer.appendChild(img);
            };

            reader.readAsDataURL(file);
        });
    }

    if (bioTextarea && charCount) {
        charCount.textContent = bioTextarea.value.length;

        bioTextarea.addEventListener('input', function () {
            const length = this.value.length;
            charCount.textContent = length;

            if (length >= 200) {
                charCount.style.color = '#F44336';
            } else {
                charCount.style.color = '#00BFA6';
            }
        });
    }

});
