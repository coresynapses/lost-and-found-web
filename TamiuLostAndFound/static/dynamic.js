console.log("TAMIU Lost and Found") //test commit 2

// Welcome Message
window.addEventListener('load', function () {
    console.log('Lost and Found');
});

// Select elements
const loginButton = document.getElementById("loginButton");
const registrationButton = document.getElementById("registrationButton");
const reportButton = document.getElementById("reportButton"); 
const returnToMainButton = document.getElementById("returnToMain");
const loginSection = document.getElementById("loginSection");
const registrationSection = document.getElementById("registrationSection");
const reportSection = document.getElementById("reportSection");
const mainContent = document.querySelector(".item-container");


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


document.addEventListener("DOMContentLoaded", function () {
    const loginButton = document.getElementById("loginButton");
    const registrationButton = document.getElementById("registrationButton");
    const loginSection = document.getElementById("loginSection");
    const registrationSection = document.getElementById("registrationSection");
    const reportSection = document.getElementById("reportForm");

    if (loginButton && loginSection) {
        loginButton.addEventListener("click", function () {
            loginSection.style.display = loginSection.style.display === "block" ? "none" : "block";
            registrationSection.style.display = "none"; // Hide registration when login is clicked
            reportSection.style.display = "none"; // Hide report when login is clicked
        });
    }

    if (registrationButton && registrationSection) {
        registrationButton.addEventListener("click", function () {
            registrationSection.style.display = registrationSection.style.display === "block" ? "none" : "block";
            loginSection.style.display = "none"; // Hide login when registration is clicked
            reportSection.style.display = "none"; // Hide report when registration is clicked
        });
    }

});

const reportForm = document.getElementById("reportForm");
const showReportButton = document.getElementById("reportBtn");
const cancelButton = document.querySelector(".report-btn-secondary");

showReportButton.addEventListener("click", function() {
    reportForm.style.display = "block";
});

cancelButton.addEventListener("click", function() {
    reportForm.style.display = "none";
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
        if (!file.type.startsWith('image/')) {
            alert('Please upload a valid image file.');
            return;
        }

        // Create a FileReader prev image
        const reader = new FileReader();
        reader.onload = function (e) {
            // Display the prev
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