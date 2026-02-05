const toggles = document.querySelectorAll(".toggle-password");

toggles.forEach(toggle => {
    toggle.addEventListener("click", () => {
        const input = document.getElementById(toggle.dataset.target);

        if (input.type === "password") {
            input.type = "text";
            toggle.classList.replace("fa-eye", "fa-eye-slash");
        } else {
            input.type = "password";
            toggle.classList.replace("fa-eye-slash", "fa-eye");
        }
    });
});
