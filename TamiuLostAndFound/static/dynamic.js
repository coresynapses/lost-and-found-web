console.log("TAMIU Lost and Found") //test commit 2

// Welcome Message
window.addEventListener('load', function () {
    console.log('Lost and Found');
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

// Details Button Functionality
document.querySelectorAll('.details-btn').forEach(button => {
    button.addEventListener('click', function () {
        const itemId = button.dataset.itemId;
        window.location.href = `/details/${itemId}`;
    });
});