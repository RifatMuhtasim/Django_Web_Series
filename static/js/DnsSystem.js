var btnChange = document.querySelector('#ibn');
var btnEn = document.querySelector('.IdEnable');
var btnDi = document.querySelector('.IdDisable');
var idPro = document.querySelector('#IdProtection');
var btnHtmlEn = "<h6>Id Protection</h6><button onclick='bchange()' id='ibn' class='btn btn-success IdEnable mx-1'>Enable</button>";
var btnHtmlDi = "<h6>Id Protection</h6><button onclick='bchange()' id='ibn' class='btn btn-danger IdDisable mx-1'>Disable</button>";

var toggle = document.querySelector('.toggle');
var text = document.querySelector('.resultText')

function achange(){
                var a = text.defaultValue
                if (a == "false"){
                        text.innerHTML = "true"
                }else{
                        text.innerHTML = "false"
                }        
}

function xchange(){
        var a = text.defaultValue
        if (a == "False"){
                text.innerHTML = "True"
        }else{
                text.innerHTML = "False"
        }        
}

function bchange(){
        toggle.classList.toggle('checked');
        if (toggle.classList.contains('checked')){
                text.innerHTML= 'true';
        }else{
                text.innerHTML='false';
        }
}

console.log('Long Live Bangladesh')