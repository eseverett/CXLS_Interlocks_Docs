// Purpose: This script makes tables with images scrollable on smaller screens.

document.addEventListener("DOMContentLoaded", function() {
    const tables = document.querySelectorAll('table');

    tables.forEach(function(table) {
        if (table.querySelector('img')) {
            const wrapper = document.createElement('div');
            wrapper.style.overflowX = 'auto';
            table.parentNode.insertBefore(wrapper, table);
            wrapper.appendChild(table);
        }
    });
});
