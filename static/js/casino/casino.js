axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

function DetailFormatterButInfoCasino(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formCasino(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="FormuCasino-' + row.id + '">' +
        '<template>' +
        '<form @submit.prevent="submitFormCasino" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +
        '<div class="row">' +
        '<div class="col-md-6 " style="position:absolute; left:1;top:1   ">' +
        '<div id="sectIntegreOCasino-' + row.id + '" class="dataTable_width_auto resutatatIntegranteCasino-' + row.id +
        '">' +
        '</div>' +
        '</div>' +

        '<div class="col-sm-6   offset-6" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>
        '<select  id="OccionId_integrante_Casino-' + row.id +
        '" class="sectIntegrenteOnChanAcu-' + row.id + ' form-select form-select-sm form-control" v-model="selectIdIntegranteAcumulado"><option value="">Selecciones Integrante</option>' +
        '<option id="id_integrante"  v-for="(optionIntegranteACU) in allIntegrantesAcumuladoss" v-bind:value="optionIntegranteACU.id">[[optionIntegranteACU.nombres]]  [[optionIntegranteACU.apellidos]]</option></select></div>' +
        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6  ">' +
        '<div class="form-group">' +
        '<select  class="form-select form-select-sm form-control" v-model="selectIDPatinadorAcumulado" id="OccionId_pantinador_Casino-' + row.id +
        '"><option  value="">Selecciones Patinador</option>' +
        '<option  v-for="option in allPatinadoresAcumulados" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select></div>' +
        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_casino" name="cant_casino-' + row.id +
        '" type="number" v-model="cant_casino" required/> </div>' +
        '</div>' +

        '<div class="col-sm-6 mb-3 offset-6">' +
        '<div class="form-group  "><input class="form-control btn btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +
        '</div>' +
        '</div>' +
        '<h5 id="TotalImporte-' + row.id + '" style="position:;right:5;top:1"></h3>' +
        '<br><br><br>' +
        '</template>';
}

function DetailFormatterButAccionCasino(index, row) {
    //r = parseInt("[[progressRest]]");
    return '<div class="row">' +
        '<div class="col-md-9">' +
        '<table  class="table animated fadeIn "  id="items-table-CasinoGene-' + row.id +
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
        '<tbody calss="table-striped table  table-sm  table-bordered table-hover" id="casinoKill-' + row.id + '">' +

        '</tbody>' +
        '</table>' +
        '<script type="application/javascript">' + 'CasinoProd(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '</div>';
}




function formCasino(idCasino, idUsuario) {

    new Vue({
        el: '#FormuCasino-' + idCasino,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allPatinadoresAcumulados: [],
                allIntegrantesAcumuladoss: [],
                selectIdIntegranteAcumulado: '',
                selectIDPatinadorAcumulado: '',
                selectIdTareaAcumulado: '',
                selectIdTallaAcumulado: '',
                cant_casino: '',
                usuario: idUsuario,
                idCasino: idCasino,
                total: '',

            }
        },
        methods: {
            getAcumuladoDataIntegrante: function() {
                const selectElement = document.querySelector(".sectIntegrenteOnChanAcu-" + idCasino);
                selectElement.addEventListener("change", (event) => {
                    const resutatatIntegranteCasino = document.querySelector(".resutatatIntegranteCasino-" + idCasino);
                    const idIntegranteSelect = event.target.value;
                    Vue.prototype.$varGlobalSelectIntegrAcu = idIntegranteSelect;
                    axios
                        .get('/casino/totalImporteInte/', {
                            params: {
                                idCasino: idCasino,
                                idIntegranteSelect: idIntegranteSelect
                            }
                        })
                        .then((resp) => { this.total = resp.data.TotalCasinoImporte; })
                        .catch(error => console.log(error));
                    document.getElementById('sectIntegreOCasino-' + idCasino).innerHTML =
                        '<div class="text-center"">' +
                        '<table  class="table text-center animated fadeIn"  id="items-table-Casino-' + idCasino +
                        '">' +
                        '<thead class="thead-dark">' +
                        '<tr>' +
                        '<th>id</th>' +

                        '<th class="text-center">Fecha</th>' +
                        '<th class="text-center">Cantidad</th>' +
                        '</tr>' +
                        '</thead>' +
                        '<tbody calss="" id="casinoKill-' + idCasino + '">' +
                        '<td class="text-center">ID</td>' +

                        '<td class="text-center">Cantidad</td>' +
                        '<td class="text-center">Fecha</td></tr>' +
                        '</tbody>' +
                        '</table>' +
                        '</div>';
                    CasinoImporte(idCasino, idIntegranteSelect);


                });
            },
            getAcumuladoData: function() {
                axios
                    .get('/integrante/integrante-list/')
                    .then((resp) => {
                        this.allIntegrantesAcumuladoss = resp.data
                    }).catch(error => console.log(error));

                axios
                    .get('/casino/lista_patinadoresAct-casino/')
                    .then((resp) => {
                        this.allPatinadoresAcumulados = resp.data
                    }).catch(error => console.log(error));
            },
            submitFormCasino: function() {
                var OccionId_integrante_Casino = $('select[id="OccionId_integrante_Casino-' + this.idCasino + '"]').val().trim();
                var OccionId_pantinador_Casino = $('select[id="OccionId_pantinador_Casino-' + this.idCasino + '"]').val().trim();
                var Cantidad_Casino = $('input[name="cant_casino-' + this.idCasino + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if
                console.log(OccionId_integrante_Casino);
                console.log(OccionId_pantinador_Casino);


                if (Cantidad_Casino && OccionId_integrante_Casino) {
                    axios.post('/casino/cproCasino/', {
                        idCasino: idCasino,
                        usuario: idUsuario,
                        OccionId_integrante_Casino: OccionId_integrante_Casino,
                        OccionId_pantinador_Casino: OccionId_pantinador_Casino, //l
                        Cantidad_Casino: Cantidad_Casino,
                    }).then(response => {

                        document.getElementById('sectIntegreOCasino-' + idCasino).innerHTML =
                            '<div class="text-center"">' +
                            '<table  class="table text-center animated fadeIn"  id="items-table-Casino-' + idCasino +
                            '">' +
                            '<thead class="thead-dark">' +
                            '<tr>' +
                            '<th class="" >ID</th>' +
                            '<th class="text-center">Fecha</th>' +
                            '<th class="text-center">Cantidad</th>' +
                            '</tr>' +
                            '</thead>' +
                            '<tbody calss="" id="casinoKill-' + idCasino + '">' +
                            '<td class="text-center">ID</td>' +
                            '<td class="text-center">Cantidad</td>' +
                            '<td class="text-center">Fecha</td></tr>' +
                            '</tbody>' +
                            '</table>' +
                            '</div>';
                        CasinoImporte(idCasino, OccionId_integrante_Casino);


                    })
                }
            }
        },
        mounted: function() {
            this.getAcumuladoDataIntegrante();
            this.getAcumuladoData();
        }
    })





}

