// Function to show the modal
function showModal(event) {
    event.preventDefault(); // Prevent form submission
    const modal = document.getElementById("result-modal");
    modal.style.display = "flex";
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById("result-modal");
    modal.style.display = "none";
}

// Close modal if user clicks outside the modal content
window.onclick = function (event) {
    const modal = document.getElementById("result-modal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
};
