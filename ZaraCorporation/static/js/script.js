

// Add smooth scrolling to all links
// https://www.w3schools.com/howto/howto_css_smooth_scroll.asp
$("a").on('click', function(event) {
    if (this.hash !== "") {
    event.preventDefault();
    var hash = this.hash;
  
    $('html, body').animate({
        scrollTop: $(hash).offset().top
    }, 400, function(){
    window.location.hash = hash;
    });
} // End if
});