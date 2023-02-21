var select_autor = $('select[name="Autor_correspondencia"]');
var select_autores = $('select[name="otros_autores"]');
var $select_palabras = document.querySelector("#id_palabra");
let opciones = document.getElementById('id_tipo_trabajo')
let cajaTexto = document.getElementById("tabla")
var pal_claves = "";
var keywordsN = "";

const MAXIMO_TAMANIO_BYTES = 5000000; // 1MB = 1 millón de bytes


var trabajo={
    items : {
        tipo_trabajo: '',
        subTipo_trabajo: '',
        titulo : '',
        Autor_correspondencia:'',
        otros_autores :[],
        autores_ingreso :[],
        observaciones : '',
        institucion_principal: '',
        resumen_esp : '',
        palabras_claves: [],
        resumen_ingles : '',
        keywords: [],
        curso: '',
        manuscritos : [],
        tablas : []
    },
}

    $(function () {
        /* 
        Función que recibe los eventos en el formulario de registro de trabajo científico.
        Algunos eventos son: Select2 para autores, instituciones, palabras claves y keywords; cambios en lista desplegable, acciones en botones, abrir o cerrar modales y envío de formularios.
        NOTA: Todos los archivos js también hay que crearlos en la carpeta staticfiles en el mismo orden para que funcionen en producción.
        */
        
        $('#id_tipo_trabajo').on('change',function(){
            var selectValor = $(this).val();    
            if (selectValor === 'E-poster') {
                $('#id_tabla').prop('hidden', true);
                $('#tablaLabel_id').prop('hidden', true);
                $('#subtipoLabel_id').prop('hidden', true);
                $('#manuscritosLabel_id').prop('hidden', true);
                $('#eposterLabel_id').prop('hidden', false);
                $('#id_subtipo_trabajo').prop('hidden', true);
                $('#id_subtipo_trabajo').prop('required', false);
                $('#autorIN_id').prop('hidden', true);
                $('#id_autorIN').prop('required', false);

            }
            else if (selectValor === 'Ingreso') {
                $('#eposterLabel_id').prop('hidden', true);
                $('#manuscritosLabel_id').prop('hidden', false);
                $('#id_tabla').prop('hidden', false);
                $('#tablaLabel_id').prop('hidden', false);
                $('#subtipoLabel_id').prop('hidden', false);
                $('#id_subtipo_trabajo').prop('hidden', false);
                $('#id_subtipo_trabajo').prop('required', true);                
                $('#autorIN_id').prop('hidden', false);
                $('#id_autorIN').prop('required', true);
            }
            else {
                $('#eposterLabel_id').prop('hidden', true);
                $('#manuscritosLabel_id').prop('hidden', false);
                $('#id_tabla').prop('hidden', false);
                $('#tablaLabel_id').prop('hidden', false);
                $('#subtipoLabel_id').prop('hidden', false);
                $('#id_subtipo_trabajo').prop('hidden', false);
                $('#id_subtipo_trabajo').prop('required', true);
                $('#autorIN_id').prop('hidden', true);
                $('#id_autorIN').prop('required', false);
            
            }
        });
        $('#id_curso').on('change',function(){
            var selectValor = $(this).val();
            const csrf2 = document.getElementsByName('csrfmiddlewaretoken')[0].value

            $.ajax({
                delay: 250,
                type: 'POST',
                url: window.location.pathname,
                data: {curso_id: selectValor, action:'search_curso' },
                
                success: function (data) {
                    if (data['error']) {
                        message_error(data['error']);
                        $('#botonEnviar').prop('hidden', true);
                        $('#botonEnviar').prop('disabled', true);

                    }
                    else{
                        $('#botonEnviar').prop('hidden', false);
                        $('#botonEnviar').prop('disabled', false);

                    }
                    return {                        
                        results: data
                    };
                    
                },
                error: function(data) {

                    alert(data);
                    $('#observaciones').val("");
                   }
              }) 
        });
        $('.select2').select2({
            theme: "bootstrap4",
            language: 'es',
        });        

        $('select[name="Autor_correspondencia"]').select2({
            theme: "bootstrap4",
            language: 'es',
            allowClear: true,
            placeholder: 'Ingrese un Nombre o apellido',
            minimumInputLength: 1,
        });
        $('select[name="autor"]').select2({
            theme: "bootstrap4",
            language: 'es',
            placeholder: 'Ingrese un Nombre o apellido',
            minimumInputLength: 1,
        });
        $('select[name="autorIN"]').select2({
            theme: "bootstrap4",
            language: 'es',
            placeholder: 'Ingrese un Nombre o apellido',
            minimumInputLength: 1,
        });
        $('select[name="institucion_principal"]').select2({
            theme: "bootstrap4",
            language: 'es',
            allowClear: true,
            ajax: {
                delay: 250,
                type: 'POST',
                url: window.location.pathname,
                data: function (params) {
                    var queryParameters = {
                        term: params.term,
                        action: 'search_institucion'
                    }
                    return queryParameters;
                },
                processResults: function (data) {
                    return {                        
                        results: data
                    };
                },
            },
            placeholder: 'Ingrese una institucion',
            minimumInputLength: 1,
        });
        $('select[name="institucion"]').select2({
            theme: "bootstrap4",
            language: 'es',
            allowClear: true,
            ajax: {
                delay: 250,
                type: 'POST',
                url: window.location.pathname,
                data: function (params) {
                    var queryParameters = {
                        term: params.term,
                        action: 'search_institucion'
                    }
                    return queryParameters;
                },
                processResults: function (data) {
                    return {                        
                        results: data
                    };
                },
            },
            placeholder: 'Ingrese una institucion',
            minimumInputLength: 1,
        });
        $('select[name="palabra"]').select2({
            theme: "bootstrap4",
            language: 'es',
            allowClear: true,
            ajax: {
                delay: 250,
                type: 'POST',
                url: window.location.pathname,
                data: function (params) {
                    var queryParameters = {
                        term: params.term,
                        action: 'search_palabrasClaves'
                    }
                    return queryParameters;
                },
                processResults: function (data) {
                    return {                        
                        results: data
                    };
                },
            },
            placeholder: 'Ingrese una palabra clave',
            minimumInputLength: 1,
        });
        $('select[name="keyword"]').select2({
            theme: "bootstrap4",
            language: 'es',
            allowClear: true,
            ajax: {
                delay: 250,
                type: 'POST',
                url: window.location.pathname,
                data: function (params) {
                    var queryParameters = {
                        term: params.term,
                        action: 'search_keywords'
                    }
                    return queryParameters;
                },
                processResults: function (data) {
                    return {                        
                        results: data
                    };
                },
            },
            placeholder: 'Ingrese una keyword',
            minimumInputLength: 1,
        });

        $('.btnAddAutor').on('click', function () {
            $('#autoresModal').modal('show');
        });
        $('.btnAddAutor2').on('click', function () {
            $('#autoresModal2').modal('show');
        });
        $('.btnAddInst').on('click', function () {
            $('#institucionModal').modal('show');
        });
        $('.btnAddInst2').on('click', function () {
            $('#institucionModal2').modal('show');
        });
        $('.btnAddPalC').on('click', function () {
            $('#palabras_claveModal').modal('show');
        });
        $('.btnAddKeyword').on('click', function () {
            $('#keywordsModal').modal('show');
        });

        $('#autoresModal').on('hidden.bs.modal', function (e) {
            $('#Autor_form1').trigger('reset');
        });
        $('#autoresModal2').on('hidden.bs.modal', function (e) {
            $('#Autor_form2').trigger('reset');
        });
        $('#institucionModal').on('hidden.bs.modal', function (e) {
            $('#Inst_form1').trigger('reset');
        });
        $('#institucionModal2').on('hidden.bs.modal', function (e) {
            $('#Inst_form12').trigger('reset');
        });
        $('#palabras_claveModal').on('hidden.bs.modal', function (e) {
            $('#palC_form').trigger('reset');
        });
        $('#keywordsModal').on('hidden.bs.modal', function (e) {
            $('#Keyw_form').trigger('reset');
        });
        $('#Autor_form1').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'create_autor1');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de crear al siguiente Autor?', parameters, function (response) {
                    //console.log(response);
                    var newOption = new Option(response.full_name, response.id, false, true);
                    $('select[name="Autor_correspondencia"]').append(newOption).trigger('change');
                    /* $('select[name="autor"]').append(newOption).trigger('change');
 */
                    $('#autoresModal').modal('hide');
                });
        });

        $('#Autor_form2').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'create_autor2');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de registrar al siguiente Autor?', parameters, function (response) {
                    console.log(response);
                    var newOption = new Option(response.full_name, response.id, false, true);
                    /* $('select[name="Autor_correspondencia"]').append(newOption).trigger('change'); */
                    $('select[name="autor"]').append(newOption).trigger('change');

                    $('#autoresModal2').modal('hide');
                });
        });
        $('#Inst_form1').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'create_institucion');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de registrar la siguiente institución?', parameters, function (response) {
                    message_success("Institución creada con exito!");
                    var newOption = new Option(response.institucion, response.id, false, true);
                    $('select[name="institucion_principal"]').append(newOption).trigger('change');

                    $('#institucionModal').modal('hide');
                });
        });
        $('#Inst_form2').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'create_institucion');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de registrar la siguiente institución?', parameters, function (response) {
                    message_success("Institución creada con exito!");
                    var newOption = new Option(response.institucion, response.id, false, true);
                    $('select[name="institucion"]').append(newOption).trigger('change');

                    $('#institucionModal').modal('hide');
                });
        });
        $('#palC_form').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'agregar_palabras_claves');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de registrar la siguiente Palabra clave?', parameters, function (response) {
                    message_success("Palabra clave creada con exito!");
                    var newOption = new Option(response.palabra, response.id, false, true);
                    $('select[name="palabra"]').append(newOption).trigger('change');

                    $('#palabras_claveModal').modal('hide');
                });
        });
        $('#Keyw_form').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            parameters.append('action', 'agregar_keywords');
            submit_with_ajax(window.location.pathname, 'Notificación',
                '¿Estas seguro de registrar la siguiente Keyword?', parameters, function (response) {
                    message_success("Keyword creada con exito!");
                    var newOption = new Option(response.keyword, response.id, false, true);
                    $('select[name="keyword"]').append(newOption).trigger('change');

                    $('#keywordsModal').modal('hide');
                });
        });
        $('#trabajo_form').on('submit', function (e) {
            e.preventDefault();    
            trabajo.items.tipo_trabajo = $('select[name="tipo_trabajo"]').val();
            trabajo.items.subTipo_trabajo = $('select[name="subtipo_trabajo"]').val();
            trabajo.items.titulo = $('input[name="titulo"]').val();
            trabajo.items.Autor_correspondencia = $('select[name="Autor_correspondencia"]').val();
            trabajo.items.otros_autores = $('select[name="autor"]').val();
            trabajo.items.autores_ingreso = $('select[name="autorIN"]').val();
            trabajo.items.observaciones = $('input[name="observaciones"]').val();
            trabajo.items.institucion_principal = $('select[name="institucion_principal"]').val();
            trabajo.items.otras_instituciones = $('select[name="institucion"]').val();
            trabajo.items.resumen_esp = $('input[name="resumen_esp"]').val();
            trabajo.items.palabras_claves = $('select[name="palabra"]').val();
            trabajo.items.resumen_ingles = $('input[name="resumen_ingles"]').val();
            trabajo.items.keywords = $('select[name="keyword"]').val();
            trabajo.items.curso = $('select[name="curso"]').val();

            var archivos = [];
            var archivos2 = [];
            var ext =[];
            var contador = 0;
            const tamManus = $('input[name="manuscrito"]').get(0).files.length;
            const tamTablas = $('input[name="tabla"]').get(0).files.length;
            
            for (var i = 0; i < tamManus; ++i) {
                archivos.push($('input[name="manuscrito"]').get(0).files[i]);
                ext[i] = archivos[i].name.split('.').pop();
                ext[i] = ext[i].toLowerCase();
                if (trabajo.items.tipo_trabajo !='E-poster') {
                    if (archivos[i].size > MAXIMO_TAMANIO_BYTES) {
                        const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
                        alert(`El tamaño máximo del archivo ${archivos[i].name} debe ser menor a ${tamanioEnMb} MB`);
                        contador ++;
                    }
                    
                    else if (ext[i] === "docx" ||  ext[i] === "doc") {
                        trabajo.items.manuscritos.push($('input[name="manuscrito"]').get(0).files[i].name);
                        
                    } 
                    else{
                        alert(`El  archivo ${archivos[i].name} debe ser documento word`);
                        contador ++;
                    }
                }
                else{
                    if (ext[i] === "pptx" || ext[i] ==="ppt" || ext[i] ==="mp4" || ext[i] ==="mov" || ext[i] ==="avi") {
                        if (archivos[i].size > 	150000000 ) {
                            const tamanioEnMb = 	150000000  / 1000000;
                            alert(`El tamaño máximo del archivo ${archivos[i].name} debe ser menor a ${tamanioEnMb} MB`);
                            contador ++;
                        }
                        else{
                            trabajo.items.manuscritos.push($('input[name="manuscrito"]').get(0).files[i].name);
                        }
                        
                    } 
                    else{
                        alert(`El  archivo ${archivos[i].name} debe ser documento powerPoint o video`);
                        contador ++;
                    }
                }
                
            };
            for (var i = 0; i < tamTablas; ++i) {
                archivos2.push($('input[name="tabla"]').get(0).files[i]);
                ext[i] = archivos2[i].name.split('.').pop();
                ext[i] = ext[i].toLowerCase();
                if (archivos2[i].size > MAXIMO_TAMANIO_BYTES) {
                    const tamanioEnMb = MAXIMO_TAMANIO_BYTES / 1000000;
                    alert(`El tamaño máximo del archivo ${archivos2[i].name} debe ser menor a ${tamanioEnMb} MB`);
                }
                else{
                    trabajo.items.tablas.push($('input[name="tabla"]').get(0).files[i].name);
                }
            };
            
            trabajo.items.autores_ingreso.forEach(element => {
                if (element === null || element.trim().length === 0) {
                    trabajo.items.autores_ingreso.shift();
                } 
            });

            if (contador == 0) {
                var parameters = new FormData();
                parameters.append('action', $('input[name="action"]').val());
                parameters.append('trabajo', JSON.stringify(trabajo.items));
                for (var i = 0; i < $('input[name="manuscrito"]').get(0).files.length; ++i) {
                    parameters.append('manuscritos', document.getElementById('id_manuscrito').files[i]);                    
                }
                for (var i = 0; i < $('input[name="tabla"]').get(0).files.length; ++i) {
                    parameters.append('tablas', document.getElementById('id_tabla').files[i]);                    
                }
                if (trabajo.items.autores_ingreso.length >2) {
                    message_error("Solo se pueden agregar dos autores de ingreso");
                } else {
                    submit_trabajo_with_ajax(window.location.pathname, 'Notificación', 'Si hay algún error al enviar el trabajo científico, por favor tomar captura al error y enviarlo al correo revistacolombiana@sccot.org.co junto con el trabajo científico y los datos solicitados en el formulario para que este pueda ser validado. Esto solo puede ser enviado en el rango de fechas de la convocatoria del curso. No se aceptan trabajos enviados después de esta fecha', parameters, function () {
                    message_success("Trabajo registrado con exito!");
                    location.href = '/';
                });
                }
            }            
        });
    });