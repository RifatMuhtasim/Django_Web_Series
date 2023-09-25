
const heroLgText = document.querySelector('.heroLgTxt');
const heroSmText = document.querySelector('.heroSmTxt');

const strHeroLgText = heroLgText.textContent;
const strHeroSmText = heroSmText.textContent;

const splitHeroLgText = strHeroLgText.split('');
const splitHeroSmText = strHeroSmText.split('');

heroLgText.textContent= '';
heroSmText.textContent= '';


for(let i= 0; i < splitHeroLgText.length; i++){
    heroLgText.innerHTML += "<span>"+ splitHeroLgText[i] + "</span>";
};
for(let j= 0; j < splitHeroSmText.length; j++){
    heroSmText.innerHTML += "<span>"+ splitHeroSmText[j] + "</span>";
}


let lgchar= 0;
let smchar= 0;

let lgtimer = setInterval(lgon, 15);
let smtimer = setInterval(smon, 15);


function lgon(){
    const spanlist = document.querySelectorAll('span')[lgchar];
    spanlist.classList.add('fade');
    lgchar++;
    if(lgchar === splitHeroLgText.length+29){
        lgcomplete();
        return;
    }
};
function smon(){
    const spanSmList = document.querySelectorAll('span')[smchar];
    spanSmList.classList.add('fade');
    smchar++;
    if(smchar === splitHeroSmText.length+4){
        smcomplete();
        return;
    }
}


function lgcomplete(){
    clearInterval(lgtimer);
    lgtimer= null;
};
function smcomplete(){
    clearInterval(smtimer);
    smtimer= null;
};

console.log(heroLgText);
console.log(heroSmText);