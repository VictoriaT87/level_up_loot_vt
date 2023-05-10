/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// get key in text for, slice off quotation at beginning and end
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
// stripe variable from stripe script in base.html
var stripe = Stripe(stripePublicKey);
// create elements for card payment
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
// create card element
var card = elements.create('card', {
    style: style
});
// mount card elements to element div on template
card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {

    // prevent default - don't post until this function runs
    ev.preventDefault();

    // disable to prevent multiple submissions
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);

    // show blue loading arrow on payment
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // check if save info box is checked
    var saveInfo = Boolean($('#id-save-info').attr('checked'));

    // get csrf token from form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    // send token, if saved, clientsecret key to view
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };

    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {

        // get stripe confirm payment securely
        stripe.confirmCardPayment(clientSecret, {

            payment_method: {
                // get all these details on payment succeed
                // send to admin panel if webhook successful
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
            // execute function on result
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                            <span class="icon" role="alert">
                            <i class="fas fa-times"></i>
                            </span>
                            <span>${result.error.message}</span>`;
                $(errorDiv).html(html);

                // if error, remove loading icon
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);

                //if error with card, re-enable buttons to fix
                card.update({
                    'disabled': false
                });
                $('#submit-button').attr('disabled', false);
            } else { // if payment succeeds, submit form
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    });
});