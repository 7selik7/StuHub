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

function showToast(message) {
  Toastify({
    text: message,
    duration: 3000,
    close: true,
    gravity: "top",
    position: "center",
    backgroundColor: "#7F7F81",
    stopOnFocus: true,
  }).showToast();
}

let csrfToken = getCookie('csrftoken');
let deleteButtons = document.getElementsByClassName("delete-btn");

for (let i = 0; i < deleteButtons.length; i++) {
    deleteButtons[i].addEventListener("click", function() {
        let orderId = this.getAttribute("data-order-id");

        let confirmationModal = new bootstrap.Modal(document.getElementById("confirmation-modal"));
        confirmationModal.show();

        let confirmBtn = document.getElementById("confirm-btn");
        let cancelBtn = document.getElementById("cancel-btn");

        let confirmHandler = function() {
            let xhr = new XMLHttpRequest();
            xhr.open("DELETE", "/orders/delete_order/" + orderId + "/", true);
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                  let response = JSON.parse(xhr.responseText);
                  showToast(response.message);
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

window.addEventListener("DOMContentLoaded", function () {
    var descriptions = document.getElementsByClassName("description-hover");
    for (var i = 0; i < descriptions.length; i++) {
        descriptions[i].addEventListener("mouseover", function () {
            this.style.height = this.scrollHeight + "px";
        });
        descriptions[i].addEventListener("mouseout", function () {
            this.style.height = "1.5em";
        });
    }
});