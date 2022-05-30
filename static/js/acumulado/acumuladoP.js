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
        '<div class="col-md-6 " style="position:absolute; left:0; margin: 10px 0 0 10px">' +


        '<div id="sectIntegreOC-' + row.id + '" class="table thead-dark  animated fadeIn resutatatIntegranteAcuPatinador-' + row.id +
        '">' +
        '<table class="thead-dark animated fadeIn">' +
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

        '<div class="col-sm-6   offset-6" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>
        '<select  id="OccionId_integrante_AcuPatinador-' + row.id +
        '" class="sectIntegrenteOnChanAcuPatinador-' + row.id + ' form-select form-select-sm form-control" v-model="selectIdIntegranteAcumulado"><option value="" disabled>Selecciones Integrante</option>' +
        '<option id="id_integranteP"  v-for="(optionIntegranteACU) in allIntegrantesAcumuladosPatinador" v-bind:value="optionIntegranteACU.id">[[optionIntegranteACU.nombres]]  [[optionIntegranteACU.apellidos]]</option></select></div>' +
        '</div>' +


        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<select  id="OccionId_tarea_Acu-' + row.id +
        '" class="form-select form-select-sm form-control " v-model="selectIdTareaAcumulado"><option value="" disable>Selecciones Tarea</option>' +
        '<option id="id_tarea"  v-for="(optionTareaAcu) in allTareasAcumuladosPatinador" v-bind:value="optionTareaAcu.id">[[optionTareaAcu.nom_tarea]] / [[optionTareaAcu.detalle]]</option></select></div>' +
        '</div>' +


        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<select  id="OccionId_talla_AcuPatinador-' + row.id +
        '" class="form-select form-control form-select-sm" v-model="selectIdTallaAcumulado"><option value="" disabled>Selecciones Talla</option>' +
        '<option id="id_talla"  v-for="(opcTareaAcu) in allTallasAcumulados"  v-bind:value="opcTareaAcu.id">[[opcTareaAcu.num_talla]] / [[opcTareaAcu.nom_talla]]</option></select></div>' +
        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_prod_AcumPatinador" name="cant_prod_AcumPatinador-' + row.id +
        '" type="number" v-model="cant_prod_AcumPatinador" required/> </div>' +
        '</div>' +



        '<div class="col-sm-6 mb-3 offset-6">' +
        '<div class="form-group  "><input class="form-control btn btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +
        '</div>' +
        '</div>' +
        '</template>';
}

function formAcumuladoPatinador(idAcumuladoPatinador, idUsuario) {

    new Vue({
        el: '#FormuAcumuladoPatinador-' + idAcumuladoPatinador,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allTareaAcumuladosPatinador: [],
                allTareasAcumuladosPatinador: [],
                allTallasAcumulados: [],

                allIntegrantesAcumuladosPatinador: [],
                selectIdIntegranteAcumulado: '',
                selectIDPatinadorAcumulado: '',
                selectIdTareaAcumulado: '',
                selectIdTallaAcumulado: '',
                cant_prod_AcumPatinador: '',
                usuario: idUsuario,
                idAcumuladoPatinador: idAcumuladoPatinador,

            }
        },
        methods: {

            getAcumuladoDataPatinadorIntegrantePatinador: function() {

                //evento de escucha de integrante
                const selectElement = document.querySelector(".sectIntegrenteOnChanAcuPatinador-" + idAcumuladoPatinador);
                selectElement.addEventListener("change", (event) => {
                    const resutatatIntegranteAcuPatinador = document.
                    querySelector(".resutatatIntegranteAcuPatinador-" + idAcumuladoPatinador);
                    const idIntegranteSelect = event.target.value;
                    //variable global prototype idIntegranteSelect
                    Vue.prototype.$varGlobalSelectIntegrAcu = idIntegranteSelect;
                    axios.get('/blackbox/dataAcumuladoInte-listPatinador/', {
                        params: {
                            idIntegranteSelectPatinador: this.$varGlobalSelectIntegrAcu,
                            idAcumuladoPatinador: idAcumuladoPatinador,
                        }
                    }).then((resp) => {
                        this.allTareaAcumuladosPatinador = resp.data;
                    }).catch(error => console.log(error));







                });
            },


            getAcumuladoDataPatinador: function() {
                AcumuladoProdPatinador(idAcumuladoPatinador);


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




            submitFormAcumuladoPatinador: function() {
                var OccionId_integrante_AcuPatinador = $('select[id="OccionId_integrante_AcuPatinador-' + this.idAcumuladoPatinador + '"]').val().trim();
                var OccionId_pantinador_Acu = $('select[id="OccionId_pantinador_Acu-' + this.idAcumuladoPatinador + '"]').val().trim();
                var OccionId_tarea_Acu = $('select[id="OccionId_tarea_Acu-' + this.idAcumuladoPatinador + '"]').val().trim();
                var OccionId_talla_AcuPatinador = $('select[id="OccionId_talla_AcuPatinador-' + this.idAcumuladoPatinador + '"]').val().trim();
                var Cantidad_Acu = $('input[name="cant_prod_AcumPatinador-' + this.idAcumuladoPatinador + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if

                if (Cantidad_Acu && OccionId_integrante_AcuPatinador && OccionId_pantinador_Acu &&
                    OccionId_tarea_Acu && OccionId_talla_AcuPatinador) {
                    axios.post('/acumulado/cproAcumulado/', {
                        idAcumuladoPatinador: idAcumuladoPatinador,
                        usuario: idUsuario,
                        acumulado_id: idAcumuladoPatinador,
                        OccionId_integrante_AcuPatinador: OccionId_integrante_AcuPatinador,
                        OccionId_pantinador_Acu: OccionId_pantinador_Acu, //l
                        OccionId_tarea_Acu: OccionId_tarea_Acu,
                        OccionId_talla_AcuPatinador: OccionId_talla_AcuPatinador,
                        Cantidad_Acu: Cantidad_Acu,
                    }).then(response => {


                        axios.get('dataAcumuladoInte-list/', {
                            params: {
                                idIntegranteSelect: this.$varGlobalSelectIntegrAcu,
                                idAcumuladoPatinador: idAcumuladoPatinador,
                            }
                        }).then((resp) => {
                            this.allTareaAcumuladosPatinador = resp.data;
                        }).catch(error => console.log(error));
                    })

                }

            }
        },
        mounted: function() {
            this.getAcumuladoDataPatinadorIntegrantePatinador();
            this.getAcumuladoDataPatinador();
        }
    })





}



function DetailFormatterButAccionAcumuladoPatinador(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +

        '<div class="col-md-12">' +
        '<table  class="table animated fadeIn "  id="items-table-AcumuladoPatinador-' + row.id +
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

function AcumuladoProdPatinador(idAcumuladoPatinador, idUsuario) {
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


function deleteAcumuladoUnico(id_acumulado) {

    axios.delete('eliminar_acumulado/' + id_acumulado + '/')
        .then(res => {
            console.log(res);
        }).catch(error => console.log(error));

}









function carrarAcumulado(id_acumulado) {

    axios.get('/acumulado/cerrarAcumulado/', {
            params: {
                idAcumuladoPatinador: id_acumulado,
            }
        })
        .then((resp) => {

            window.location.reload();
        })
        .catch(error => console.log(error));


}