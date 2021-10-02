
function getOffSet(){
    var _offset = 0;
    var windowHeight = window.innerHeight;
    return _offset;
}

function setParallaxPosition($doc, multiplier, $object){
    var offset = getOffSet();
    var fromTop= $doc.scrollTop();
    bgCss = 'center '+ (multiplier * fromTop - offset)  + 'px';
    $object.css({'background-position': bgCss})
}

var backgroundImageParallax = function($object, multiplier, forceSet){
    multiplier = typeof multiplier !== 'undefined' ? multiplier : 0.2;
    multiplier =  multiplier -1;
    var $doc = $(document);
    if(forceSet){
        setParallaxPosition($doc, multiplier, $object);
    }
    else{
        $(window).scroll(function(){
            setParallaxPosition($doc, multiplier, $object);
        })
    }
}

$(function(){
    backgroundImageParallax($('.heroimg'), 0.7, false);
    window.addEventListener('resize', function(){
        backgroundImageParallax($('.heroimg'), 0.9, true)
    }, true)
})