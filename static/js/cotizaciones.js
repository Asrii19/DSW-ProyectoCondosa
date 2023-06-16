function mostrarTabla(tab) {
    if (tab === 'pendientes') {
        document.getElementById('tabla-pendientes').style.display = 'block';
        document.getElementById('tabla-completadas').style.display = 'none';
        document.getElementById('pendientes-tab').classList.add('is-active');
        document.getElementById('completadas-tab').classList.remove('is-active');
    } else if (tab === 'completadas') {
        document.getElementById('tabla-pendientes').style.display = 'none';
        document.getElementById('tabla-completadas').style.display = 'block';
        document.getElementById('pendientes-tab').classList.remove('is-active');
        document.getElementById('completadas-tab').classList.add('is-active');
    }
}

function mostrarPopup(popupId) {
    var popup = document.getElementById(popupId);
    rellenarImportes(popupId);
    popup.classList.add("is-active");
}

function cerrarPopup(popupId) {
    var popup = document.getElementById(popupId);
    popup.classList.remove("is-active");
}

// Función para aceptar la cotización
function aceptarCotizacion(idSolicitud) {
    // Lógica para aceptar la cotización con el ID de solicitud proporcionado
    console.log("Cotización aceptada. ID de Solicitud: " + idSolicitud);
    console.log(importeJardineros);
}

// Función para rechazar la cotización
function rechazarCotizacion(idSolicitud) {
    // Lógica para rechazar la cotización con el ID de solicitud proporcionado
    console.log("Cotización rechazada. ID de Solicitud: " + idSolicitud);
}



function rellenarImportes(idSolicitud) {

    

}