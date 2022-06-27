axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoAcumuladoPatinador(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formAcumuladoPatinador(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +


        '<div id="FormuAcumuladoPatinador-' + row.id + '">' +
        '<template>' +
        '<form @submit.prevent="submitFormAcumuladoPatinador" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +

        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +

        '<div class="row">' +

        '<div class="col-sm-3 offset-" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>

        '<v-select ' +
        'v-model="OccionId_integrante_AcuPatinador" placeholder="Seleccione Integrante" :options="allIntegrantesAcumuladosPatinador.map(academicClass => ({label: academicClass.nombres, value: academicClass.id}))"></v-select>' +

        '</div>' +
        '</div>' +


        '<div class="col-sm-3 offset-">' +
        '<div class="form-group">' +
        '<v-select ' +
        'v-model="selectIdTareaAcumulado"  placeholder="Seleccione Tarea"  :options="allTareasAcumuladosPatinador.map(academicClassTarea => ({label: academicClassTarea.nom_tarea+\' \'+academicClassTarea.detalle, value: academicClassTarea.id}))"></v-select>' +


        '</div>' +

        '</div>' +


        '<div class="col-sm-3 offset-">' +
        '<div class="form-group">' +
        '<v-select ' +
        'v-model="selectIdTallaAcumulado"  placeholder="Seleccione Talla"  :options="allTallasAcumulados.map(academicClassTalla => ({label: academicClassTalla.num_talla+\' / \'+academicClassTalla.nom_talla, value: academicClassTalla.id}))"></v-select>' +
        '</div>' +

        '</div>' +

        '<div class="col-sm-3 offset-">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_prod_AcumPatinador" name="cant_prod_AcumPatinador-' + row.id +
        '" type="number" v-model="cant_prod_AcumPatinador" required/> </div>' +
        '</div>' +



        '<div class="col-sm-12 offset-">' +
        '<div class="form-group  "><input class="form-control btn-success btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +


        '</div>' +
        '<div class="col-sm-12">' +
        '<div  style="overflow-x:auto;">' +
        '<div id="sectIntegreOC-' + row.id + '" class="resutatatIntegranteAcuPatinador-' + row.id +
        '">' +
        '</div>' +
        '</div>' +
        '</div>' +

        '<div class="col-sm-12 offset-">' +
        '<div style="overflow-x:auto;">' +
        '<table class="thead-dark table-fill animated fadeIn">' +
        '<thead class="">' +
        '<tr><th scope="col" class="text-center">Tareas</th>' +
        '<th scope="col" class="text-center">Cantidad</th></tr>' + '</thead>' +
        '<tbody>' +
        '<tr v-for="i in allTareaAcumuladosPatinador">' +
        '<td class="text-center">[[i.tarea]]</td>' +
        '<td class="text-center">[[i.cat_total_tarea]]</td>' +
        '</tr>' +
        '</tbody>' +
        '</table>' +
        '</div>' +
        '</div>' +


        '</div>' +
        '</div>' +
        '</template>';
}

function formAcumuladoPatinador(idAcumuladoPatinador, idUsuarioPatinador) {
    Vue.component('v-select', VueSelect.VueSelect, {
        extends: VueSelect,

    });
    new Vue({

        el: '#FormuAcumuladoPatinador-' + idAcumuladoPatinador,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allTareaAcumuladosPatinador: [],
                allTareasAcumuladosPatinador: [],
                allTallasAcumulados: [],

                allIntegrantesAcumuladosPatinador: [],
                OccionId_integrante_AcuPatinador: '',
                selectIdTareaAcumulado: '',
                selectIdTallaAcumulado: '',
                cant_prod_AcumPatinador: '',
                usuario: idUsuarioPatinador,
                idAcumuladoPatinador: idAcumuladoPatinador,

            }
        },
        methods: {
            getAcumuladoDataPatinador: function() {
                AcumuladoProdPatinador(idAcumuladoPatinador);
            },

            submitFormAcumuladoPatinador: function() {
                var OccionId_integrante_AcuPatinador = this.OccionId_integrante_AcuPatinador.value;
                var OccionId_tarea_AcuPatinador = this.selectIdTareaAcumulado.value;
                var OccionId_talla_AcuPatinador = this.selectIdTallaAcumulado.value;
                var Cantidad_AcuPatinador = $('input[name="cant_prod_AcumPatinador-' + this.idAcumuladoPatinador + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if

                if (Cantidad_AcuPatinador && OccionId_integrante_AcuPatinador &&
                    OccionId_tarea_AcuPatinador && OccionId_talla_AcuPatinador) {
                    axios.post('/blackbox/cproAcumuladoPatinador/', {
                        idAcumuladoPatinador: idAcumuladoPatinador,
                        usuarioPatinador: idUsuarioPatinador,
                        acumulado_idPatinador: idAcumuladoPatinador,
                        OccionId_integrante_AcuPatinador: OccionId_integrante_AcuPatinador,
                        OccionId_tarea_AcuPatinador: OccionId_tarea_AcuPatinador,
                        OccionId_talla_AcuPatinador: OccionId_talla_AcuPatinador,
                        Cantidad_AcuPatinador: Cantidad_AcuPatinador,
                    }).then(response => {


                        axios.get('/blackbox/dataAcumuladoInte-listPatinador/', {
                            params: {
                                idIntegranteSelectPatinador: OccionId_integrante_AcuPatinador,
                                idAcumuladoPatinador: idAcumuladoPatinador,
                            }
                        }).then((resp) => {
                            this.allTareaAcumuladosPatinador = resp.data;
                        }).catch(error => console.log(error));
                    })

                }

            }
        },
        created() {
            axios
                .get('/blackbox/integrante-listPatinador/')
                .then((resp) => {
                    this.allIntegrantesAcumuladosPatinador = resp.data
                }).catch(error => console.log(error));

            axios
                .get('/blackbox/tarea-listPatinador/')
                .then((resp) => {
                    this.allTareasAcumuladosPatinador = resp.data;
                })
                .catch(error => console.log(error));
            axios
                .get('/blackbox/tallaEmpresa-listPatinador/?idOp=' + idAcumuladoPatinador)
                .then((resp) => {
                    this.allTallasAcumulados = resp.data;
                    console.log(this.allTallasAcumulados);
                }).catch(error => console.log(error));
        },
        watch: {
            OccionId_integrante_AcuPatinador(val) {
                axios.get('/blackbox/dataAcumuladoInte-listPatinador/', {
                    params: {
                        idIntegranteSelectPatinador: val.value,
                        idAcumuladoPatinador: idAcumuladoPatinador,
                    }
                }).then((resp) => {
                    this.allTareaAcumuladosPatinador = resp.data;
                }).catch(error => console.log(error));

            }
        },
        mounted: function() {
            this.getAcumuladoDataPatinador();
        }
    })





}



