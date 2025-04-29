console.log("TAMIU Lost and Found"); //test commit 2
console.log('dynamic.js loaded');

// All logic INSIDE DOMContentLoaded
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


    // Login Button
    if (loginButton && loginSection) {
        loginButton.addEventListener("click", function () {
            loginSection.style.display = loginSection.style.display === "block" ? "none" : "block";
            if (registrationSection) registrationSection.style.display = "none";
            if (reportSection) reportSection.style.display = "none";
        });
    }

    // Registration Button
    if (registrationButton && registrationSection) {
        registrationButton.addEventListener("click", function () {
            registrationSection.style.display = registrationSection.style.display === "block" ? "none" : "block";
            if (loginSection) loginSection.style.display = "none";
            if (reportSection) reportSection.style.display = "none";
        });
    }

    // Return to Main Button
    if (returnToMainButton && loginSection) {
        returnToMainButton.addEventListener("click", function () {
            loginSection.style.display = "none";
        });
    }

    // Search Bar
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

    // Report Button
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

    // Upload Image Preview
    if (uploadImageInput) {
        uploadImageInput.addEventListener('change', function (event) {
            const file = event.target.files[0];
            if (file) {
                if (!file.type.startsWith('image/')) {
                    alert('Please upload a valid image file.');
                    return;
                }
                const reader = new FileReader();
                reader.onload = function (e) {
                    const previewContainer = document.getElementById('preview-container');
                    if (previewContainer) {
                        previewContainer.innerHTML = `<img src="${e.target.result}" alt="Preview Image">`;
                    }
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Upload Button
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

    // CLAIM ITEM BUTTON 
    if (claimButton && claimForm) {
        console.log('Claim button and form found!');
	
        claimButton.addEventListener('click', function () {
            console.log('Claim button clicked!');
            if (claimForm.style.display === 'none' || claimForm.style.display === '') {
                claimForm.style.display = 'flex';
            } else {
                claimForm.style.display = 'none';
            }
        });

    } else {
        console.log('Claim button or claim form not found!');
    }

    if (claimForm && claimButton && reportFraudButton) {
        claimForm.addEventListener('submit', function(event) {
            event.preventDefault();
    
            console.log('Claim form submitted.');
    
            // Hide 
            claimButton.style.display = 'none';

             // Hide 
            claimForm.style.display = 'none';
    
            // Show Report Fraud button
            reportFraudButton.style.display = 'inline-block';
    
        
        });
    }

    if (reportFraudButton && reportFraudForm) {
        reportFraudButton.addEventListener('click', function () {
            console.log('Report Fraud button clicked!');
            if (reportFraudForm.style.display === 'none' || reportFraudForm.style.display === '') {
                reportFraudForm.style.display = 'flex'; // Open the form
            } else {
                reportFraudForm.style.display = 'none'; // (Optional: clicking again hides it)
            }
        });
    }

    const fraudFormElement = document.getElementById('fraudForm');
    const fraudThankYouMessage = document.getElementById('fraud-thank-you');
    const reportFraudFormContainer = document.getElementById('report-fraud-form');
    
    if (fraudFormElement && fraudThankYouMessage && reportFraudFormContainer) {
        fraudFormElement.addEventListener('submit', function(event) {
            event.preventDefault(); // Stop full page reload
    
            console.log('Fraud form submitted.');
    
            // Hide the Report Fraud form
            reportFraudFormContainer.style.display = 'none';
    
            // Show the Thank You message
            fraudThankYouMessage.style.display = 'block';
    
            // Redirect after 5 seconds (optional)
            setTimeout(function() {
                window.location.href = '/'; // or your page
            }, 5000);
        });
    }

    // Get the current item ID from the URL
    const currentUrl = window.location.href;
    const itemIdMatch = currentUrl.match(/\/item-list\/(\d+)/);
    
    if (itemIdMatch) {
	let currentItemId = parseInt(itemIdMatch[1]); // Extract current item ID as number
	
	if (prevButton) {
            prevButton.addEventListener('click', function() {
		if (currentItemId > 1) { // Optional: Only go back if > 1
                    const prevItemId = currentItemId - 1;
                    window.location.href = `/item-list/${prevItemId}/`;
		}
		// Optional: if at 1, loop to last item? (Advanced)
            });
	}
	
	if (nextButton) {
            nextButton.addEventListener('click', function() {
		const nextItemId = currentItemId + 1;
		window.location.href = `/item-list/${nextItemId}/`;
            });
	}
    }
});
