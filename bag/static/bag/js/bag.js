$(document).ready(function () {
    // Start popover for this page
    $('[data-toggle="popover"]').popover();

    // Start tooltips for this page
    $('[data-toggle="tooltip"]').tooltip();

    // var max_quantity = $( "input[name=stock_quantity]" ).val();

    // Disable +/- buttons outside 1-Max Qty range
    function handleEnableDisable(productId, maxQuantity) {
        var currentValue = parseInt($(`#id_qty_${productId}`).val());
        var maxQuantity = parseInt($(`#id_max_qty_${productId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue >= maxQuantity;
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
        var maxQuantity = parseInt($(`#id_max_qty_${productId}`).val());
        handleEnableDisable(productId);
        var currentValue = parseInt($(this).val());
        if (currentValue > maxQuantity){
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
    // Update quantity on click
    $('.update-link').click(function (e) {
        var form = $(this).prev('.update-form');
        form.submit();
    });
    // Remove product and reload on click
    $('.remove-item').click(function (e) {
        var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
        var productId = $(this).attr('id').split('remove_')[1];
        var url = `/bag/remove/${productId}/`;
        var data = { 'csrfmiddlewaretoken': csrfToken, };

        $.post(url, data)
            .done(function () {
                location.reload();
            });
    });
    // Creating a form for the delivery selection
    $(".delivery-submit").click(function () {
        var selected = [];
        $.each($("input[name='delivery-option']:checked"), function () {
            selected.push($(this).attr("id"));
            $('#id-selected').val(selected);
        });
        console.log(selected)
        $("#delivery-form").submit();
    });
});