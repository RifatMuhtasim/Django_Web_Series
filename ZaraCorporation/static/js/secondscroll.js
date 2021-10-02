// Scroll Navbar 

$(window).scroll(function(e){
        if(window.innerHeight < 500){
                if($(document).scrollTop() >1){
                        $('#header').addClass('scroll');
                }
                else{
                        $('#header').removeClass('scroll');
                }
        }
        else{
                if($(document).scrollTop()> 1){
                        $('#header').addClass('scroll');
                }
                else{
                        $('#header').removeClass('scroll');
                }
        }
})