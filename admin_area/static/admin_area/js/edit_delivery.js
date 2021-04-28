$(document).ready(function () {
    $( ".table-form" ).click(function() {
        $(this).find("input").focus();
        $(this).find("select").focus();
    });
});