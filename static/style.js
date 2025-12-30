document.getElementById('submitBtn').addEventListener('click', function() {
    const name = document.getElementById('nameInput').value;
    if (name.trim() === '') {
        alert('Please enter a name.');
        return;
    }
    fetch('/submit_name', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred.');
    });
});