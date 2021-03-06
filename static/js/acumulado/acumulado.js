axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoAcumulado(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formAcumulado(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +


        '<div id="FormuAcumulado-' + row.id + '">' +
        '<template>' +
        '<form @submit.prevent="submitFormAcumulado" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +

        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +
        '<div class="row">' +
        '<div class="col-md-6 " style="position:absolute; left:0; margin: 10px 0 0 10px">' +


        '<div id="sectIntegreOC-' + row.id + '" class="table thead-dark  animated fadeIn resutatatIntegranteAcu-' + row.id +
        '">' +
        '<table class="thead-dark animated fadeIn">' +
        '<thead class="">' +
        '<tr><th scope="col" class="text-center">Tareas</th>' +
        '<th scope="col" class="text-center">Cantidad</th></tr>' + '</thead>' +
        '<tbody>' +
        '<tr v-for="i in allTareaAcumulados">' +
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
        'v-model="OccionId_integrante_Acu" placeholder="Seleccione Integrante" :options="allIntegrantesAcumuladoss.map(academicClass => ({label: academicClass.nombres, value: academicClass.id}))"></v-select>' +
        '</div>' +
        '</div>' +
        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +

        '<v-select ' +
        'v-model="selectID_Patinador_Acu"  placeholder="Seleccione Patinador"  :options="allPatinadoresAcumulados.map(academicClassPatinador => ({label: academicClassPatinador.nomPatinador+\' \'+academicClassPatinador.apellPatinador, value: academicClassPatinador.id}))"></v-select>' +
        '</div>' +
        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +

        '<v-select ' +
        'v-model="selectID_Tarea_Acu"  placeholder="Seleccione Tarea"  :options="allTareasAcumulados.map(academicClassTarea => ({label: academicClassTarea.nom_tarea+\' \'+academicClassTarea.detalle, value: academicClassTarea.id}))"></v-select>' +
        '</div>' +

        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +

        '<v-select ' +
        'v-model="selectID_Talla_Acu"  placeholder="Seleccione Talla"  :options="allTallasAcumulados.map(academicClassTalla => ({label: academicClassTalla.num_talla+\' / \'+academicClassTalla.nom_talla, value: academicClassTalla.id}))"></v-select>' +
        '</div>' +
        '</div>' +
        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_prod_Acum" name="cant_prod_Acum-' + row.id +
        '" type="number" v-model="cant_prod_Acum" required/> </div>' +
        '</div>' +

        '<div class="col-sm-6 mb-3 offset-6">' +
        '<div class="form-group  "><input class="form-control btn btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +
        '</div>' +
        '</div>' +
        '</template>';
}

function formAcumulado(idAcumulado, idUsuario) {
    Vue.component('v-select', VueSelect.VueSelect, {
        extends: VueSelect,

    });

    new Vue({
        el: '#FormuAcumulado-' + idAcumulado,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                OccionId_integrante_Acu: '',
                selectID_Patinador_Acu: '',
                selectID_Tarea_Acu: '',
                selectID_Talla_Acu: '',
                allTareaAcumulados: [],
                allTareasAcumulados: [],
                allTallasAcumulados: [],
                allPatinadoresAcumulados: [],
                allIntegrantesAcumuladoss: [],



                cant_prod_Acum: '',
                usuario: idUsuario,
                idAcumulado: idAcumulado,

            }
        },

        methods: {

            getAcumuladoData: function() {
                AcumuladoProd(idAcumulado);

            },

            submitFormAcumulado: function() {




                var OccionId_integrante_Acu = this.OccionId_integrante_Acu.value;
                var OccionId_pantinador_Acu = this.selectID_Patinador_Acu.value;
                var OccionId_tarea_Acu = this.selectID_Tarea_Acu.value;
                var OccionId_talla_Acu = this.selectID_Talla_Acu.value;
                var Cantidad_Acu = $('input[name="cant_prod_Acum-' + this.idAcumulado + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if

                if (Cantidad_Acu && OccionId_integrante_Acu && OccionId_pantinador_Acu &&
                    OccionId_tarea_Acu && OccionId_talla_Acu) {
                    axios.post('/acumulado/cproAcumulado/', {
                        idAcumulado: idAcumulado,
                        usuario: idUsuario,
                        acumulado_id: idAcumulado,
                        OccionId_integrante_Acu: OccionId_integrante_Acu,
                        OccionId_pantinador_Acu: OccionId_pantinador_Acu, //l
                        OccionId_tarea_Acu: OccionId_tarea_Acu,
                        OccionId_talla_Acu: OccionId_talla_Acu,
                        Cantidad_Acu: Cantidad_Acu,
                    }).then(response => {


                        axios.get('dataAcumuladoInte-list/', {
                            params: {
                                idIntegranteSelect: OccionId_integrante_Acu,
                                idAcumulado: idAcumulado,
                            }
                        }).then((resp) => {
                            this.allTareaAcumulados = resp.data;
                        }).catch(error => console.log(error));
                    })

                }

            }
        },

        created() {


            axios
                .get('/integrante/integrante-list/')
                .then((resp) => {
                    this.allIntegrantesAcumuladoss = resp.data
                }).catch(error => console.log(error));
            axios
                .get('/produccion/lista_patinadoresAct-prod/')
                .then((resp) => {
                    this.allPatinadoresAcumulados = resp.data
                }).catch(error => console.log(error));
            axios
                .get('/tarea/tarea-list/')
                .then((resp) => {
                    this.allTareasAcumulados = resp.data;
                })
                .catch(error => console.log(error));
            axios
                .get('/talla/tallaEmpresa-list/?idOp=' + idAcumulado)
                .then((resp) => {
                    this.allTallasAcumulados = resp.data;
                    console.log(this.allTallasAcumulados);
                }).catch(error => console.log(error));
        },
        watch: {
            OccionId_integrante_Acu(val) {

                axios.get('dataAcumuladoInte-list/', {
                    params: {
                        idIntegranteSelect: val.value,
                        idAcumulado: idAcumulado,
                    }
                }).then((resp) => {
                    this.allTareaAcumulados = resp.data;
                }).catch(error => console.log(error));

            }
        },
        mounted: function() {

            this.getAcumuladoData();
        }
    })





}