function DetailFormatterButAccionAcumuladoPatinador(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +

        '<div style="overflow-x:auto;" class="col-md-12">' +
        '<table  class="table-fill animated fadeIn "  id="items-table-AcumuladoPatinador-' + row.id +
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

        //'</div>' +
        // '<div class="">' + '<button value="" onclick="deleteAllAcumulado(' + row.id + ')"  id="buttonEliminarAllacumulado" class="btn btn-outline-danger icofont-ui-remov ">Eliminar</button>' +
        // '</div>' +
        '<script type="application/javascript">' + 'AcumuladoProdPatinador(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '</div>';
    //'<div class="">' +

    //'<button class="btn btn-outline-success " type="submit" onclick="carrarAcumulado(' + row.id + ')">Cerrar Acu</button>' +

    //'</div>';
}

function AcumuladoProdPatinador(idAcumuladoPatinador, idUsuarioPatinador) {
    $(document).ready(function() {
        let table = $("#items-table-AcumuladoPatinador-" + idAcumuladoPatinador).removeAttr("width").dataTable({
            ajax: {
                url: '/blackbox/AcumuladoProc-listPatinador/?idAcumuladoPatinador=' + idAcumuladoPatinador,
                dataSrc: ''
            },
            language: { "sProcessing": "Procesando...", "sLengthMenu": "Mostrar _MENU_ registros", "sZeroRecords": "No se encontraron resutatatIntegrantes", "sEmptyTable": "Ningún dato disponible", "sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros", "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros", "sInfoFiltered": "(filtrado de un total de _MAX_ registros)", "sInfoPostFix": "", "sSearch": "Buscar:", "sUrl": "", "sInfoThousands": ",", "sLoadingRecords": "Cargando...", "oPaginate": { "sFirst": "Primero", "sLast": "Último", "sNext": "Siguiente", "sPrevious": "Anterior" }, "oAria": { "sSortAscending": ": Activar para ordenar la columna de manera ascendente", "sSortDescending": ": Activar para ordenar la columna de manera descendente" } },
            // scrollY: '500px',
            scrollCollapse: true,
            scrollY: "250px",
            order: [
                [5, "dsc"]
            ],
            "columnDefs": [
                { "className": "dt-center", "targets": "_all" }
            ],
            columns: [
                { data: "nomIntegrante" },
                { data: "apeIntegrante" },
                { data: "nomTarea" },
                { data: "nom_talla" },
                { data: "can_prod_acum" },
                { data: "created_at" },
                { data: "delAcumulProc", visible: false },
            ]

        });
        $("#items-table-AcumuladoPatinador-" + idAcumuladoPatinador).on("click", "button", function() {
            $("#items-table-AcumuladoPatinador-" + idAcumuladoPatinador).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-AcumuladoPatinador-" + idAcumuladoPatinador).DataTable().ajax.reload();
        }
    })
}