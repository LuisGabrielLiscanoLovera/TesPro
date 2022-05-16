axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoProduccion(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +
        '<div class="col-sm-1">' +
        '</div>' +
        '<script type="application/javascript">' + 'formProduccionOP(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +

        '<div class="col-sm-3"><div id="FormuProduccionOP-' + row.id +
        '"><template>' +

        '<form @submit.prevent="submitFormProduccion" class="form dark">' + '<div hidden=True>{% csrf_token %}</div>' +


        '<select  class="form-control" v-model="selectIDPatinadorProduccion" id="OccionId_pantinador-' + row.id +
        '"><option  value="">Selecciones Patinador</option>' +
        '<option  v-for="option in allPatinadoresProduccions" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select>' +




        '<select  id="OccionId_talla-' + row.id +
        '" class="form-control" v-model="selectIdTallaProduccion"><option  value="">Selecciones Talla</option>' +
        '<option id="id_talla"  v-for="(optionTalla) in allTallasProduccions"  v-bind:value="optionTalla.id">[[optionTalla.num_talla]] / [[optionTalla.nom_talla]]</option></select>' +


        '<select  id="OccionId_tarea-' + row.id +
        '" class="form-control" v-model="selectIdTareaProduccion"><option   value="">Selecciones Tarea</option>' +
        '<option id="id_tarea"  v-for="(optionTarea) in allTareasProduccions" v-bind:value="optionTarea.id">[[optionTarea.nom_tarea]] / [[optionTarea.detalle]]</option></select>' +





        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +




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
        '<div class="col-sm-12">' +
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
                selectIdTareaProduccion: '',
                selectIdTallaProduccion: '',
                selectIDPatinadorProduccion: '',
                usuario: idUsuario,
                id_OP: idOperacion,

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
                    .get('/despacho/lista_patinadoresAct/')
                    .then((resp) => {
                        this.allPatinadoresProduccions = resp.data
                    })
                    .catch(error => console.log(error));
                axios
                    .get('/talla/tallaOP-list/?idOp=' + idOperacion)
                    .then((resp) => {
                        this.allTallasProduccions = resp.data;

                    })
                    .catch(error => console.log(error));

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
                [1, "desc"]
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