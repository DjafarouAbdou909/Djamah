document.addEventListener('DOMContentLoaded', function() {

    // ================================
    // TOGGLE COMMENTS SECTION
    // ================================
    const toggleCommentsBtns = document.querySelectorAll('.btn-toggle-comments');
    
    toggleCommentsBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const postId = this.dataset.post;
            const commentsSection = document.getElementById(`comments-${postId}`);
            
            if (commentsSection) {
                if (commentsSection.style.display === 'none' || !commentsSection.style.display) {
                    commentsSection.style.display = 'block';
                    commentsSection.style.animation = 'slideDown 0.3s ease';
                    
                    // Scroll vers les commentaires
                    setTimeout(() => {
                        commentsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }, 100);
                } else {
                    commentsSection.style.display = 'none';
                }
            }
        });
    });

    // ================================
    // TOGGLE REPLY FORM
    // ================================
    const toggleReplyBtns = document.querySelectorAll('.btn-toggle-reply');
    
    toggleReplyBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const commentId = this.dataset.comment;
            const replyForm = document.getElementById(`reply-form-${commentId}`);
            
            if (replyForm) {
                if (replyForm.style.display === 'none' || !replyForm.style.display) {
                    replyForm.style.display = 'block';
                    replyForm.querySelector('.reply-input').focus();
                } else {
                    replyForm.style.display = 'none';
                }
            }
        });
    });

    // ================================
    // AUTO-HIDE MESSAGES
    // ================================
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = 'slideOutUp 0.3s ease';
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });

    // ================================
    // LIKE BUTTON ANIMATION
    // ================================
    const likeForms = document.querySelectorAll('.action-form');
    
    likeForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const btn = this.querySelector('.btn-action');
            const icon = btn.querySelector('i');
            
            // Add animation
            icon.style.animation = 'heartBeat 0.3s ease';
            
            setTimeout(() => {
                icon.style.animation = '';
            }, 300);
        });
    });

    // ================================
    // SHOW COMMENTS BY DEFAULT IF HAS COMMENTS
    // ================================
    document.querySelectorAll('.comments-section').forEach(section => {
        const commentsList = section.querySelector('.comments-list');
        const hasComments = commentsList && commentsList.children.length > 0;
        
        if (hasComments) {
            section.style.display = 'block';
        } else {
            section.style.display = 'none';
        }
    });

    // ================================
    // COMMENT FORM SUBMIT ANIMATION
    // ================================
    const commentForms = document.querySelectorAll('.comment-form');
    
    commentForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('.btn-send-comment');
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            submitBtn.disabled = true;
        });
    });

    // ================================
    // REPLY FORM SUBMIT ANIMATION
    // ================================
    const replyForms = document.querySelectorAll('.reply-form');
    
    replyForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('.btn-send-reply');
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            submitBtn.disabled = true;
        });
    });

    // ================================
    // IMAGE LAZY LOADING
    // ================================
    const images = document.querySelectorAll('.post-image img');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }

    // ================================
    // PREVENT DOUBLE SUBMIT
    // ================================
    const allForms = document.querySelectorAll('form');
    
    allForms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButtons = this.querySelectorAll('button[type="submit"]');
            submitButtons.forEach(btn => {
                btn.disabled = true;
            });
        });
    });

    // ================================
    // ANIMATIONS KEYFRAMES
    // ================================
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideDown {
            from {
                opacity: 0;
                max-height: 0;
                overflow: hidden;
            }
            to {
                opacity: 1;
                max-height: 2000px;
            }
        }
        
        @keyframes slideOutUp {
            from {
                opacity: 1;
                transform: translateY(0);
            }
            to {
                opacity: 0;
                transform: translateY(-20px);
            }
        }
        
        @keyframes heartBeat {
            0%, 100% {
                transform: scale(1);
            }
            25% {
                transform: scale(1.3);
            }
            50% {
                transform: scale(1.1);
            }
            75% {
                transform: scale(1.4);
            }
        }
        
        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(100px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes slideOutRight {
            from {
                opacity: 1;
                transform: translateX(0);
            }
            to {
                opacity: 0;
                transform: translateX(100px);
            }
        }

        /* Fade in effect for loaded images */
        .post-image img {
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .post-image img.loaded {
            opacity: 1;
        }
    `;
    document.head.appendChild(style);

    // ================================
    // CONSOLE LOG
    // ================================
    console.log('✅ Page d\'accueil DJAMAH chargée');
    console.log('📝 Posts:', document.querySelectorAll('.post-card').length);
    console.log('💬 Sections de commentaires:', document.querySelectorAll('.comments-section').length);
    
    // Log des commentaires par post
    document.querySelectorAll('.post-card').forEach((card, index) => {
        const postId = card.dataset.postId;
        const commentsCount = card.querySelectorAll('.comment-item').length;
        console.log(`Post ${postId}: ${commentsCount} commentaire(s)`);
    });

});