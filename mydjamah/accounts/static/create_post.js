document.addEventListener('DOMContentLoaded', function() {

    // ================================
    // ELEMENTS
    // ================================
    const contentTextarea = document.getElementById('id_content');
    const charCount = document.getElementById('charCount');
    const imageInput = document.getElementById('id_image');
    const imagePreview = document.getElementById('imagePreview');
    const previewImg = document.getElementById('previewImg');
    const removeImageBtn = document.getElementById('removeImage');
    const pdfInput = document.getElementById('id_pdf');
    const pdfPreview = document.getElementById('pdfPreview');
    const pdfName = document.getElementById('pdfName');
    const removePdfBtn = document.getElementById('removePdf');
    const postForm = document.getElementById('postForm');

    // ================================
    // CHARACTER COUNTER
    // ================================
    if (contentTextarea && charCount) {
        function updateCharCount() {
            const length = contentTextarea.value.length;
            charCount.textContent = length;
            
            if (length > 1000) {
                charCount.style.color = '#F44336';
            } else if (length > 500) {
                charCount.style.color = '#FF9800';
            } else {
                charCount.style.color = '#00BFA6';
            }
        }
        
        // Initial count
        updateCharCount();
        
        contentTextarea.addEventListener('input', updateCharCount);
    }

    // ================================
    // IMAGE UPLOAD & PREVIEW
    // ================================
    if (imageInput) {
        imageInput.addEventListener('change', function() {
            const file = this.files[0];
            
            if (!file) return;
            
            // Validate file type
            if (!file.type.startsWith('image/')) {
                alert('Veuillez sélectionner une image valide (JPG, PNG, GIF, etc.)');
                this.value = '';
                return;
            }
            
            // Validate file size (5MB max)
            if (file.size > 5 * 1024 * 1024) {
                alert('L\'image ne doit pas dépasser 5MB.');
                this.value = '';
                return;
            }
            
            // Show preview
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImg.src = e.target.result;
                imagePreview.style.display = 'block';
                imagePreview.style.animation = 'fadeIn 0.3s ease';
            };
            reader.readAsDataURL(file);
        });
    }

    // Remove image
    if (removeImageBtn) {
        removeImageBtn.addEventListener('click', function() {
            imageInput.value = '';
            imagePreview.style.display = 'none';
            previewImg.src = '';
        });
    }

    // ================================
    // PDF UPLOAD & PREVIEW
    // ================================
    if (pdfInput) {
        pdfInput.addEventListener('change', function() {
            const file = this.files[0];
            
            if (!file) return;
            
            // Validate file type
            if (file.type !== 'application/pdf') {
                alert('Veuillez sélectionner un fichier PDF valide.');
                this.value = '';
                return;
            }
            
            // Validate file size (10MB max)
            if (file.size > 10 * 1024 * 1024) {
                alert('Le fichier PDF ne doit pas dépasser 10MB.');
                this.value = '';
                return;
            }
            
            // Show preview
            pdfName.textContent = file.name;
            pdfPreview.style.display = 'flex';
            pdfPreview.style.animation = 'fadeIn 0.3s ease';
        });
    }

    // Remove PDF
    if (removePdfBtn) {
        removePdfBtn.addEventListener('click', function() {
            pdfInput.value = '';
            pdfPreview.style.display = 'none';
            pdfName.textContent = '';
        });
    }

    // ================================
    // FORM VALIDATION
    // ================================
    if (postForm) {
        postForm.addEventListener('submit', function(e) {
            const content = contentTextarea.value.trim();
            
            if (!content) {
                e.preventDefault();
                alert('Veuillez entrer du contenu pour votre publication.');
                contentTextarea.focus();
                return false;
            }
            
            if (content.length < 10) {
                e.preventDefault();
                alert('Votre publication doit contenir au moins 10 caractères.');
                contentTextarea.focus();
                return false;
            }
            
            // Show loading state
            const submitBtn = this.querySelector('.btn-publish');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Publication...';
        });
    }

    // ================================
    // DRAG AND DROP FOR IMAGE
    // ================================
    const imageLabel = document.querySelector('label[for="id_image"]');
    
    if (imageLabel) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            imageLabel.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            imageLabel.addEventListener(eventName, () => {
                imageLabel.style.borderColor = '#00BFA6';
                imageLabel.style.background = 'rgba(0, 191, 166, 0.1)';
            });
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            imageLabel.addEventListener(eventName, () => {
                imageLabel.style.borderColor = '#78909C';
                imageLabel.style.background = 'white';
            });
        });
        
        imageLabel.addEventListener('drop', function(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            
            if (files.length > 0) {
                imageInput.files = files;
                imageInput.dispatchEvent(new Event('change'));
            }
        });
    }

    // ================================
    // AUTO-RESIZE TEXTAREA
    // ================================
    if (contentTextarea) {
        contentTextarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    }

    // ================================
    // ANIMATIONS
    // ================================
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(style);

    // ================================
    // CONSOLE LOG
    // ================================
    console.log('✅ Formulaire de création de post chargé');

});