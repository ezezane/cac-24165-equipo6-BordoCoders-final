
// Validar si el mail es igual al mail confirmado
function validarEmail() {
    var mail = document.getElementById("email").value;
    var confirmmail = document.getElementById("conf-email").value;

    if (mail !== confirmmail) {
        alert("Confirme nuevamente el email ingresado");
        return false;
    }
    return true;
}


document.querySelector("form")
    .addEventListener("submit", e => {
        e.preventDefault()
        alert("Formulario enviado exitosamente!")
        location.reload()
    })