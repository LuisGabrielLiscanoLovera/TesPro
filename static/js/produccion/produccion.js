axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoProduccion(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +
        '<script type="application/javascript">' + 'formProduccionOP(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +





        '<div id="FormuProduccionOP-' + row.id + '">' +
        '<template>' +

        '<form @submit.prevent="submitFormProduccion" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +


        '<div class="col-mx-9">' +
        '<div class="form-group">' +

        '<select  id="OccionId_integrante_prod-' + row.id +
        '" class="form-select form-select-sm form-control" v-model="selectIdIntegranteProduccion"><option value="">Selecciones Integrante</option>' +
        '<option id="id_integrante"  v-for="(optionIntegrante) in allIntegrantesProduccions" v-bind:value="optionIntegrante.id">[[optionIntegrante.nombres]]  [[optionIntegrante.apellidos]]</option></select></div>' +
        '</div>' +

        '<div class="col-mx-9">' +
        '<div class="form-group">' +
        '<select  class="form-select form-select-sm form-control" v-model="selectIDPatinadorProduccion" id="OccionId_pantinador_prod-' + row.id +
        '"><option  value="">Selecciones Patinador</option>' +
        '<option  v-for="option in allPatinadoresProduccions" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select></div>' +
        '</div>' +

        '<div class="col-mx-9">' +
        '<div class="form-group">' +
        '<select  id="OccionId_tarea-' + row.id +
        '" class="form-select form-select-sm form-control " v-model="selectIdTareaProduccion"><option value="">Selecciones Tarea</option>' +
        '<option id="id_tarea"  v-for="(optionTarea) in allTareasProduccions" v-bind:value="optionTarea.id">[[optionTarea.nom_tarea]] / [[optionTarea.detalle]]</option></select></div>' +
        '</div>' +

        '<div class="col-mx-9">' +
        '<div class="form-group">' +
        '<select  id="OccionId_talla-' + row.id +
        '" class="form-select form-control form-select-sm" v-model="selectIdTallaProduccion"><option value="">Selecciones Talla</option>' +
        '<option id="id_talla"  v-for="(optionTalla) in allTallasProduccions"  v-bind:value="optionTalla.id">[[optionTalla.num_talla]] / [[optionTalla.nom_talla]]</option></select></div>' +
        '</div>' +

        '<div class="col-mx-9">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_prod" name="cant_produccion-' + row.id +
        '"  type="number" v-model="cant_prod" required/> </div>' +
        '</div>' +

        '<div class="col-mx-9">' +
        '<div class="form-group  "><input class="form-control btn btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +

        '</template>' +
        '</div>' +

        '</div>';





}

function DetailFormatterButAccionProduccion(index, row) {
    //r = parseInt("[[progressRest]]");

    return '<div class="row">' +
        //'<div class="col-sm-1">' +
        //'</div>' +
        '<div class="col-mx-9">' +
        '<table  class="table animated fadeIn "  id="items-table-produccion-' + row.id +
        '">' +
        '<thead class="thead-dark">' +
        '<tr>' +
        '<th class="text-center">Nombre</th>' +
        '<th class="text-center">Apellido</th>' +
        '<th class="text-center">Tarea</th>' +
        '<th class="text-center">Talla</th>' +
        '<th class="text-center">Cantidad</th>' +
        '<th class="text-center">Fecha</th>' +
        '<th class="text-center">Eliminar</th>' +
        '</tr>' +
        '</thead>' +
        '<tbody calss="table-striped table  table-sm  table-bordered table-hover" id="produccionKill-' + row.id + '">' +
        '</tbody>' +
        '</table>' +
        '<script type="application/javascript">' + 'ProduccionOP(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '</div>';
}




