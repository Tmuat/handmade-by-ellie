$(document).ready(function () {
    // Creating a form for the delivery selection
    $("#select-go").click(function () {
        var actionSelected = $("#select-options option:selected").val();

        if (actionSelected == "dispatched") {
            $("#select-form").attr('action', "/store-admin/dispatch/");
            $("#select-form").submit();
        } else if (actionSelected == "completed") {
            $("#select-form").attr('action', "/store-admin/complete/");
            $("#select-form").submit();
        };
    });
});