axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoProduccionPatinador(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formProduccionOPPatinador(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="FormuProduccionOPPatinador-' + row.id + '">' +
        '<template>' +
        '<form @submit.prevent="submitFormProduccionPatinador" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +
        '<div class="row">' +

        '<div class="col-md-4 " style="position:absolute; left:0; margin: 10px 0 0 10px">' +
        '<div id="sectIntegreOC-' + row.id + '" class="table animated fadeIn resutatatIntegrante-' + row.id +
        '">' +

        '<div style="overflow-x:auto;">' +

        '<table class="thead-dark animated fadeIn">' +
        '<thead class="">' +
        '<tr><th scope="col" class="text-center">Tareas</th><th scope="col" class="text-center">Cantidad</th></tr>' +
        '</thead>' +
        '<tbody>' +
        '<tr v-for="i in allTareaProduccionsPatinador">' +

        '<td class="text-center">[[i.tarea]]</td>' +
        '<td class="text-center">[[i.cat_total_tarea]]</td>' +
        '</tr>' +
        '</tbody>' +
        '</table>' +
        '</div>' +

        '</div>' +
        '</div>' +



        '<div class="col-sm-6   offset-6" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>
        '<v-select ' +
        'v-model="selectIdIntegranteProduccion" placeholder="Seleccione Integrante" :options="allIntegrantesProduccions.map(academicClass => ({label: academicClass.nombres, value: academicClass.id}))"></v-select>' +



        '</div>' +
        '</div>' +









        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<v-select ' +
        'v-model="selectIdTareaProduccionPatinador"  placeholder="Seleccione Tarea"  :options="allTareasProduccions.map(academicClassTarea => ({label: academicClassTarea.nom_tarea+\' \'+academicClassTarea.detalle, value: academicClassTarea.id}))"></v-select>' +
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
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_prod" name="cant_produccionPatinador-' + row.id +
        '"  type="number" v-model="cant_prod" required/> </div>' +
        '</div>' +

        '<div class="col-sm-6 mb-3 offset-6">' +
        '<div class="form-group  "><input class="form-control btn btn-success btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +

        '</div>' +
        '</div>' +
        '</template>';
}

function DetailFormatterButAccionProduccionPatinador(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +

        '<div style="overflow-x:auto;" class="col-md-12">' +
        '<table  class="table animated fadeIn "  id="items-table-produccionPatinador-' + row.id +
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
        '<script type="application/javascript">' + 'ProduccionOPPatinador(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '</div>';
}

/* function deleteProduccionUnico(id_produccion) {

    axios.delete('eliminar_produccion/' + id_produccion + '/')
        .then(res => {
            console.log(res);
        }).catch(error => console.log(error));

} */

function formProduccionOPPatinador(idOperacionPatinador, idUsuario) {
    Vue.component('v-select', VueSelect.VueSelect, {
        extends: VueSelect,

    });
    new Vue({
        el: '#FormuProduccionOPPatinador-' + idOperacionPatinador,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allTallasProduccions: [],
                allTareasProduccions: [],
                allIntegrantesProduccions: [],
                allTareaProduccionsPatinador: [],
                selectIdIntegranteProduccion: '',
                selectIdTareaProduccionPatinador: '',
                selectIdTallaProduccion: '',
                selectIDPatinadorProduccion: '',
                cant_prod: '',
                name: 'pass',
                usuario: idUsuario,
                idOperacionPatinador: idOperacionPatinador,

            }
        },
        methods: {
            getProduccionData: function() {
                ProduccionOPPatinador(idOperacionPatinador);


            },
            submitFormProduccionPatinador: function() {
                var OccionId_integrante_prodPatinador = this.selectIdIntegranteProduccion.value;
                var OccionId_tareaPatinador = this.selectIdTareaProduccionPatinador.value;
                var OccionId_tallaPatinador = this.selectIdTallaProduccion.value;
                var cantidad = $('input[name="cant_produccionPatinador-' + this.idOperacionPatinador + '"]').val().trim();


                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if
                if (cantidad && OccionId_integrante_prodPatinador && OccionId_tareaPatinador && OccionId_tallaPatinador) {
                    axios.post('/blackbox/createPatinadorProduccion/', {
                        idOperacionPatinador: idOperacionPatinador,
                        usuario: idUsuario,
                        OccionId_integrante_prodPatinador: OccionId_integrante_prodPatinador,

                        OccionId_tareaPatinador: OccionId_tareaPatinador,
                        OccionId_tallaPatinador: OccionId_tallaPatinador,
                        cantidadProdPatinador: cantidad,
                    }).then(response => {
                        //console.log("produccion creada");
                        //console.log(this.$varGlobalSelectIntegrProd);
                        axios.get('/blackbox/dataProduccionInte-listPatinador/', {
                            params: {
                                idIntegranteSelectPatinador: OccionId_integrante_prodPatinador,
                                idOpPatinador: idOperacionPatinador,
                            }
                        }).then((resp) => {
                            this.allTareaProduccionsPatinador = resp.data;
                        }).catch(error => console.log(error));
                    })
                }
            }
        },
        created() {
            axios
                .get('/blackbox/tarea-listPatinador/')
                .then((resp) => {
                    this.allTareasProduccions = resp.data;
                })
                .catch(error => console.log(error));
            axios
                .get('/blackbox/integrante-listPatinador/')
                .then((resp) => {
                    this.allIntegrantesProduccions = resp.data
                }).catch(error => console.log(error));

            axios
                .get('/blackbox/tallaOP-list-patinador/?idOp=' + idOperacionPatinador)
                .then((resp) => {
                    this.allTallasProduccions = resp.data;
                    console.log(this.allTallasProduccions);
                }).catch(error => console.log(error));
        },

        watch: {
            selectIdIntegranteProduccion(val) {

                axios.get('/blackbox/dataProduccionInte-listPatinador/', {
                    params: {
                        idIntegranteSelectPatinador: val.value,
                        idOpPatinador: idOperacionPatinador,
                    }
                }).then((resp) => {
                    this.allTareaProduccionsPatinador = resp.data;
                }).catch(error => console.log(error));

            }
        },



        mounted: function() {

            this.getProduccionData();
        }
    })
}

function ProduccionOPPatinador(idOperacionPatinador, idUsuario) {
    $(document).ready(function() {
        let table = $("#items-table-produccionPatinador-" + idOperacionPatinador).removeAttr("width").dataTable({
            ajax: {
                url: '/blackbox/produccionOP-listPatinador/?idOp=' + idOperacionPatinador,
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
                {
                    data: "delProduccion",
                    visible: false
                },
            ]

        });
        $("#items-table-produccionPatinador-" + idOperacionPatinador).on("click", "button", function() {
            $("#items-table-produccionPatinador-" + idOperacionPatinador).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-produccionPatinador-" + idOperacionPatinador).DataTable().ajax.reload();
        }
    })
}