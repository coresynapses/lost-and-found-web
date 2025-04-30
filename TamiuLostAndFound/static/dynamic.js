
console.log("TAMIU Lost and Found"); // test commit 2
console.log('dynamic.js loaded');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');

    // Select elements
    const loginButton = document.getElementById("loginButton");
    const registrationButton = document.getElementById("registrationButton");
    const reportButton = document.getElementById("reportButton");
    const returnToMainButton = document.getElementById("returnToMain");
    const loginSection = document.getElementById("loginSection");
    const registrationSection = document.getElementById("registrationSection");
    const reportSection = document.getElementById("reportSection");
    const mainContent = document.querySelector(".item-container");
    const reportForm = document.getElementById("reportForm");
    const showReportButton = document.getElementById("reportBtn");
    const cancelButton = document.querySelector(".report-btn-secondary");
    const searchBar = document.getElementById('search-bar');
    const uploadImageInput = document.getElementById('upload-image');
    const uploadButton = document.getElementById('upload-btn');
    const claimButton = document.getElementById('claim-item-btn');
    const claimForm = document.getElementById('claim-proof-form');
    const reportFraudButton = document.getElementById('report-fraud-btn');
    const reportFraudForm = document.getElementById('report-fraud-form');
    const prevButton = document.getElementById('prev-btn');
    const nextButton = document.getElementById('next-btn');
    const fraudFormElement = document.getElementById('fraudForm');
    const fraudThankYouMessage = document.getElementById('fraud-thank-you');
    const reportFraudFormContainer = document.getElementById('report-fraud-form');
    const themeButton = document.getElementById('themeToggle');

    // Login toggle
    if (loginButton && loginSection) {
        loginButton.addEventListener("click", function () {
            loginSection.style.display = loginSection.style.display === "block" ? "none" : "block";
            if (registrationSection) registrationSection.style.display = "none";
            if (reportSection) reportSection.style.display = "none";
        });
    }

    // Registration toggle
    if (registrationButton && registrationSection) {
        registrationButton.addEventListener("click", function () {
            registrationSection.style.display = registrationSection.style.display === "block" ? "none" : "block";
            if (loginSection) loginSection.style.display = "none";
            if (reportSection) reportSection.style.display = "none";
        });
    }

    // Return button
    if (returnToMainButton && loginSection) {
        returnToMainButton.addEventListener("click", function () {
            loginSection.style.display = "none";
        });
    }

    // Search bar
    if (searchBar) {
        searchBar.addEventListener('input', function (e) {
            const query = e.target.value.toLowerCase();
            const items = document.querySelectorAll('.item-card');
            items.forEach(item => {
                const itemName = item.querySelector('.item-name').textContent.toLowerCase();
                item.style.display = itemName.includes(query) ? '' : 'none';
            });
        });
    }

    // Show report form
    if (showReportButton && reportForm) {
        showReportButton.addEventListener("click", function () {
            reportForm.style.display = "block";
        });
    }

    if (cancelButton && reportForm) {
        cancelButton.addEventListener("click", function () {
            reportForm.style.display = "none";
        });
    }

    // Upload image preview
    if (uploadImageInput) {
        uploadImageInput.addEventListener('change', function (event) {
            const file = event.target.files[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    const previewContainer = document.getElementById('preview-container');
                    if (previewContainer) {
                        previewContainer.innerHTML = `<img src="${e.target.result}" alt="Preview Image">`;
                    }
                };
                reader.readAsDataURL(file);
            } else {
                alert('Please upload a valid image file.');
            }
        });
    }

    if (uploadButton && uploadImageInput) {
        uploadButton.addEventListener('click', function () {
            const file = uploadImageInput.files[0];
            if (file) {
                const formData = new FormData();
                formData.append('image', file);
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
    }

    // Details Button
    document.querySelectorAll('.details-btn').forEach(button => {
        button.addEventListener('click', function () {
            const itemId = button.dataset.itemId;
            window.location.href = `/details/${itemId}`;
        });
    });

    // Claim logic
    if (claimButton && claimForm) {
        claimButton.addEventListener('click', function () {
            claimForm.style.display = claimForm.style.display === 'none' ? 'flex' : 'none';
        });
    }

    if (claimForm && claimButton && reportFraudButton) {
        claimForm.addEventListener('submit', function (event) {
            event.preventDefault();
            claimButton.style.display = 'none';
            claimForm.style.display = 'none';
            reportFraudButton.style.display = 'inline-block';
        });
    }

    if (reportFraudButton && reportFraudForm) {
        reportFraudButton.addEventListener('click', function () {
            reportFraudForm.style.display = reportFraudForm.style.display === 'none' ? 'flex' : 'none';
        });
    }

    if (fraudFormElement && fraudThankYouMessage && reportFraudFormContainer) {
        fraudFormElement.addEventListener('submit', function (event) {
            event.preventDefault();
            reportFraudFormContainer.style.display = 'none';
            fraudThankYouMessage.style.display = 'block';
            setTimeout(function () {
                window.location.href = '/';
            }, 5000);
        });
    }

    // Navigation buttons
    const currentUrl = window.location.href;
    const itemIdMatch = currentUrl.match(/\/item-list\/(\d+)/);
    if (itemIdMatch) {
        let currentItemId = parseInt(itemIdMatch[1]);
        if (prevButton) {
            prevButton.addEventListener('click', function () {
                if (currentItemId > 1) {
                    const prevItemId = currentItemId - 1;
                    window.location.href = `/item-list/${prevItemId}/`;
                }
            });
        }
        if (nextButton) {
            nextButton.addEventListener('click', function () {
                const nextItemId = currentItemId + 1;
                window.location.href = `/item-list/${nextItemId}/`;
            });
        }
    }

    // THEME TOGGLE
    const savedTheme = localStorage.getItem('theme') || 'light';
    function applyTheme(theme) {
        if (theme === 'dark') {
            document.body.classList.add('dark-mode');
            themeButton.textContent = '☀️';
        } else {
            document.body.classList.remove('dark-mode');
            themeButton.textContent = '🌙';
        }
        localStorage.setItem('theme', theme);
    }

    applyTheme(savedTheme);

    if (themeButton) {
        themeButton.addEventListener('click', () => {
            const isDark = document.body.classList.contains('dark-mode');
            applyTheme(isDark ? 'light' : 'dark');
        });
    }
});
