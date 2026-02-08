document.addEventListener('DOMContentLoaded', function () {
    const toastElList = document.querySelectorAll('.toast');

    toastElList.forEach(function (toastEl) {
        const toast = new bootstrap.Toast(toastEl, {
            delay: 3000
        });
        toast.show();
    });
});