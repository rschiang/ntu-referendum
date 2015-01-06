$(document).ready(function() {
    if ($("#hero").length) {
        parallax();
    }
});

$(window).scroll(function(e) {
    if ($("#hero").length) {
        parallax();
    }
});

function parallax(){
    if( $("#hero").length > 0 ) {
        var plxBackground = $("#hero-background");
        var plxWindow = $("#hero");

        var plxWindowTopToPageTop = $(plxWindow).offset().top;
        var windowTopToPageTop = $(window).scrollTop();
        var plxWindowTopToWindowTop = plxWindowTopToPageTop - windowTopToPageTop;

        var plxBackgroundTopToPageTop = $(plxBackground).offset().top;
        var windowInnerHeight = window.innerHeight;
        var plxBackgroundTopToWindowTop = plxBackgroundTopToPageTop - windowTopToPageTop;
        var plxBackgroundTopToWindowBottom = windowInnerHeight - plxBackgroundTopToWindowTop;
        var plxSpeed = 0.27;

        plxBackground.css('top', - (plxWindowTopToWindowTop * plxSpeed) + 'px');
    }
}
