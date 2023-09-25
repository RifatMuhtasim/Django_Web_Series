
const heroLgText = document.querySelector('.heroLgTxt');
const strHeroLgText = heroLgText.textContent;
const splitHeroLgText = strHeroLgText.split('');
heroLgText.textContent= '';

for(let i= 0; i < splitHeroLgText.length; i++){
    heroLgText.innerHTML += "<span>"+ splitHeroLgText[i] + "</span>";
};

let lgchar= 0;

let lgtimer = setInterval(lgon, 40);

function lgon(){
    const spanlist = document.querySelectorAll('span')[lgchar];
    spanlist.classList.add('fade');
    lgchar++;
    if(lgchar === splitHeroLgText.length+29){
         lgcomplete();
         return;
    }
};

function lgcomplete(){
   clearInterval(lgtimer);
   lgtimer= null;
};

console.log(heroLgText);