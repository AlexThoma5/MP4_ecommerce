/* jshint esversion: 11 */

const editButtons = document.getElementsByClassName("btn-edit");
const editServiceForm = document.getElementById("editServiceForm");
const hiddenDescriptionInput = document.getElementById("hidden-description");
const modalEl = document.getElementById("editServiceModal");
const newEditModal = new bootstrap.Modal(modalEl);

// Quill initilisation, help from chatGPT on setup
const quill = new Quill("#quill-editor", {
  theme: "snow",
  modules: {
    toolbar: [["bold"], ["italic"], [{ list: "bullet" }]],
  },
});

/**
 * Initialises edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated service's data attributes upon click.
 * - Prefills the modal input fields and Quill editor with current service data.
 * - Updates the form's action URL for the specific service.
 * - Shows the modal for editing.
 */

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let serviceId = e.currentTarget.getAttribute("data-service_id");
    let serviceType = e.currentTarget.getAttribute("data-service_type");
    let serviceName = e.currentTarget.getAttribute("data-service_name");
    let serviceDesc = e.currentTarget.getAttribute("data-service_desc");
    let servicePrice = e.currentTarget.getAttribute("data-service_price");
    let serviceDuration = e.currentTarget.getAttribute("data-service_duration");
    let serviceSessions = e.currentTarget.getAttribute("data-service_sessions");
    let imageUrl = e.currentTarget.getAttribute("data-image-url");
    let previewImage = document.getElementById("image-preview");

    // Prefill modal input fields
    modalEl.querySelector("#id_edit-service_type").value = serviceType;
    modalEl.querySelector("#id_edit-name").value = serviceName;
    modalEl.querySelector("#id_edit-price").value = servicePrice;
    modalEl.querySelector("#id_edit-duration").value = serviceDuration;
    modalEl.querySelector("#id_edit-session_count").value = serviceSessions;

    // Always reset to default src which is static image
    previewImage.src = previewImage.dataset.defaultSrc;
    // Injects cloudinary url if its not placeholder
    if (imageUrl && !imageUrl.includes("placeholder")) {
      previewImage.src = imageUrl;
    }

    // Fill Quill editor field
    quill.root.innerHTML = serviceDesc;

    // Update form action via serviceID
    editServiceForm.setAttribute("action", `edit/${serviceId}/`);

    // Show modal with content
    newEditModal.show();
  });
}

/**
 * Handles form submission for the edit service modal.
 *
 * Before the form is submitted:
 * - Retrieves the current HTML content from the Quill editor.
 * - Strips invisible or empty content to prevent blank descriptions.
 * - Copies valid editor content into the hidden description input field.
 * - Ensures the backend receives clean, meaningful data for validation.
 * - (Help provided by chatGPT)
 */
editServiceForm.addEventListener("submit", function () {
  let content = quill.root.innerHTML;

  // Remove invisible tags or empty content
  const tempDiv = document.createElement("div");
  tempDiv.innerHTML = content;
  if (tempDiv.textContent.trim() === "") {
    // Treat as empty if no visible text
    hiddenDescriptionInput.value = "";
  } else {
    hiddenDescriptionInput.value = content;
  }
});
