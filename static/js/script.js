const password = document.getElementById("password");
const strength = document.getElementById("strength");

if (password) {
    password.addEventListener("input", () => {
        const value = password.value;

        if (value.length < 6) {
            strength.innerHTML = "Weak Password";
            strength.style.color = "red";
        }
        else if (value.length < 10) {
            strength.innerHTML = "Medium Password";
            strength.style.color = "orange";
        }
        else {
            strength.innerHTML = "Strong Password";
            strength.style.color = "lime";
        }
    });
}

function togglePassword() {
    const passwordField = document.getElementById("password");

    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}