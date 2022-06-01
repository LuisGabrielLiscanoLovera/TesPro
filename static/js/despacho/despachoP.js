//script vue y axios


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

//script datatable
function DetailFormatterButInfoDespachoPerfilPatinadores(index, row) {
    //r = parseInt("[[progressRest]]");

    //crea y renderiza la tabla
    return '<div class="row">' +


        '<div class="col-md-5">' +
        '<div id="FormuTallaOPPatinador-' + row.id +
        '">' +

        '<template>' +
        '<div class="border-info alert"><b><h6>Restante &nbsp;&nbsp;<b class="big-button">[[cantRestantePatinador]] <hrr></b> de [[total]]</b></h6></div>' +
        '<form @submit.prevent="submitFormDespachoPatinador" class="form dark"><div hidden=True>{% csrf_token %}</div>' +
        '<div>' +
        //'<div class="progress progress-striped"><div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="1" aria-valuemin="0" aria-valuemax="1" style="width:' +
        //'% ' +
        //'">Faltante</div></div>' +
        '<input  id="operacionPatinador-' + row.id +
        '" name="operacionPatinador-' + row.id +
        '"  type="number" hidden=True value="' + row.id +
        '"  required/>' +
        '<select  id="OccionId_tallaPatinador-' + row.id +
        '" class="form-control mb-1" v-model="selectIdTallaPatinador"><option  value="" disabled>Selecciones Talla</option>' +
        '<option id="id_talla"  v-for="(optionTalla) in allTallasOPsPatinador"  v-bind:value="optionTalla.talla"  >[[optionTalla.num_talla]] / [[optionTalla.nom_talla]]</option></select>' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant" name="cantOpDespachoPatinador-' + row.id +
        '"  type="number" v-model="cant" required/>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +
        '<br><input class="form-control form-control btn btn-success " type="submit"  value="Guardar"></form></div></div>' +
        '</template>' +
        '</div>' +


        '</div><br><br><br><br>' +


        '<div class="col-md-6">' +

        '<div id="despachoVue-' + row.id + '"><template>' +
        '<div style="overflow-x:auto;" ><table class="table-fill animated fadeIn  border-info ">' +
        '<thead class="thead-dark">' +
        '<tr>' +
        '<th class="text-center">Nombre Talla</th>' +
        '<th class="text-center">Talla Total</th>' +
        '<th class="text-center">Talla Restante</th>' +
        '</tr>' +
        '</thead><tbody id="listKill' + row.id + '">' +
        '<tr v-for="allTallaOP in allTallaOPs" :key="allTallaOP.id">' +
        '<td class="text-center">[[allTallaOP.nom_talla]]</td><td class="text-center">[[allTallaOP.can_talla]]' +
        '</td><td class=" text-center">[[allTallaOP.res_talla]]</td></tr>' +
        '</tbody></template></div></div>' +
        '</table>' + '<script type="application/javascript">' + 'formOPPatinador(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +

        '</div>' +

























        '</div>' +









        '</div>';

}

function DetailFormatterButAccionDespachoPatinador(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +



        '<div class="col-md-12">' +
        '<table class="animated fadeIn table thead-dark text-center " id="items-tablePatinador' + row.id +
        '"><thead><tr>' +


        '<th cass="text-center">Patinador</th>' +
        '<th cass="text-center">Talla</th>' +
        '<th cass="text-center">Cantidad</th>' +
        '<th cass="text-center">Fecha</th>' +
        '<th cass="text-center">Eliminar</th>' +
        '</tr></thead><tbody></tbody></table>' +

        '</div>' +



        '<center><div class="col-md-6 col-md-offset-1 align-self-center">' +
        //'<button class="btn btn-sm btn-block btn-outline-danger  icofont-ui-remove" type="submit" onclick="deleteDespacho(' + row.id + ')">' +


        '</div></center>' +
        '<script type="application/javascript">' +
        '$(document).ready(function() {' +

        'var table= $("#items-tablePatinador' + row.id +
        '").removeAttr("width").dataTable({  "searching": true' +
        ',serverSide: true, scrollY: "250px", scrollCollapse: true,' +
        'order:[[4,"desc"]],' +




        'sAjaxSource:' +
        '"/blackbox/dataPatinador/?idOpPatinador= ' + row.id + ' &usuarioPatinador=' + row.usuario + '",' +
        'columns: [' +
        ' {' +
        'name: "nomPatinadorDespacho",' +
        'data: 0' +
        '}, {' +
        'name: "nomTallaDespacho",' +
        'data: 1' +
        '}, ' +

        '{name:"can_terminada",data:2}, ' +
        '{name:"created_at",data:3},' +
        '{name:"btnDelDespacho",data:4 ,visible: false},' +


        '],' +

        '"language": {"sProcessing": "Procesando...","sLengthMenu": "Mostrar _MENU_ registros","sZeroRecords": "No se encontraron resultados","sEmptyTable": "Ningún dato disponible","sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros","sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros","sInfoFiltered": "(filtrado de un total de _MAX_ registros)","sInfoPostFix": "","sSearch": "Buscar:","sUrl": "","sInfoThousands": ",","sLoadingRecords": "Cargando...","oPaginate": {"sFirst": "Primero","sLast": "Último","sNext": "Siguiente","sPrevious": "Anterior"},"oAria": {"sSortAscending": ": Activar para ordenar la columna de manera ascendente","sSortDescending": ": Activar para ordenar la columna de manera descendente"}},' +
        '"columnDefs": [{ "className": "dt-center", "targets": "_all" }],' +

        '});' +

        //reload data table despues de eliminar


        '$("#items-tablePatinador' + row.id + '").on("click", "button", function(){ ' +
        '$("#items-tablePatinador' + row.id + '").DataTable().ajax.reload();' +
        '$("#items-tablePatinador' + row.id + '").DataTable().ajax.reload();' +

        'sleepThenAct();' +

        '});' +
        '});' +

        'function sleepThenAct() {' +
        '$("#items-tablePatinador' + row.id + '").DataTable().ajax.reload();' +
        '}' +

        '</script>' +
        '</div>';

}






