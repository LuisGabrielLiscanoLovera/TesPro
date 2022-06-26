axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoProduccion(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formProduccionOP(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="FormuProduccionOP-' + row.id + '">' +
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


        '<div class="col-sm-6 mb-2 offset-6  ">' +
        '<div class="form-group">' +

        '<v-select ' +
        'v-model="selectIDPatinadorProduccion"  placeholder="Seleccione Patinador"  :options="allPatinadoresProduccions.map(academicClassPatinador => ({label: academicClassPatinador.nomPatinador+\' \'+academicClassPatinador.apellPatinador, value: academicClassPatinador.id}))"></v-select>' +
        '</div>' +
        '</div>' +



        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<v-select ' +
        'v-model="selectIdTareaProduccion"  placeholder="Seleccione Tarea"  :options="allTareasProduccions.map(academicClassTarea => ({label: academicClassTarea.nom_tarea+\' \'+academicClassTarea.detalle, value: academicClassTarea.id}))"></v-select>' +

        '</div>' +
        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<v-select ' +
        'v-model="selectIdTallaProduccion"  placeholder="Seleccione Talla"  :options="allTallasProduccions.map(academicClassTalla => ({label: academicClassTalla.num_talla+\' / \'+academicClassTalla.nom_talla, value: academicClassTalla.talla}))"></v-select>' +

        '</div>' +

        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_prod" name="cant_produccion-' + row.id +
        '"  type="number" v-model="cant_prod" required/> </div>' +
        '</div>' +

        '<div class="col-sm-6 mb-3 offset-6">' +
        '<div class="form-group  "><input class="form-control btn btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +

        '</div>' +
        '</div>' +
        '</template>';
}

function DetailFormatterButAccionProduccion(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +

        '<div style="overflow-x:auto;" class="col-md-12">' +
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

function deleteProduccionUnico(id_produccion) {

    axios.delete('eliminar_produccion/' + id_produccion + '/')
        .then(res => {
            console.log(res);
        }).catch(error => console.log(error));

}

function formProduccionOP(idOperacion, idUsuario) {
    Vue.component('v-select', VueSelect.VueSelect, {
        extends: VueSelect,

    });
    new Vue({
        el: '#FormuProduccionOP-' + idOperacion,
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




            getProduccionData: function() {
                ProduccionOP(idOperacion);
            },
            submitFormProduccion: function() {
                var OccionId_integrante_prod = this.selectIdIntegranteProduccion.value;
                var OccionId_pantinador_prod = this.selectIDPatinadorProduccion.value;
                var OccionId_tarea = this.selectIdTareaProduccion.value;
                var OccionId_talla = this.selectIdTallaProduccion.value;
                var cantidad = $('input[name="cant_produccion-' + this.idOperacion + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if
                if (cantidad && OccionId_integrante_prod && OccionId_tarea && OccionId_talla) {
                    axios.post('/produccion/create/', {
                        idOperacion: idOperacion,
                        usuario: idUsuario,
                        OccionId_integrante_prod: OccionId_integrante_prod,
                        OccionId_pantinador_prod: OccionId_pantinador_prod, //l
                        OccionId_tarea: OccionId_tarea,
                        OccionId_talla: OccionId_talla,
                        cantidadProd: cantidad,
                    }).then(response => {
                        //console.log("produccion creada");
                        //console.log(this.$varGlobalSelectIntegrProd);
                        axios.get('dataProduccionInte-list/', {
                            params: {
                                idIntegranteSelect: this.selectIdIntegranteProduccion.value,
                                idOp: idOperacion,
                            }
                        }).then((resp) => {
                            this.allTareaProduccions = resp.data;
                        }).catch(error => console.log(error));
                    })
                }
            }
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

            this.getProduccionData();
        }
    })
}

function ProduccionOP(idOperacion, idUsuario) {
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
                { data: "delProduccion" },
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