function CasinoImporte(idCasino, idIntegranteSelect) {
    $(document).ready(function() {
        let table = $("#items-table-Casino-" + idCasino).removeAttr("width").dataTable({
            ajax: {
                url: '/casino/dataCasinoInte-list/',
                data: { idCasino: idCasino, idIntegranteSelect: idIntegranteSelect },
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
        .get('/casino/totalImporteInte/', {
            params: {
                idCasino: idCasino,
                idIntegranteSelect: idIntegranteSelect
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

            document.getElementById('TotalImporte-' + idCasino).innerHTML =
                '<div class="col-md-5 offset-7 alert border btn-cyan bt ">Importe total  : <b>' + T + '</b><br class="mb-3" >Cedula: ' + cedulaIntegrante + '</div>';

        })
        .catch(error => console.log(error));
}




function CasinoProd(idCasino, idUsuario) {
    $(document).ready(function() {
        let table = $("#items-table-CasinoGene-" + idCasino).removeAttr("width").dataTable({
            ajax: {
                url: '/casino/dataCasino-list/',
                data: { idCasino: idCasino, idUsuario: idUsuario },
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
                { data: "delCasinoImport" },


            ]

        });
        $("#items-table-CasinoGene-" + idCasino).on("click", "button", function() {
            $("#items-table-CasinoGene-" + idCasino).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-CasinoGene-" + idCasino).DataTable().ajax.reload();
        }
    })
}




function deleteImporteUnico(id_casino) {

    axios.delete('/casino/deleteImporteUnico/' + id_casino + '/')
        .then(res => {
            console.log(res);
        }).catch(error => console.log(error));

}