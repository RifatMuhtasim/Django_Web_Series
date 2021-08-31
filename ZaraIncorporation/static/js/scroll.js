// Scroll Navbar 

$(window).scroll(function(e){
        if(window.innerHeight < 500){
                if($(document).scrollTop() >220){
                        $('#header').addClass('scroll');
                }
                else{
                        $('#header').removeClass('scroll');
                }
        }
        else{
                if($(document).scrollTop()> 520){
                        $('#header').addClass('scroll');
                }
                else{
                        $('#header').removeClass('scroll');
                }
        }
})