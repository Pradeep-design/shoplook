const userNameInput = document.getElementById('form3Example1cg')
userNameInput.addEventListener("input",function(event){
    if (userNameInput.validity.typeMismatch){
        userNameInput.setCustomValidity("please type username")
    }
    else{
        userNameInput.setCustomValidity("")
    }
})

const emailInput = document.getElementById("form3Example3cg");


emailInput.addEventListener("input",function(event){
    if(emailInput.validity.typeMismatch) {
        emailInput.setCustomValidity("please enter a valid email address")
    }

    else{
        emailInput.setCustomValidity("")
    }
})

const passwordInput = document.getElementById('form3Example4cg')
const regexExp = /^(?=,*[a-z](?=,*[A-Z])(?=,*\d)())

function strongPassword()
{
}

function validatePassword(event){

   const passwordInput = document.getElementById('form3Example4cg')
   const repeatPasswordInput = document.getElementById('form3Example4cdg')

   if (passwordInput.value !== repeatPasswordInput.value)
   {
    const errorMessage = document.createElement('p');
    errorMessage.textContent = 'password is no match';
    document.body.appendChild(errorMessage)
    event.preventDefault();
   }
   else{
    document.getElementById('myForm').submit();
   }
}