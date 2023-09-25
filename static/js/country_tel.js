const phoneInputField = document.querySelector("#phone");
const phoneInput = window.intlTelInput(phoneInputField, {utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js", });

var form = document.querySelector("#UserForm");
var countryCode = document.querySelector("#countryCode");
var dialCode = document.querySelector("#dialCode");
var phonexNumber = document.querySelector("#phoneNumber");

function process(event) {
    event.preventDefault();
    var phoneNumber = phoneInput.getNumber(intlTelInputUtils.numberFormat)
    // const phoneNumber = phoneInput.getNumber();
    const country = phoneInput.getSelectedCountryData();
    phonexNumber.setAttribute('value', `${phoneNumber}`)
    countryCode.setAttribute('value', `${country.iso2}`)
    dialCode.setAttribute('value', `${country.dialCode}`)
    form.submit()
}

// const info = document.querySelector(".alert-info");
// info.style.display = "";
// info.innerHTML = `Phone number in E.164 format: <strong>${phoneNumber} and country is ${country.iso2} and dial code is ${country.dialCode}</strong>`;
