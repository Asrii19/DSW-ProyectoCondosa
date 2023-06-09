// Define las restricciones para los numeros enteros
var numeros = /[^0-9]/g;
// Define las restricciones para los números decimales
var numerosd = /[^0-9.]/g;
// Define las restricciones para los nombres, apellidos y nombre de predio
var nombres = /[^A-Za-zñÑáéíóúÁÉÍÓÚ\s]+/g;
//Define las restricciones del correo
var correo = /^[@.\s]+/;

// Función de validación del documento de identidad
function validarDocumento() {
    let input = document.getElementById("documento");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto números)
    valor = valor.replace(numeros, "");

    // Limitar a 8 caracteres
    valor = valor.slice(0, 8);

    // Actualizar el valor del campo
    input.value = valor;
}

// Función de validación del apellido
function validarApellido() {
    let input = document.getElementById("apellidos");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto letras y espacios)
    valor = valor.replace(nombres, "");

    // Actualizar el valor del campo
    input.value = valor;
}

// Función de validación del nombre
function validarNombre() {
    let input = document.getElementById("nombres");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto letras y espacios)
    valor = valor.replace(nombres, "");

    // Actualizar el valor del campo
    input.value = valor;
}

// Función de validación del nombre del predio
function validarNombrePredio() {
    let input = document.getElementById("predio");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto letras y espacios)
    valor = valor.replace(nombres, "");

    // Actualizar el valor del campo
    input.value = valor;
}

// Función de validación del teléfono
function validarTelefono() {
    let input = document.getElementById("telefono");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto números)
    valor = valor.replace(numeros, "");

    // Limitar a 9 caracteres
    valor = valor.slice(0, 9);

    // Asegurar que el primer dígito sea 9
    if (valor.length > 0 && valor.charAt(0) !== "9") {
        valor = "9" + valor.slice(1);
    }

    // Actualizar el valor del campo
    input.value = valor;
}


// Función de validación del correo
function validarCorreo() {
    let correo = document.getElementById("correo");
    let valor = correo.value;


    // Reemplazar "@" por un vacío al inicio del valor
    valor = valor.replace(correo, "");
    // Verificar si hay un punto "." después del símbolo "@"
    const indiceArroba = valor.indexOf("@");
    const indicePunto = valor.indexOf(".", indiceArroba + 1);
    if (indicePunto === indiceArroba + 1) {
        // Si hay un punto "." inmediatamente después del "@", eliminarlo
        valor = valor.slice(0, indicePunto) + valor.slice(indicePunto + 1);
    }

    // Actualizar el valor del campo
    correo.value = valor;
}
// Función de validación del área
function validarArea() {
    let input = document.getElementById("area");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto números y el punto decimal)
    valor = valor.replace(/[^0-9.]/g, "");
    // Eliminar puntos adicionales al inicio del valor
    valor = valor.replace(/^\.+/, "");
    // Verificar si hay más de un punto decimal
    if ((valor.match(/\./g) || []).length > 1) {
        // Si hay más de un punto decimal, eliminar el último
        valor = valor.slice(0, valor.lastIndexOf("."));
    }

    // Actualizar el valor del campo
    input.value = valor;
}

function validarPersonalLimpieza() {
    let input = document.getElementById("limpieza");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto números)
    valor = valor.replace(numeros, "");

    // Actualizar el valor del campo
    input.value = valor;
}

function validarNroPuertasAcceso() {
    let input = document.getElementById("NroPuertasAcceso");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto números)
    valor = valor.replace(numeros, "");

    // Actualizar el valor del campo
    input.value = valor;
}

function validarNroBloques() {
    let input = document.getElementById("NroHabitaciones");
    let valor = input.value;

    // Eliminar caracteres no válidos (excepto números)
    valor = valor.replace(numeros, "");

    // Actualizar el valor del campo
    input.value = valor;
}

// rellenar automáticamente cuando se ponen las puertas de acceso
var nroPuertasAccesoInput = document.getElementById("NroPuertasAcceso");
var personalLimpiezaInput = document.getElementById("limpieza");
var vigilanteInput = document.getElementById("vigilante");
var administradorInput = document.getElementById("administrador");
var totalCotizadoInput = document.getElementById("total");

function actualizarVigilante() {
    var nroPuertasAcceso = parseInt(nroPuertasAccesoInput.value);
    var vigilanteValue = nroPuertasAcceso * 2 || 0;
    vigilanteInput.value = vigilanteValue;
    calcularTotalCotizado();
}

function calcularTotalCotizado() {
    var personalLimpieza = parseInt(personalLimpiezaInput.value) || 0;
    var vigilante = parseInt(vigilanteInput.value) || 0;
    var administrador = parseInt(administradorInput.value) || 0;

    var totalCotizado = (personalLimpieza + vigilante + administrador) * 100;
    totalCotizadoInput.value = totalCotizado;
}

nroPuertasAccesoInput.addEventListener("input", actualizarVigilante);
personalLimpiezaInput.addEventListener("input", calcularTotalCotizado);
vigilanteInput.addEventListener("input", calcularTotalCotizado);
administradorInput.addEventListener("input", calcularTotalCotizado);