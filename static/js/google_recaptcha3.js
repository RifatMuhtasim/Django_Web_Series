grecaptcha.ready(function() {
    $('#captcha').submit(function(e){
        var form = this;
        e.preventDefault()
        grecaptcha.execute('6LcQ1gkdAAAAANoaqKJD8GOJHHY42kq_POwmuXj2', {action: 'domainsearch'}).then(function(token) {
            $('#recaptcha').val(token)
            form.submit()
        });
    });
});