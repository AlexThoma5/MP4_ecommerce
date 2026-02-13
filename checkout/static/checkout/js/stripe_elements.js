/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js

    I used chatgpt to help convert the jquery from the
    BoutiqueAdo walkthrough into a more familiar 
    vanilla JS for my understanding.
*/

document.addEventListener('DOMContentLoaded', () => {
    const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
    const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);

    const stripe = Stripe(stripePublicKey);
    const elements = stripe.elements();

    const style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': { color: '#aab7c4' }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    const card = elements.create('card', { style: style });
    card.mount('#card-element');

    // Handle realtime validation errors on the card element
    card.addEventListener('change', function(event) {
        const errorDiv = document.getElementById('card-errors');
        if (event.error) {
            errorDiv.innerHTML = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submit
    const form = document.getElementById('payment-form');
    const paymentForm = document.getElementById('payment-form');
    const loadingOverlay = document.getElementById('loading-overlay');

    form.addEventListener('submit', async function(ev) {
        ev.preventDefault();

        // Disable card and submit button
        card.update({ disabled: true });
        document.getElementById('submit-button').disabled = true;

        // Hide form & show loading overlay (replaces fadeToggle)
        paymentForm.style.display = 'none';
        loadingOverlay.style.display = 'block';

        // Get save info and csrf token
        const saveInfoElement = document.getElementById('id-save-info');
        const saveInfo = saveInfoElement ? saveInfoElement.checked : false;
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        // Prepare POST data
        const postData = new FormData();
        postData.append('csrfmiddlewaretoken', csrfToken);
        postData.append('client_secret', clientSecret);
        postData.append('save_info', saveInfo);


        try {
            // Send POST request (replaces $.post)
            const response = await fetch('/checkout/cache_checkout_data/', {
                method: 'POST',
                body: postData,
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            // Confirm the card payment
            const result = await stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: form.full_name.value.trim(),
                        phone: form.phone_number.value.trim(),
                        email: form.email.value.trim(),
                    }
                },
            });

            if (result.error) {
                // Show error
                const errorDiv = document.getElementById('card-errors');
                errorDiv.innerHTML = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;

                // Re-enable form
                form.style.display = 'block';
                loadingOverlay.style.display = 'none';
                card.update({ disabled: false });
                document.getElementById('submit-button').disabled = false;
            } else if (result.paymentIntent && result.paymentIntent.status === 'succeeded') {
                form.submit();
            }

        } catch (error) {
            console.error('Payment failed:', error);
            // Reload page if caching POST fails
            location.reload();
        }
    });
});