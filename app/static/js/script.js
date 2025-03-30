document.addEventListener("DOMContentLoaded", function () {
    console.log(" App loaded successfully!");

    // 🔹 Password Toggle Function
    // ✅ Fix Password Toggle Function
    function setupPasswordToggle(toggleId, inputId) {
        const toggle = document.getElementById(toggleId);
        const input = document.getElementById(inputId);

        if (toggle && input) {
            toggle.addEventListener("click", function () {
                if (input.type === "password") {
                    input.type = "text";
                    this.classList.remove("fa-eye");
                    this.classList.add("fa-eye-slash");
                } else {
                    input.type = "password";
                    this.classList.remove("fa-eye-slash");
                    this.classList.add("fa-eye");
                }
            });
        }
    }

    setupPasswordToggle("togglePassword", "password");

    console.log("Password toggle initialized!");
});

    

    // 🔹 Role Dropdown Population
    const rolesDropdown = document.getElementById("rolesDropdown");
    if (rolesDropdown) {
        const roles = ["Manager", "Admin", "Employee"];
        rolesDropdown.innerHTML = `<option value="">Select Role...</option>`; // Default Option

        roles.forEach(role => {
            const option = document.createElement("option");
            option.value = role;
            option.textContent = role;
            rolesDropdown.appendChild(option);
        });

        console.log(" Role dropdown populated:", roles);
    }

    // 🔹 Form Validation Before Submission
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (event) {
            const managerId = document.getElementById("namesDropdown").value.trim();
            const role = document.getElementById("rolesDropdown").value.trim();
            const username = document.querySelector("[name='username']").value.trim();
            const password = document.querySelector("[name='password']").value.trim();
            const confirmPassword = document.querySelector("[name='confirm_password']").value.trim();

            console.log("Form Data:", { managerId, role, username, password, confirmPassword });

            if (!managerId) {
                alert("Please select your name!");
                event.preventDefault();
                return;
            }

            if (!role) {
                alert("Please select a role!");
                event.preventDefault();
                return;
            }

            if (!username || !password || !confirmPassword) {
                alert("All fields are required!");
                event.preventDefault();
                return;
            }

            if (password !== confirmPassword) {
                alert("Passwords do not match!");
                event.preventDefault();
                return;
            }

            console.log("Form submitted successfully!");
        });
    }
});
