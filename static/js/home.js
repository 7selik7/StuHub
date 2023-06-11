function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

let csrfToken = getCookie('csrftoken');
let executeButtons = document.getElementsByClassName("execute-btn");

for (let i = 0; i < executeButtons.length; i++) {
    executeButtons[i].addEventListener("click", function() {
        let orderId = this.getAttribute("data-order-id");

        let confirmationModal = new bootstrap.Modal(document.getElementById("confirmation-modal"));
        confirmationModal.show();

        let confirmBtn = document.getElementById("confirm-btn");
        let cancelBtn = document.getElementById("cancel-btn");

        let confirmHandler = function() {
            let xhr = new XMLHttpRequest();
            xhr.open("POST", "/orders/execute_order/" + orderId + "/", true);
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    let response = JSON.parse(xhr.responseText);
                    console.log(response.message);
                }
            };
            xhr.send();

            confirmationModal.hide();

            confirmBtn.removeEventListener("click", confirmHandler);
        };

        let cancelHandler = function() {
            confirmationModal.hide();
            confirmBtn.removeEventListener("click", confirmHandler);
        };

        confirmBtn.addEventListener("click", confirmHandler);
        cancelBtn.addEventListener("click", cancelHandler);
    });
}
