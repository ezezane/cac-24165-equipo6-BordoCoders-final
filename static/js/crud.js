function validateForm(){
    // devuelve la URI (path name) actual
    var currentURL = window.location.pathname;
    // identifica el DIV para cargar los posibles mensajes de error
    var mensajeP = document.getElementById('mensaje');
    // identifica el form de CREATE / EDIT
    var form = document.getElementById('form');
    // flag para contar los errores
    var errorFlag = 0;
    // flag para cargar los mensajes de error
    var mensajeError = "";

    // marca
    var inputMarca = document.getElementById('marca');
    if (inputMarca.value == ""){
        errorFlag = errorFlag + 1;
        mensajeError = mensajeError.concat("<p>falta el nombre de la marca</p>");
    }
    // nombre
    var inputName = document.getElementById('name');
    if (inputName.value == ""){
        errorFlag = errorFlag + 1;
        mensajeError = mensajeError.concat("<p>falta el nombre del producto</p>");
    }
    // precio
    var inputPrecio = document.getElementById('precio');
    if (inputPrecio.value == ""){
        errorFlag = errorFlag + 1;
        mensajeError = mensajeError.concat("<p>falta el precio</p>");
    }
    // imagen
    if (currentURL.startsWith('/admin/crear')){
        var inputFile = document.getElementById('file');
        if (inputFile.value == ""){
            errorFlag = errorFlag + 1;
            mensajeError = mensajeError.concat("<p>falta imagen</p>");
        }
    }

    // verificación final
    if (errorFlag > 0){
        mensajeP.className = "alert alert-danger";
        mensajeP.innerHTML = mensajeError;
    } else {
        form.submit();
    }
}