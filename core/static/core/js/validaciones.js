$(document).ready(function() {
    $("#clienteFormulario").validate({
        rules: {
			txtCorreo: {
                required:true,
                minlength:4,
                maxlength:100
            },
			txtClave: {
                required:true,
                minlength:4,
                maxlength:30
            },
            txtRut: {
                required:true,
                minlength:3,
                maxlength:30
            },
            txtNombre: {
                required:true,
                minlength:3,
                maxlength:30
            },
            txtApellido: {
                required:true,
                minlength:3,
                maxlength:30
            },
            cboComuna: {
                required:true
            },
			cboProvincia: {
                required:true
            },
            cboRegion: {
                required:true
            },
            cboVivienda: {
                required:true
            },
            txtFechaNacimiento: {
                required:true,
                date:true
            }
        }
    });
});