function formProduccionOP(idOperacion, idUsuario) {
    new Vue({
        el: '#FormuProduccionOP-' + idOperacion,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allPatinadoresProduccions: [],
                allTallasProduccions: [],
                allTareasProduccions: [],
                allIntegrantesProduccions: [],
                selectIdIntegranteProduccion: '',
                selectIdTareaProduccion: '',
                selectIdTallaProduccion: '',
                selectIDPatinadorProduccion: '',
                cant_prod: '',
                usuario: idUsuario,
                idOperacion: idOperacion,

            }
        },
        methods: {
            getProduccionData: function() {
                ProduccionOP(idOperacion);
                axios
                    .get('/tarea/tarea-list/')
                    .then((resp) => {
                        this.allTareasProduccions = resp.data;
                    })
                    .catch(error => console.log(error));
                axios
                    .get('/integrante/integrante-list/')
                    .then((resp) => {
                        this.allIntegrantesProduccions = resp.data
                    }).catch(error => console.log(error));
                axios
                    .get('/despacho/lista_patinadoresAct/')
                    .then((resp) => {
                        this.allPatinadoresProduccions = resp.data
                    }).catch(error => console.log(error));
                axios
                    .get('/talla/tallaOP-list/?idOp=' + idOperacion)
                    .then((resp) => {
                        this.allTallasProduccions = resp.data;
                    }).catch(error => console.log(error));
            },
            submitFormProduccion: function() {
                var OccionId_integrante_prod = $('select[id="OccionId_integrante_prod-' + this.idOperacion + '"]').val().trim();
                var OccionId_pantinador_prod = $('select[id="OccionId_pantinador_prod-' + this.idOperacion + '"]').val().trim();
                var OccionId_tarea = $('select[id="OccionId_tarea-' + this.idOperacion + '"]').val().trim();
                var OccionId_talla = $('select[id="OccionId_talla-' + this.idOperacion + '"]').val().trim();
                var cantidad = $('input[name="cant_produccion-' + this.idOperacion + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if


                axios.post('/produccion/create/', {
                    idOperacion: idOperacion,
                    usuario: idUsuario,
                    OccionId_integrante_prod: OccionId_integrante_prod,
                    OccionId_pantinador_prod: OccionId_pantinador_prod, //l
                    OccionId_tarea: OccionId_tarea,
                    OccionId_talla: OccionId_talla,
                    cantidadProd: cantidad,

                }).then(response => {
                    console.log(response);
                })










            }
        },



        mounted: function() {
            this.getProduccionData();
        }

    })



}

function ProduccionOP(idOperacion, idUsuario) {
    $(document).ready(function() {
        var table = $("#items-table-produccion-" + idOperacion).removeAttr("width").dataTable({
            ajax: {
                url: '/produccion/produccionOP-list/?idOp=' + idOperacion,
                dataSrc: ''
            },
            language: { "sProcessing": "Procesando...", "sLengthMenu": "Mostrar _MENU_ registros", "sZeroRecords": "No se encontraron resultados", "sEmptyTable": "Ningún dato disponible en esta tabla", "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros", "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros", "sInfoFiltered": "(filtrado de un total de _MAX_ registros)", "sInfoPostFix": "", "sSearch": "Buscar:", "sUrl": "", "sInfoThousands": ",", "sLoadingRecords": "Cargando...", "oPaginate": { "sFirst": "Primero", "sLast": "Último", "sNext": "Siguiente", "sPrevious": "Anterior" }, "oAria": { "sSortAscending": ": Activar para ordenar la columna de manera ascendente", "sSortDescending": ": Activar para ordenar la columna de manera descendente" } },
            // scrollY: '500px',

            scrollCollapse: true,
            //scrollY: "450px",

            order: [
                [5, "dsc"]
            ],

            columns: [
                { data: "nomIntegrante" },
                { data: "apeIntegrante" },
                { data: "nomTarea" },
                { data: "nom_talla" },
                { data: "can_terminada" },
                { data: "created_at" },
                { data: "delProduccion" },
            ]

        });


    })
}