function formOPPatinador(idOp, usuario) {
    new Vue({
        el: '#FormuTallaOPPatinador-' + idOp,
        delimiters: ['[[', ']]'],

        data: function() {
            return {

                allTallasOPsPatinador: [],
                id_OP: idOp,
                selectIdTallaPatinador: '',
                usuario: usuario,
                cant: '',
                cantRestantePatinador: '',

                total: '',
                fechaCierre: ''

            }

        },
        methods: {


            getDespachoDataPatinador: function() {
                tallasOPPatinador(idOp);

                axios
                    .get('/blackbox/tallaOP-list-patinador/?idOp=' + idOp)
                    .then((resp) => {
                        this.allTallasOPsPatinador = resp.data;

                    })
                    .catch(error => console.log(error));

                axios
                    .get('/blackbox/tallaOP-IncosistentePatinadores/?idOperacion=' + idOp)
                    .then((resp) => {
                        this.cantRestantePatinador = resp.data.TotalOpRestante;

                        this.total = resp.data.CanOperacion;
                        //this.progressRest = ((resp.data.TotalOpRestante * 100) / resp.data.CanTallaTotal)
                        //document.getElementById('canRestante-' + idOp).innerHTML = "Restante";

                    })
                    .catch(error => console.log(error));



            },

            submitFormDespachoPatinador() {
                var OccionId_tallaPatinador = $('select[id="OccionId_tallaPatinador-' + this.id_OP + '"]').val().trim();
                var cantOpDespachoPatinador = $('input[name="cantOpDespachoPatinador-' + this.id_OP + '"]').val().trim();
                var operacionPatinador = $('input[name="operacionPatinador-' + this.id_OP + '"]').val().trim();


                if (cantOpDespachoPatinador && operacionPatinador) {
                    axios.post('/blackbox/createPatinador/', {
                        id_OPPatinador: operacionPatinador,
                        selectIdTallaPatinador: OccionId_tallaPatinador, //
                        usuarioPatinador: this.usuario,
                        cantPatinador: cantOpDespachoPatinador //

                    }).then(response => {
                        // console.log(response);
                        // this.response = response.data
                        this.success = 'Data saved successfully';
                        this.response = JSON.stringify(response, null, 2);
                        document.getElementById('despachoVue-' + idOp).innerHTML =
                            '<table class="table animated fadeIn">' +
                            '<thead class="thead-dark">' +
                            '<tr>' +
                            '<th class="text-center">Nombre Talla</th>' +
                            '<th class="text-center">Talla Total</th>' +
                            '<th class="text-center">Talla Restante</th>' +
                            '</tr>' +
                            '</thead><tbody calss="table-striped table  table-sm  table-bordered table-hover" id="listKill' + idOp + '">' +
                            '<tr v-for="allTallaOP in allTallaOPs" :key="allTallaOP.id">' +

                            '<td class="text-center">[[allTallaOP.nom_talla]]</td>' +
                            '<td class="text-center">[[allTallaOP.can_talla]]' +
                            '</td><td class="text-center">[[allTallaOP.res_talla]]</td></tr>' +
                            '</tbody></table>';
                        tallasOPPatinador(idOp);
                        axios
                            .get('/blackbox/tallaOP-IncosistentePatinadores/?idOperacion=' + idOp)
                            .then((resp) => {
                                this.cantRestantePatinador = resp.data.TotalOpRestante;
                                //document.getElementById('canRestante-' + idOp).innerHTML = "Restante";
                                //console.log(this.cantRestantePatinador)
                            })
                            .catch(error => console.log(error));

                    }).catch(error => {
                        this.response = 'Error: ' + error.response.status
                    })

                }

            }
        },
        mounted: function() {
            this.getDespachoDataPatinador();
        }
    });
};





function tallasOPPatinador(idOp) {
    new Vue({
        el: '#despachoVue-' + idOp,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allTallaOPs: [],
            }
        },
        methods: {
            getDespachosTallasPatinador: function() {
                axios
                    .get('/blackbox/tallaOP-list-patinador/?idOp=' + idOp)
                    .then((resp) => {
                        this.allTallaOPs = resp.data;
                        if (resp.data == '') {
                            //alert("no hay un coño");
                            document.getElementById('despachoVue-' + idOp).innerHTML = '<h3>No hay tallas cargada</h3>';

                        }
                        //console.log(resp.data);

                    })
                    .catch(error => console.log(error))
            }
        },
        mounted: function() {
            this.getDespachosTallasPatinador()
        }

    });

}
/* function despachoOP(idOp, usuario) {
    new Vue({
        el: '#despachoVueAccion',
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allDespachoOPs: []
            }
        },
        methods: {
            delDespacho: function(id_despacho) {
                axios.delete('eliminar_despachos/' + id_despacho + '/').then(response => {
                    // console.log(response);
                    // this.response = response.data
                    this.success = 'Data eliminada';
                    this.response = JSON.stringify(response, null, 2)
                }).catch(error => {
                    this.response = 'Error: ' + error.response.status
                })
            },

            getDespachoS: function() {
                axios
                    .get('list/?idOp=' + idOp + '&usuario=' + usuario)
                    .then((resp) => {
                        this.allDespachoOPs = resp.data;
                    })
                    .catch(error => console.log(error));
            }
        },
        mounted: function() {
            this.getDespachoS();
        }
    });

} */