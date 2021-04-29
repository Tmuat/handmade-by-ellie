$(document).ready(function () {
    $( ".table-form" ).click(function() {
        $(this).find("input").focus();
    });

    $('#id_image').change(function () {
        var file = $('#id_image')[0].files[0];
        $('#id_new_image').text(`New Image: ${file.name}`);
        $('#id_new_image').removeClass('text-transparent');
    });
});