axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

function DetailFormatterButInfoCasinoPatinador(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formCasinoPatinador(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="FormuCasinoPatinador-' + row.id + '">' +
        '<template>' +
        '<form @submit.prevent="submitFormCasinoPatinador" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +
        '<div class="row">' +
        '<div class="col-md-6 " style="position:absolute; left:1;top:1   ">' +
        '<div id="sectIntegreOCasinoPatinador-' + row.id + '" class="dataTable_width_auto resutatatIntegranteCasino-' + row.id +
        '">' +
        '</div>' +
        '</div>' +

        '<div class="col-sm-6   offset-6" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>
        '<select  id="OccionId_integrante_CasinoPatinador-' + row.id +
        '" class="sectIntegrenteOnChanAcuPatinador-' + row.id + ' form-select form-select-sm form-control" v-model="selectIdIntegranteAcumuladoPatinador"><option value="" disabled>Selecciones Integrante</option>' +
        '<option id="id_integrante"  v-for="(optionIntegranteACU) in allIntegrantesAcumuladosPatinador" v-bind:value="optionIntegranteACU.id">[[optionIntegranteACU.nombres]]  [[optionIntegranteACU.apellidos]]</option></select></div>' +
        '</div>' +


        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_casinoPatinador" name="cant_casinoPatinador-' + row.id +
        '" type="number" v-model="cant_casinoPatinador" required/> </div>' +
        '</div>' +

        '<div class="col-sm-6 mb-3 offset-6">' +
        '<div class="form-group  "><input class="form-control btn btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +
        '</div>' +
        '</div>' +
        '<h5 id="TotalImportePatinador-' + row.id + '" style="position:;right:5;top:1"></h3>' +
        '<br><br><br>' +
        '</template>';
}

function DetailFormatterButAccionCasinoPatinador(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +
        '<div style="overflow-x:auto;" class="col-md-12">' +
        '<table  class="table animated fadeIn "  id="items-table-CasinoGenePatinador-' + row.id +
        '">' +
        '<thead class="thead-dark">' +
        '<tr>' +
        '<th class="text-center">id</th>' +
        '<th class="text-center">Cedula</th>' +
        '<th class="text-center">Nombre</th>' +
        '<th class="text-center">Apellido</th>' +
        '<th class="text-center">Cantidad</th>' +
        '<th class="text-center">Fecha</th>' +
        '<th class="text-center">Eliminar</th>' +
        '</tr>' +
        '</thead>' +
        '<tbody calss="table-striped table  table-sm  table-bordered table-hover" id="casinoKillPatinador-' + row.id + '">' +

        '</tbody>' +
        '</table>' +
        '<script type="application/javascript">' + 'CasinoProdPatinador(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +




        '</div>' +

        '</div>';
}


function formCasinoPatinador(idCasino, idUsuario) {


    new Vue({
        el: '#FormuCasinoPatinador-' + idCasino,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allPatinadoresAcumuladosPatinador: [],
                allIntegrantesAcumuladosPatinador: [],
                selectIdIntegranteAcumuladoPatinador: '',

                cant_casinoPatinador: '',
                usuario: idUsuario,
                idCasino: idCasino,
                total: '',

            }
        },
        methods: {
            getAcumuladoDataIntegrantePatinador: function() {

                const selectElement = document.querySelector(".sectIntegrenteOnChanAcuPatinador-" + idCasino);
                if (selectElement) {
                    selectElement.addEventListener("change", (event) => {
                        const resutatatIntegranteCasino = document.querySelector(".resutatatIntegranteCasino-" + idCasino);
                        const idIntegranteSelectPatinador = event.target.value;

                        if (idIntegranteSelectPatinador != '') {
                            Vue.prototype.$varGlobalSelectIntegrAcu = idIntegranteSelectPatinador;
                            axios
                                .get('/blackbox/dataCasino-listPatinador/', {
                                    params: {
                                        idCasinoPatinador: idCasino,
                                        idIntegranteSelectPatinador: idIntegranteSelectPatinador
                                    }
                                })
                                .then((resp) => { this.total = resp.data.TotalCasinoImporte; })
                                .catch(error => console.log(error));

                            document.getElementById('sectIntegreOCasinoPatinador-' + idCasino).innerHTML =
                                '<div style="overflow-x:auto;" class="text-center"">' +
                                '<table  class="table text-center animated fadeIn"  id="items-table-Casino-' + idCasino +
                                '">' +
                                '<thead class="thead-dark">' +
                                '<tr>' +
                                '<th>id</th>' +

                                '<th class="text-center">Fecha</th>' +
                                '<th class="text-center">Cantidad</th>' +
                                '</tr>' +
                                '</thead>' +
                                '<tbody calss="" id="casinoKillPatinador-' + idCasino + '">' +
                                '<td class="text-center">ID</td>' +

                                '<td class="text-center">Cantidad</td>' +
                                '<td class="text-center">Fecha</td></tr>' +
                                '</tbody>' +
                                '</table>' +
                                '</div>';
                            CasinoImportePatinador(idCasino, idIntegranteSelectPatinador);


                        } else {
                            document.getElementById('sectIntegreOCasinoPatinador-' + idCasino).innerHTML = '';
                            document.getElementById('TotalImportePatinador-' + idCasino).innerHTML = '';
                        }
                    });

                }

            },
            getAcumuladoDataPatinador: function() {
                axios
                    .get('/blackbox/integrante-listPatinador/')
                    .then((resp) => {
                        this.allIntegrantesAcumuladosPatinador = resp.data
                    }).catch(error => console.log(error));


            },
            submitFormCasinoPatinador: function() {
                var OccionId_integrante_CasinoPatinador = $('select[id="OccionId_integrante_CasinoPatinador-' + this.idCasino + '"]').val().trim();
                var Cantidad_CasinoPatinador = $('input[name="cant_casinoPatinador-' + this.idCasino + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if
                console.log("id casino =", idCasino, 'Cantidad_CasinoPatinador=', Cantidad_CasinoPatinador, 'OccionId_integrante_CasinoPatinador=', OccionId_integrante_CasinoPatinador);

                if (OccionId_integrante_CasinoPatinador) {
                    axios.post('/blackbox/cproCasinoPatinador/', {
                        idccp: idCasino,
                        usuario: idUsuario,
                        OccionId_integrante_CasinoPatinador: OccionId_integrante_CasinoPatinador,
                        Cantidad_CasinoPatinador: Cantidad_CasinoPatinador,
                    }).then(response => {

                        document.getElementById('sectIntegreOCasinoPatinador-' + idCasino).innerHTML =
                            '<div style="overflow-x:auto;" class="text-center"">' +
                            '<table  class="table text-center animated fadeIn"  id="items-table-Casino-' + idCasino +
                            '">' +
                            '<thead class="thead-dark">' +
                            '<tr>' +
                            '<th class="" >ID</th>' +
                            '<th class="text-center">Fecha</th>' +
                            '<th class="text-center">Cantidad</th>' +
                            '</tr>' +
                            '</thead>' +
                            '<tbody calss="" id="casinoKillPatinador-' + idCasino + '">' +
                            '<td class="text-center">ID</td>' +
                            '<td class="text-center">Cantidad</td>' +
                            '<td class="text-center">Fecha</td></tr>' +
                            '</tbody>' +
                            '</table>' +
                            '</div>';
                        CasinoImportePatinador(idCasino, OccionId_integrante_CasinoPatinador);


                    })
                }
            }
        },
        mounted: function() {
            this.getAcumuladoDataIntegrantePatinador();
            this.getAcumuladoDataPatinador();
        }
    })





}

