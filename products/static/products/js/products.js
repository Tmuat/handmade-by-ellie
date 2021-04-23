// Code adapted from https://codepen.io/RonaldElzen/pen/KWpZov
let state = "minimized";
$('#sidenav-toggle').click(function () {
    if (state == "minimized") {
        $('.sidebar').css('margin-left', '0px');
        $('#all_products').addClass('d-none');
        $('#sidenav-toggle').addClass('d-none');
        state = "expanded";
    }
})
// Code to check if screen resized and filters are hidden
$(window).resize(function () {
    var width = $(window).width();
    if (width > 768) {
        $('.sidebar').removeAttr('style');
        $('#all_products').removeClass('d-none');
        $('#sidenav-toggle').removeClass('d-none');
    }
});


// Code taken from Boutique Ado

$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})

// Code for the side filter

$("#filter").click(function(){
    var currentUrl = new URL(window.location);
    var category = [];
    var selectedVal = "";

    $.each($("input[name='category_select']:checked"), function(){
        category.push($(this).val());
    });

    $.each($("input[name='sort_radio']:checked"), function(){
        selectedVal = selectedVal.replace("", $(this).val());
    });

    if (category.length > 0) {
        var category_string = category.join(",")
        currentUrl.searchParams.set("category", category_string);
    }

    if (selectedVal != "") {
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
    }
    
    window.location.replace(currentUrl);
});