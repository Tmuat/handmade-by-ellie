// Code adapted from https://codepen.io/RonaldElzen/pen/KWpZov
let state = "minimized";
$('#sidenav-toggle').click(function () {
    if (state == "expanded") {
        $('.sidebar').css('margin-left', '-100%');
        state = "minimized";
    } else {
        if (state == "minimized") {
            $('.sidebar').css('margin-left', '0px');
            state = "expanded";
        }
    }
})
// Code to check if screen resized and filters are hidden
$(window).resize(function () {
    var width = $(window).width();
    if (width > 768) {
        $('.sidebar').removeAttr('style');
    }
});