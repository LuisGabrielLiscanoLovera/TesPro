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
        '<div class="col-md-6 " style="position:absolute; left:0; margin: 10px 0 0 10px">' +


        '<div id="sectIntegreOCasino-' + row.id + '" class="resutatatIntegranteAcu-' + row.id +
        '">' +


        '</div>' +
        '</div>' +

        '<div class="col-sm-6   offset-6" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>
        '<select  id="OccionId_integrante_Acu-' + row.id +
        '" class="sectIntegrenteOnChanAcu-' + row.id + ' form-select form-select-sm form-control" v-model="selectIdIntegranteAcumulado"><option value="">Selecciones Integrante</option>' +
        '<option id="id_integrante"  v-for="(optionIntegranteACU) in allIntegrantesAcumuladoss" v-bind:value="optionIntegranteACU.id">[[optionIntegranteACU.nombres]]  [[optionIntegranteACU.apellidos]]</option></select></div>' +
        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6  ">' +
        '<div class="form-group">' +
        '<select  class="form-select form-select-sm form-control" v-model="selectIDPatinadorAcumulado" id="OccionId_pantinador_Acu-' + row.id +
        '"><option  value="">Selecciones Patinador</option>' +
        '<option  v-for="option in allPatinadoresAcumulados" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select></div>' +
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

function DetailFormatterButAccionCasino(index, row) { return 'XD DetailFormatterButAccionCasino'; }







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
                cant_prod_Acum: '',
                usuario: idUsuario,
                idCasino: idCasino,

            }
        },
        methods: {
            getAcumuladoDataIntegrante: function() {
                const selectElement = document.querySelector(".sectIntegrenteOnChanAcu-" + idCasino);
                selectElement.addEventListener("change", (event) => {
                    const resutatatIntegranteAcu = document.
                    querySelector(".resutatatIntegranteAcu-" + idCasino);
                    const idIntegranteSelect = event.target.value;
                    Vue.prototype.$varGlobalSelectIntegrAcu = idIntegranteSelect;
                    //  axios.get('casino/dataCasinoInte-list/', {
                    // params: {
                    //     idIntegranteSelect: this.$varGlobalSelectIntegrAcu,
                    //idCasino: idCasino,
                    //   }
                    // }).then((resp) => {

                    document.getElementById('sectIntegreOCasino-' + idCasino).innerHTML =
                        '<div class="">' +

                        '<table  class="table animated fadeIn "  id="items-table-Casino-' + idCasino +
                        '">' +
                        '<thead class="thead-dark">' +
                        '<tr>' +
                        /*  '<th class="text-center">Nombre</th>' +
                         '<th class="text-center">Apellido</th>' + */
                        '<th class="text-center">Fecha</th>' +
                        '<th class="text-center">Cantidad</th>' +

                        '</tr>' +
                        '</thead>' +
                        '<tbody calss="" id="casinoKill-' + idCasino + '">' +
                        /*  '<tr><td class="text-center">Nombre</td>' +
                         '<td class="text-center">Apellido</td>' + */
                        '<td class="text-center">Cantidad</td>' +
                        '<td class="text-center">Fecha</td></tr>' +
                        '</tbody>' +
                        '</table>' +
                        '</div>';
                    CasinoImporte(idCasino, idIntegranteSelect);








                    console.log("passs");








                    // }).catch(error => console.log(error));
                });
            },
            getAcumuladoData: function() {
                AcumuladoProd(idCasino);
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
            },
            submitFormAcumulado: function() {
                var OccionId_integrante_Acu = $('select[id="OccionId_integrante_Acu-' + this.idCasino + '"]').val().trim();
                var OccionId_pantinador_Acu = $('select[id="OccionId_pantinador_Acu-' + this.idCasino + '"]').val().trim();
                var Cantidad_Acu = $('input[name="cant_prod_Acum-' + this.idCasino + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if
                axios.post('/acumulado/cproAcumulado/', {
                    idCasino: idCasino,
                    usuario: idUsuario,
                    acumulado_id: idCasino,
                    OccionId_integrante_Acu: OccionId_integrante_Acu,
                    OccionId_pantinador_Acu: OccionId_pantinador_Acu, //l
                    Cantidad_Acu: Cantidad_Acu,
                }).then(response => {

                    axios.get('dataAcumuladoInte-list/', {
                        params: {
                            idIntegranteSelect: this.$varGlobalSelectIntegrAcu,
                            idCasino: idCasino,
                        }
                    }).then((resp) => {
                        this.allTareaAcumulados = resp.data;
                    }).catch(error => console.log(error));
                })
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
                //url: 'casino/dataCasinoInte-list/',?idCasino=' + idCasino + '/?idIntegranteSelect=' + idIntegranteSelect,

                url: 'casino/dataCasinoInte-list/',
                data: { idCasino: idCasino, idIntegranteSelect: idIntegranteSelect },
                dataSrc: ''
            },
            language: { "sProcessing": "Procesando...", "sLengthMenu": "Mostrar _MENU_ registros", "sZeroRecords": "No se encontraron resutatatIntegrantes", "sEmptyTable": "Ningún dato disponible en esta tabla", "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros", "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros", "sInfoFiltered": "(filtrado de un total de _MAX_ registros)", "sInfoPostFix": "", "sSearch": "Buscar:", "sUrl": "", "sInfoThousands": ",", "sLoadingRecords": "Cargando...", "oPaginate": { "sFirst": "Primero", "sLast": "Último", "sNext": "Siguiente", "sPrevious": "Anterior" }, "oAria": { "sSortAscending": ": Activar para ordenar la columna de manera ascendente", "sSortDescending": ": Activar para ordenar la columna de manera descendente" } },
            scrollY: '150px',
            scrollCollapse: true,
            "searching": false,

            scrollY: "250px",
            order: [
                [1, "dsc"]
            ],
            columns: [

                { data: "created_at" },
                { data: "cantidad" }


            ]

        });
        $("#items-table-Casino-" + idCasino).on("click", "button", function() {
            $("#items-table-Casino-" + idCasino).DataTable().ajax.reload();
            sleepThenAct();
        })

        function sleepThenAct() {
            $("#items-table-Casino-" + idCasino).DataTable().ajax.reload();
        }
    })
}