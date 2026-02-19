const form = document.getElementById("editContactDetailsForm")

/**
 * Adds submission feedback to the Edit Contact Details form.
 *
 * When the form is submitted:
 * - Locates the form's submit button via `[type='submit']`.
 * - Disables the button to prevent duplicate submissions.
 * - Updates the button text to display a loading spinner
 *   and "Saving..." message for user feedback.
 */

if (form){
    form.addEventListener("submit", (e) => {
        const submitBtn = form.querySelector("[type='submit']");
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Saving... <i class="fa-solid fa-spinner fa-spin ms-2"></i>';
    });
}
