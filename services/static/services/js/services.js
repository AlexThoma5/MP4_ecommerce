/* jshint esversion: 11 */

// Modal and Form variables
const serviceForm = document.getElementById("serviceForm");
const modalEl = document.getElementById("serviceModal");
const newModal = new bootstrap.Modal(modalEl);
const modalTitle = document.getElementById("serviceModalLabel");
const hiddenDescriptionInput = document.getElementById("hidden-description");
const submitBtn = document.getElementById("submitButton");

// Separate delete modal
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

// Quill initilisation, help from chatGPT on setup
const quill = new Quill("#quill-editor", {
  theme: "snow",
  modules: {
    toolbar: [["bold"], ["italic"], [{ list: "bullet" }]],
  },
});

/**
 * Delegates click events for buttons with `data-btn-modal`.
 *
 * - Determines which action to take based on `data-btn-modal` attribute.
 * - Calls `prepareAddModal`, `prepareEditModal`, or `prepareDeleteModal`.
 */
document.addEventListener("click", function (e) {
    const button = e.target.closest("[data-btn-modal]");
    if (!button) return;

    const modalAction = button.dataset.btnModal;

    switch (modalAction) {
        case "add":
            prepareAddModal();
            break;

        case "edit":
            prepareEditModal(button);
            break;

        case "delete":
            prepareDeleteModal(button);
            break;

        default:
            console.warn("Unknown modal action:", modalAction);
    }
});

/**
 * Prepares the Add Service modal.
 *
 * - Resets the form and Quill editor.
 * - Resets the image preview to the default.
 * - Updates modal title and submit button text.
 * - Updates form action to "add/".
 * - Displays the modal.
 */
function prepareAddModal() {
    serviceForm.reset();
    quill.root.innerHTML = "";

    document.getElementById("image-label").textContent = "Default image:";
    const previewImage = document.getElementById("image-preview");
    previewImage.src = previewImage.dataset.defaultSrc;

    modalTitle.textContent = "Add Service";
    submitBtn.textContent = "Save";
    serviceForm.setAttribute("action", "add/");
    newModal.show();
}

/**
 * Prepares the Edit Service modal for a specific service.
 *
 * - Prefills modal input fields using the button's dataset.
 * - Fills Quill editor with the service description.
 * - Updates the image preview (existing or default).
 * - Updates modal title and submit button text.
 * - Updates form action for the specific service ID.
 * - Displays the modal.
 */
function prepareEditModal(button) {
    const serviceId = button.dataset.service_id;

    // Prefill modal input fields
    modalEl.querySelector("#id_service_type").value = button.dataset.service_type;
    modalEl.querySelector("#id_name").value = button.dataset.service_name;
    modalEl.querySelector("#id_price").value = button.dataset.service_price;
    modalEl.querySelector("#id_duration").value = button.dataset.service_duration;
    modalEl.querySelector("#id_session_count").value = button.dataset.service_sessions;

    // Fill Quill editor field
    quill.root.innerHTML = button.dataset.service_desc;

    // Image preview logic
    const imageUrl = button.dataset.imageUrl;
    const previewImage = document.getElementById("image-preview");
    // Reset image back to default src
    previewImage.src = previewImage.dataset.defaultSrc;
    // Injects cloudinary url if its not placeholder
    if (imageUrl && !imageUrl.includes("placeholder")) {
        previewImage.src = imageUrl;
    }

    document.getElementById("image-label").textContent = "Current image:";
    modalTitle.textContent = "Edit Service";
    submitBtn.textContent = "Update";
    serviceForm.setAttribute("action", `edit/${serviceId}/`);
    newModal.show();
}

/**
 * Handles form submission for the Add/Edit service modal.
 *
 * - Retrieves HTML content from the Quill editor.
 * - Strips invisible or empty content to prevent blank descriptions.
 * - Copies valid editor content into the hidden description input field.
 */
serviceForm.addEventListener("submit", function () {
    const textContent = quill.root.innerHTML.trim();

    // Remove invisible tags caused by quill
    if (textContent === "<p><br></p>") {
        hiddenDescriptionInput.value = "";
    } else {
        hiddenDescriptionInput.value = textContent;
    }
});

/**
 * Prepares the Delete Service modal.
 *
 * - Sets the service name in the confirmation modal.
 * - Updates the delete confirmation link.
 * - Displays the delete modal.
 */
function prepareDeleteModal(button) {
    const serviceId = button.dataset.service_id;
    const serviceName = button.dataset.service_name;

    document.getElementById("service-name").innerText = serviceName;
    document.getElementById("deleteConfirm").href = `delete/${serviceId}`;

    deleteModal.show();
}
