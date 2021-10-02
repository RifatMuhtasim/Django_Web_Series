
function checkEmail(event){
    
    var name = $('#name').val();
    var email = $('#email').val();
    var text = $('#text').val();
    var errormessage = $('#errormessage');
    errormessage = errormessage.empty()

    if(name.length <= 5){
        event.preventDefault();
        errormessage.append('<div> Please Enter Your Full Name </div>')
    }

    if(text.length <= 10){
        event.preventDefault();
        errormessage.append('<div> Please Enter A valid Message </div>')
    }

    if(!(email.length >=5 && email.include('@') && email.include('.'))){
        event.preventDefault();
        errormessage.append('<div> Please Enter A Valid Email </div>')
    }

console.log("Email is Successfully Running")
}


// https://formsubmit.co/tablab.bd@gmail.com