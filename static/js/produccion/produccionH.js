axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoProduccionHistorial(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formProduccionOPHistorial(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="FormuProduccionOPHistorial-' + row.id + '">' +
        '<template>' +
        '<form @submit.prevent="submitFormProduccion" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +
        '<div class="row">' +

        '<div class="col-md-6 " style="position:absolute; left:0; margin: 10px 0 0 10px">' +
        '<div id="sectIntegreOC-' + row.id + '" class="table animated fadeIn resutatatIntegrante-' + row.id +
        '">' +

        '<table class="thead-dark animated fadeIn">' +
        '<thead class="">' +
        '<tr><th scope="col" class="text-center">Tareas</th><th scope="col" class="text-center">Cantidad</th></tr>' +
        '</thead>' +
        '<tbody>' +
        '<tr v-for="i in allTareaProduccions">' +

        '<td class="text-center">[[i.tarea]]</td>' +
        '<td class="text-center">[[i.cat_total_tarea]]</td>' +

        '</tr>' +

        '</tbody>' +
        '</table>' +

        '</div>' +
        '</div>' +

        '<div class="col-sm-6   offset-6" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>


        '<v-select ' +
        'v-model="selectIdIntegranteProduccion" placeholder="Seleccione Integrante" :options="allIntegrantesProduccions.map(academicClass => ({label: academicClass.nombres, value: academicClass.id}))"></v-select>' +
        '</div>' +
        '</div>' +




        '</form>' +

        '</div><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>' +
        '</div>' +
        '</template>';
}

function DetailFormatterButAccionProduccionHistorial(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +

        '<div style="overflow-x:auto;" class="col-md-10">' +
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
        '<div class="">' + '<button value="" onclick="deleteAllProduccionHistorial(' + row.id + ')"  id="buttonEliminarAllacumulado" class="btn btn-outline-danger icofont-ui-remov ">Eliminar</button>' +
        '</div>' +
        '<script type="application/javascript">' + 'ProduccionOPHistorial(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '</div>';
}

function deleteProduccionUnico(id_produccion) {

    axios.delete('eliminar_produccion/' + id_produccion + '/')
        .then(res => {
            console.log(res);
        }).catch(error => console.log(error));

}

function formProduccionOPHistorial(idOperacion, idUsuario) {
    Vue.component('v-select', VueSelect.VueSelect, {
        extends: VueSelect,

    });
    new Vue({
        el: '#FormuProduccionOPHistorial-' + idOperacion,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allPatinadoresProduccions: [],
                allTallasProduccions: [],
                allTareasProduccions: [],
                allIntegrantesProduccions: [],
                allTareaProduccions: [],
                selectIdIntegranteProduccion: '',
                selectIdTareaProduccion: '',
                selectIdTallaProduccion: '',
                selectIDPatinadorProduccion: '',
                cant_prod: '',
                name: 'pass',
                usuario: idUsuario,
                idOperacion: idOperacion,

            }
        },
        methods: {
            getProduccionDataHistorial: function() {
                ProduccionOPHistorial(idOperacion);

            },

        },
        created() {
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
                .get('/produccion/lista_patinadoresAct-prod/')
                .then((resp) => {
                    this.allPatinadoresProduccions = resp.data
                }).catch(error => console.log(error));
            axios
                .get('/talla/tallaOP-list/?idOp=' + idOperacion)
                .then((resp) => {
                    this.allTallasProduccions = resp.data;
                    console.log(this.allTallasProduccions);
                }).catch(error => console.log(error));
        },
        watch: {
            selectIdIntegranteProduccion(val) {

                axios.get('dataProduccionInte-list/', {
                    params: {
                        idIntegranteSelect: val.value,
                        idOp: idOperacion,
                    }
                }).then((resp) => {
                    this.allTareaProduccions = resp.data;
                }).catch(error => console.log(error));

            }
        },
        mounted: function() {
            this.getProduccionDataHistorial();
        }
    })
}

function ProduccionOPHistorial(idOperacion, idUsuario) {
    $(document).ready(function() {
        let table = $("#items-table-produccion-" + idOperacion).removeAttr("width").dataTable({
            ajax: {
                url: '/produccion/produccionOP-list/?idOp=' + idOperacion,
                dataSrc: ''
            },
            language: { "sProcessing": "Procesando...", "sLengthMenu": "Mostrar _MENU_ registros", "sZeroRecords": "No se encontraron resutatatIntegrantes", "sEmptyTable": "Ningún dato disponible en esta tabla", "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros", "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros", "sInfoFiltered": "(filtrado de un total de _MAX_ registros)", "sInfoPostFix": "", "sSearch": "Buscar:", "sUrl": "", "sInfoThousands": ",", "sLoadingRecords": "Cargando...", "oPaginate": { "sFirst": "Primero", "sLast": "Último", "sNext": "Siguiente", "sPrevious": "Anterior" }, "oAria": { "sSortAscending": ": Activar para ordenar la columna de manera ascendente", "sSortDescending": ": Activar para ordenar la columna de manera descendente" } },
            // scrollY: '500px',
            scrollCollapse: true,
            scrollY: "250px",
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
                { data: "delProduccion", visible: false },
            ]

        });
        $("#items-table-produccion-" + idOperacion).on("click", "button", function() {
            $("#items-table-produccion-" + idOperacion).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-produccion-" + idOperacion).DataTable().ajax.reload();
        }
    })
}

function deleteAllProduccionHistorial(idOperacion) {
    $.ajax({
        url: 'deleteAllProduccion/',

        data: {
            'idOperacion': idOperacion,
        },
        dataType: 'json',
        success: function(data) {
            window.location.reload();

        }
    });
}