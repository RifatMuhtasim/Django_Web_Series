console.log('Hellow I am from Password show')
// Recaptcha v2
const password = document.getElementById('password')
const toggley = document.getElementById('toggley')
const eye = document.getElementById('eye')


function show_hide(){
    if(password.type === 'password'){
        password.setAttribute('type', 'text');
        toggley.classList.add('hide');
        eye.classList.remove('fa-eye-slash');
        eye.classList.add('fa-eye');
    }else{
        password.setAttribute('type', 'password');
        toggley.classList.remove('hide');
        eye.classList.remove('fa-eye');
        eye.classList.add('fa-eye-slash');
    }
}

const password2 = document.getElementById('password2')
const toggley2 = document.getElementById('toggley2')
const eye2 = document.getElementById('eye2')

function show_hide2(){
    if(password2.type === 'password'){
        password2.setAttribute('type', 'text');
        toggley2.classList.add('hide');
        eye2.classList.remove('fa-eye-slash');
        eye2.classList.add('fa-eye');
    }else{
        password2.setAttribute('type', 'password');
        toggley2.classList.remove('hide');
        eye2.classList.remove('fa-eye');
        eye2.classList.add('fa-eye-slash');
    }
}


// Recaptcha v2

function search(){
    // e.preventDefault();
    grecaptcha.ready(function(){
        console.log('i am done');
        grecaptcha.execute('6LcQ1gkdAAAAANoaqKJD8GOJHHY42kq_POwmuXj2', {action: 'domainsearch'}).then(function(token){
            console.log('i am done 2')
            document.getElementById('g-recaptcha-response').value = token;
        });
    });
}