function DetailFormatterButAccionAcumulado(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +

        '<div class="col-md-10">' +
        '<table  class="table animated fadeIn "  id="items-table-Acumulado-' + row.id +
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
        '<script type="application/javascript">' + 'AcumuladoProd(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '</div>' +
        '<div class="">' +

        '<button class="btn btn-outline-success " type="submit" onclick="carrarAcumulado(' + row.id + ')">Cerrar Acumulado</button>' +

        '</div>';
}

function AcumuladoProd(idAcumulado, idUsuario) {
    $(document).ready(function() {
        let table = $("#items-table-Acumulado-" + idAcumulado).removeAttr("width").dataTable({
            ajax: {
                url: 'AcumuladoProc-list/?idAcumulado=' + idAcumulado,
                dataSrc: ''
            },
            language: { "sProcessing": "Procesando...", "sLengthMenu": "Mostrar _MENU_ registros", "sZeroRecords": "No se encontraron resutatatIntegrantes", "sEmptyTable": "Ning??n dato disponible", "sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros", "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros", "sInfoFiltered": "(filtrado de un total de _MAX_ registros)", "sInfoPostFix": "", "sSearch": "Buscar:", "sUrl": "", "sInfoThousands": ",", "sLoadingRecords": "Cargando...", "oPaginate": { "sFirst": "Primero", "sLast": "??ltimo", "sNext": "Siguiente", "sPrevious": "Anterior" }, "oAria": { "sSortAscending": ": Activar para ordenar la columna de manera ascendente", "sSortDescending": ": Activar para ordenar la columna de manera descendente" } },
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
                { data: "delAcumulProc" },
            ]

        });
        $("#items-table-Acumulado-" + idAcumulado).on("click", "button", function() {
            $("#items-table-Acumulado-" + idAcumulado).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-Acumulado-" + idAcumulado).DataTable().ajax.reload();
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
                idAcumulado: id_acumulado,
            }
        })
        .then((resp) => {

            window.location.reload();
        })
        .catch(error => console.log(error));


}