function CasinoImportePatinador(idCasino, idIntegranteSelectPatinador) {
    $(document).ready(function() {
        let table = $("#items-table-Casino-" + idCasino).removeAttr("width").dataTable({
            ajax: {
                url: '/blackbox/dataCasinoInte-listPatinador/',
                data: { idCasinoPatinador: idCasino, idIntegranteSelectPatinador: idIntegranteSelectPatinador },
                dataSrc: ''
            },
            language: { "sProcessing": "Procesando...", "sLengthMenu": "Mostrar _MENU_ registros", "sZeroRecords": "No se encontraron resutatatIntegrantes", "sEmptyTable": "Ningún dato disponible ", "sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros", "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros", "sInfoFiltered": "(filtrado de un total de _MAX_ registros)", "sInfoPostFix": "", "sSearch": "Buscar:", "sUrl": "", "sInfoThousands": ",", "sLoadingRecords": "Cargando...", "oPaginate": { "sFirst": "Primero", "sLast": "Último", "sNext": "Siguiente", "sPrevious": "Anterior" }, "oAria": { "sSortAscending": ": Activar para ordenar la columna de manera ascendente", "sSortDescending": ": Activar para ordenar la columna de manera descendente" } },

            scrollCollapse: true,
            "searching": false,

            scrollY: "250px",
            order: [
                [1, 'desc']
            ],
            columns: [
                { data: "id", "visible": false },
                { data: "created_at" },
                { data: "cantidad", render: $.fn.dataTable.render.number(',', '.', 2, ' ') },
            ],
            "columnDefs": [
                { "className": "dt-center", "targets": "_all" }
            ],

        });
        $("#items-table-Casino-" + idCasino).on("click", "button", function() {
            $("#items-table-Casino-" + idCasino).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-Casino-" + idCasino).DataTable().ajax.reload();
        }
    });
    axios
        .get('/blackbox/totalImporteIntePatinador/', {
            params: {
                idCasinoPatinador: idCasino,
                idIntegranteSelectPatinador: idIntegranteSelectPatinador
            }
        })
        .then((resp) => {

            this.total = resp.data.TotalCasinoImporte;

            this.cedulaIntegrante = resp.data.cedulaIntegrante;
            if (this.total == null) { this.total = 0 }

            var T = (this.total).toLocaleString('en-US', {
                style: 'currency',
                currency: 'USD',
            });

            document.getElementById('TotalImportePatinador-' + idCasino).innerHTML =
                '<div class="col-md-5 offset-7 alert border btn-cyan bt ">Importe total  : <b>' + T + '</b><br class="mb-3" >Cedula: ' + cedulaIntegrante + '</div>';

        })
        .catch(error => {
            document.getElementById('TotalImportePatinador-' + idCasino).innerHTML = '',
                console.log(error)
        });
}

function CasinoProdPatinador(idCasino, idUsuario) {
    $(document).ready(function() {
        let table = $("#items-table-CasinoGenePatinador-" + idCasino).removeAttr("width").dataTable({
            ajax: {
                url: '/blackbox/dataCasino-listPatinador/',
                data: { idCasinoPatinador: idCasino, idUsuario: idUsuario },
                dataSrc: ''
            },
            language: { "sProcessing": "Procesando...", "sLengthMenu": "Mostrar _MENU_ registros", "sZeroRecords": "No se encontraron resutatatIntegrantes", "sEmptyTable": "Ningún dato disponible", "sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros", "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros", "sInfoFiltered": "(filtrado de un total de _MAX_ registros)", "sInfoPostFix": "", "sSearch": "Buscar:", "sUrl": "", "sInfoThousands": ",", "sLoadingRecords": "Cargando...", "oPaginate": { "sFirst": "Primero", "sLast": "Último", "sNext": "Siguiente", "sPrevious": "Anterior" }, "oAria": { "sSortAscending": ": Activar para ordenar la columna de manera ascendente", "sSortDescending": ": Activar para ordenar la columna de manera descendente" } },
            // scrollY: '500px',
            scrollCollapse: true,
            scrollY: "250px",
            order: [
                [5, 'dsc']
            ],
            "columnDefs": [
                { "className": "dt-center", "targets": "_all" }

            ],
            columns: [
                { data: "id", "visible": false },
                { data: "cedulaIntegrante" },
                { data: "nomIntegrante" },
                { data: "apelIntegrante" },
                { data: "cantidad", render: $.fn.dataTable.render.number(',', '.', 2, ' ') },
                { data: "created_at" },
                { data: "delCasinoImport", visible: false },


            ]

        });
        $("#items-table-CasinoGenePatinador-" + idCasino).on("click", "button", function() {
            $("#items-table-CasinoGenePatinador-" + idCasino).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-CasinoGenePatinador-" + idCasino).DataTable().ajax.reload();
        }
    })
}