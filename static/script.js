// Fetch available properties from the backend
async function fetchProperties() {
    try {
        const response = await fetch('/properties');
        if (!response.ok) {
            throw new Error('Failed to fetch properties');
        }
        const properties = await response.json();
        updatePropertiesList(properties);
    } catch (error) {
        console.error('Error fetching properties:', error);
    }
}

function updatePropertiesList(properties) {
    const propertiesList = document.getElementById('properties-list');
    propertiesList.innerHTML = ''; // Clear previous data
    properties.forEach(property => {
        const propertyCard = document.createElement('div');
        propertyCard.classList.add('property-card');
        propertyCard.innerHTML = `
            <h3>${property.name}</h3>
            <p>Agent ID: ${property.agent_id}</p>
            <!-- Add more property details here as needed -->
        `;
        propertiesList.appendChild(propertyCard);
    });
}

// Handle form submission for tenant registration
async function handleRegistration(event) {
    event.preventDefault();
    const registrationForm = event.target;
    try {
        const formData = new FormData(registrationForm);
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                full_name: formData.get('full-name'),
                email: formData.get('email'),
                property_id: formData.get('property-id')
            })
        });
        if (!response.ok) {
            throw new Error('Failed to register tenant');
        }
        const data = await response.json();
        alert(data.message); // Show registration status message
        registrationForm.reset(); // Clear the form
    } catch (error) {
        console.error('Error registering tenant:', error);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    fetchProperties();

    const registrationForm = document.getElementById('registration-form');
    registrationForm.addEventListener('submit', handleRegistration);
});
