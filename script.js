// Registration
document.querySelector('.link a').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the link from being followed

    var email = prompt('Enter your email:');
    var password = prompt('Enter your password:');

    localStorage.setItem('email', email);
    localStorage.setItem('password', password);

    alert('Registration successful!');
});

// Login
document.querySelector('.btnn a').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the link from being followed

    var email = document.querySelector('input[type="email"]').value;
    var password = document.querySelector('input[type="password"]').value;

    if (email === localStorage.getItem('email') && password === localStorage.getItem('password')) {
        alert('Login successful!');
    } else {
        alert('Invalid credentials!');
    }
});
