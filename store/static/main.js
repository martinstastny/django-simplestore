$(function () {
    "use strict";

    $('img.lazy').lazyload();

    // Billing adddress toggle
    var $billingCheckboxLabel = $('#id_shipping_address-use_as_billing');
    var $billingForm = $('.js-billing-form');

    $billingCheckboxLabel.on('click', function (e) {
        $billingForm.toggleClass('hidden');
    });

});