$(document).ready(function () {

    $('[data-toggle="popover"]').popover();

    var max_quantity = $( "input[name=stock_quantity]" ).val();

    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(productId) {
        var currentValue = parseInt($(`#id_qty_${productId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue >= max_quantity;
        $(`#decrement-qty_${productId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${productId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for (var i = 0; i < allQtyInputs.length; i++) {
        var productId = $(allQtyInputs[i]).data('product_id');
        handleEnableDisable(productId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function () {
        var productId = $(this).data('product_id');
        handleEnableDisable(productId);
        var currentValue = parseInt($(this).val());
        if (currentValue > max_quantity){
            $(this).popover('show');
        };
    });
    // Increment quantity
    $('.increment-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        var productId = $(this).data('product_id');
        handleEnableDisable(productId);
    });
    // Decrement quantity
    $('.decrement-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        var productId = $(this).data('product_id');
        handleEnableDisable(productId);
    });
});