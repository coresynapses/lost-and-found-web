console.log("TAMIU Lost and Found") //test commit 2

// Welcome Message
window.addEventListener('load', function () {
    console.log('Lost and Found');
});


//return to main menu from log in screen option
returnToMain.addEventListener("click", function () {
    loginSection.style.display = "none"; // Simply hide the login form
});

// Search Bar Functionality for Item Cards
document.getElementById('search-bar').addEventListener('input', function (e) {
    const query = e.target.value.toLowerCase();
    const items = document.querySelectorAll('.item-card');

    items.forEach(item => {
        const itemName = item.querySelector('.item-name').textContent.toLowerCase();
        item.style.display = itemName.includes(query) ? '' : 'none';
    });
});

//log in logic
document.addEventListener("DOMContentLoaded", function () {
    const loginButton = document.getElementById("loginButton");
    const loginSection = document.getElementById("loginSection");

    if (loginButton && loginSection) {
        loginButton.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent link from navigating away
            loginSection.style.display = "block"; // Show login form
        });
    }
});

// Toggle visibility of the registration form
document.getElementById('registrationButton').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent default behavior (if it's an anchor)
    const registrationSection = document.getElementById('registrationSection');
    if (registrationSection.style.display === 'none') {
        registrationSection.style.display = 'block'; // Show the form
       
    } else {
        registrationSection.style.display = 'none'; // Hide the form (optional toggle)
    }
});


// Filter for Functionality of Status, Category, and Disposition
document.querySelectorAll('.filter-dropdown').forEach(filter => {
    filter.addEventListener('change', function () {
        const statusFilter = document.getElementById('status-filter').value.toLowerCase();
        const categoryFilter = document.getElementById('category-filter').value.toLowerCase();
        const dispositionFilter = document.getElementById('disposition-filter').value.toLowerCase();
        const items = document.querySelectorAll('.item-card');

        items.forEach(item => {
            const itemStatus = item.dataset.status.toLowerCase();
            const itemCategory = item.dataset.category.toLowerCase();
            const itemDisposition = item.dataset.disposition.toLowerCase();

            const statusMatch = statusFilter === 'all' || itemStatus === statusFilter;
            const categoryMatch = categoryFilter === 'all' || itemCategory === categoryFilter;
            const dispositionMatch = dispositionFilter === 'all' || itemDisposition === dispositionFilter;

            item.style.display = (statusMatch && categoryMatch && dispositionMatch) ? '' : 'none';
        });
    });
});
// Handle file input and preview the uploaded image

document.getElementById('upload-image').addEventListener('change', function (event) {
    const file = event.target.files[0];

    if (file) {
        // Check if the file is an image
        if (!file.type.startsWith('image/')) {
            alert('Please upload a valid image file.');
            return;
        }

        // Create a FileReader to preview the image
        const reader = new FileReader();
        reader.onload = function (e) {
            // Display the preview
            const previewContainer = document.getElementById('preview-container');
            previewContainer.innerHTML = `<img src="${e.target.result}" alt="Preview Image">`;
        };
        reader.readAsDataURL(file);
         }
});

// Handle file input and preview the uploaded image
document.getElementById('upload-image').addEventListener('change', function (event) {
    const file = event.target.files[0];

    if (file) {
        // Check if the file is an image
        if (!file.type.startsWith('image/')) {
            alert('Please upload a valid image file.');
            return;
        }

        // Create a FileReader to prev the image
        const reader = new FileReader();
        reader.onload = function (e) {
            const previewContainer = document.getElementById('preview-container');
            previewContainer.innerHTML = `<img src="${e.target.result}" alt="Preview Image">`;
        };
        reader.readAsDataURL(file);
    }
});

// Handle the upload button click event
document.getElementById('upload-btn').addEventListener('click', function () {
    const fileInput = document.getElementById('upload-image');
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('image', file);
        // BACKEND Replace '/upload' with Django endpoint for upload handling
        fetch('/upload', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                alert('Image uploaded successfully!');
                console.log('Server response:', data);
            })
            .catch(error => {
                console.error('Error uploading image:', error);
                alert('Image upload failed.');
            });
    } else {
        alert('Please select an image before uploading.');
    }
});

// Details Button Functionality
document.querySelectorAll('.details-btn').forEach(button => {
    button.addEventListener('click', function () {
        const itemId = button.dataset.itemId;
        window.location.href = `/details/${itemId}`;
    });
});