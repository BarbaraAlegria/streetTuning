document.addEventListener('DOMContentLoaded', function() {
    var updateBtns = document.getElementsByClassName('update-cart');
    var changeQuantityBtns = document.getElementsByClassName('chg-quantity');

    for (var i = 0; i < updateBtns.length; i++) {
        updateBtns[i].addEventListener('click', function() {
            var productId = this.getAttribute('data-p');
            var action = this.getAttribute('data-action');
            console.log('Producto ID:', productId, 'Acción:', action);

            if (productId && action) {
                addToCart(productId, action);
            }
        });
    }

    for (var i = 0; i < changeQuantityBtns.length; i++) {
        changeQuantityBtns[i].addEventListener('click', function() {
            var productId = this.closest('.cart-row').getAttribute('data-product');
            var action = this.getAttribute('data-action');
            console.log('Producto ID:', productId, 'Acción:', action);

            if (productId && action) {
                updateCartQuantity(productId, action);
            }
        });
    }

    function addToCart(productId, action) {
        console.log('Agregando al carrito:', productId);

        const url = '/update_cart/';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('data:', data);
            if (data.status === 'error') {
                Swal.fire({
                    icon: 'warning',
                    title: 'Stock insuficiente',
                    text: data.message,
                    showConfirmButton: true,
                });
            } else {
                updateCartTotal(data.cart_items);  // Actualizar el contador inmediatamente
                Swal.fire({
                    icon: 'success',
                    title: 'Producto agregado al carrito',
                    showConfirmButton: false,
                    timer: 1500
                });
            }
        });
    }

    function updateCartQuantity(productId, action) {
        console.log('Actualizando cantidad del carrito:', productId, action);

        const url = '/update_cart_quantity/';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('data:', data);
            if (data.status === 'error') {
                Swal.fire({
                    icon: 'warning',
                    title: 'Stock insuficiente',
                    text: data.message,
                    showConfirmButton: true,
                });
            } else {
                updateCartTotal(data.cart_items); 
                   // Actualiza el DOM o recarga la página para reflejar los cambios en el carrito
                   location.reload(); // Actualizar el contador inmediatamente
            }
        });
    }

    function updateCartTotal(cartTotal) {
        document.getElementById('cart-total').textContent = cartTotal;
    }

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

    // Actualiza el contador del carrito al cargar la página
    fetch('/get_cart_items/')
    .then(response => response.json())
    .then(data => {
        updateCartTotal(data.cart_items);
    });
});
