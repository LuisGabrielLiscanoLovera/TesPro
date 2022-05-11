//script vue y axios


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";






//script datatable





function DetailFormatterButInfoOperacionDespacho(index, row) {
    //r = parseInt("[[progressRest]]");






    //crea y renderiza la tabla
    return '<div class="row">' +
        '<div class="col-sm-1">' +
        '</div>' +
        '<div class="col-sm-6">' +
        '<div id="despachoVue-' + row.id + '"><template>' +
        '<table class="table animated fadeIn border border border-info ">' +
        '<thead class="thead-dark">' +
        '<tr>' +
        '<th class="text-center">Nombre Talla</th>' +
        '<th class="text-center">Talla Total</th>' +
        '<th class="text-center">Talla Restante</th>' +
        '</tr>' +
        '</thead><tbody calss="table-striped table  table-sm  table-bordered table-hover" id="listKill' + row.id + '">' +
        '<tr v-for="allTallaOP in allTallaOPs" :key="allTallaOP.id">' +
        '<td>[[allTallaOP.nom_talla]]</td><td>[[allTallaOP.can_talla]]' +
        '</td><td>[[allTallaOP.res_talla]]</td></tr>' +
        '</tbody></template></div>' +
        '</table>' + '<script type="application/javascript">' + 'formOP(' + row.id + ',' + row.empresa + ');' +
        '</' + 'script>' +

        '</div>' +

        '<div class="col-sm-3"><div id="FormuTallaOP-' + row.id +
        '"><template>' +

        '<form @submit.prevent="submitFormDespacho" class="form dark"><div hidden=True>{% csrf_token %}</div>' +

        '<div>' +
        '<div class="alert alert-info"><p>Total restante [[cantRestante]] de [[total]]  </p>' +


        //'<div class="progress progress-striped"><div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="1" aria-valuemin="0" aria-valuemax="1" style="width:' +
        //'% ' +
        //'">Faltante</div></div>' +
        '<input  id="operacion-' + row.id +
        '" name="operacion-' + row.id +
        '"  type="number" hidden=True value="' + row.id +
        '"  required/>' +



        '</div> <select  class="form-control" v-model="selectIDPatinador" id="OccionId_pantinador-' + row.id +
        '"><option disabled value="">Selecciones Patinador</option>' +
        '<option  v-for="option in allPatinadoresOPs" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select>' +


        '<select  id="OccionId_talla-' + row.id +
        '" class="form-control" v-model="selectIdTalla"><option  value="">Selecciones Talla</option>' +

        '<option id="id_talla"  v-for="(optionTalla) in allTallasOPs"  v-bind:value="optionTalla.talla"  >[[optionTalla.num_talla]] / [[optionTalla.nom_talla]]</option></select>' +
        '<input class="form-control" autocomplete="off" placeholder="Cantidad terminada" id="cant" name="cantOpDespacho-' + row.id +
        '"  type="number" v-model="cant" required/>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +



        '<br><input class="form-control btn btn-block" type="submit"  value="Guardar"></form></div></div>' + '</div>' +

        '</div></template>' +

        '</div>';

}






function DetailFormatterButAccionDespacho(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +



        '<div class="col-md-10">' +
        '<table class="ag-theme-material animated fadeIn border " id="items-table' + row.id +
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

        '<button class="btn btn-outline-success " type="submit" onclick="carrarOp(' + row.id + ')"> <h5>Cerrar op</h5></button>' +

        '</div></center>' +
        '<script type="application/javascript">' +
        '$(document).ready(function() {' +

        'var table= $("#items-table' + row.id +
        '").removeAttr("width").dataTable({  "searching": true' +
        ',serverSide: true, scrollY: "250px", scrollCollapse: true,' +
        'order:[[4,"desc"]],' +




        'sAjaxSource:' +
        '"data/?idOp= ' + row.id + ' &usuario=' + row.usuario + '",' +
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
        '{name:"btnDelDespacho",data:4 },' +


        '],' +

        '"language": {"sProcessing": "Procesando...","sLengthMenu": "Mostrar _MENU_ registros","sZeroRecords": "No se encontraron resultados","sEmptyTable": "Ningún dato disponible en esta tabla","sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros","sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros","sInfoFiltered": "(filtrado de un total de _MAX_ registros)","sInfoPostFix": "","sSearch": "Buscar:","sUrl": "","sInfoThousands": ",","sLoadingRecords": "Cargando...","oPaginate": {"sFirst": "Primero","sLast": "Último","sNext": "Siguiente","sPrevious": "Anterior"},"oAria": {"sSortAscending": ": Activar para ordenar la columna de manera ascendente","sSortDescending": ": Activar para ordenar la columna de manera descendente"}},' +


        '});' +

        //reload data table despues de eliminar


        '$("#items-table' + row.id + '").on("click", "button", function(){ ' +
        '$("#items-table' + row.id + '").DataTable().ajax.reload();' +
        '$("#items-table' + row.id + '").DataTable().ajax.reload();' +

        'sleepThenAct();' +

        '});' +
        '});' +

        'function sleepThenAct() {' +
        '$("#items-table' + row.id + '").DataTable().ajax.reload();' +
        '}' +

        '</script>' +
        '</div>';

}


function carrarOp(id_OP) {

    axios.get('/operacion/cerrarOP/?idOP=' + id_OP)
        .then((resp) => {
            console.log("operacion cerrada");
            window.location.reload();
        })
        .catch(error => console.log(error));


}





function deleteDespachoUnico(id_despacho) {

    axios.delete('eliminar_despachos/' + id_despacho + '/')
        .then(res => {
            console.log(res)
        }).catch(error => console.log(error));

}



function formOP(idOp, usuario) {
    new Vue({
        el: '#FormuTallaOP-' + idOp,
        delimiters: ['[[', ']]'],

        data: function() {
            return {
                selectIDPatinador: '',
                allPatinadoresOPs: [],
                allTallasOPs: [],
                id_OP: idOp,
                selectIdTalla: '',
                usuario: usuario,
                cant: '',
                cantRestante: '',
                progressRest: '',
                total: '',
                fechaCierre: ''

            }

        },
        methods: {


            getDespachoData: function() {
                tallasOP(idOp);

                axios
                    .get('/despacho/lista_patinadoresAct/')
                    .then((resp) => {
                        this.allPatinadoresOPs = resp.data
                    })
                    .catch(error => console.log(error));
                axios
                    .get('/talla/tallaOP-list/?idOp=' + idOp)
                    .then((resp) => {
                        this.allTallasOPs = resp.data;

                    })
                    .catch(error => console.log(error));

                axios
                    .get('/talla/tallaOP-Incosistente/?idOperacion=' + idOp)
                    .then((resp) => {
                        this.cantRestante = resp.data.TotalOpRestante;

                        this.total = resp.data.CanOperacion;
                        //this.progressRest = ((resp.data.TotalOpRestante * 100) / resp.data.CanTallaTotal)
                        //document.getElementById('canRestante-' + idOp).innerHTML = "Restante";

                    })
                    .catch(error => console.log(error));



            },

            submitFormDespacho() {
                var OccionId_pantinador = $('select[id="OccionId_pantinador-' + this.id_OP + '"]').val().trim();
                var OccionId_talla = $('select[id="OccionId_talla-' + this.id_OP + '"]').val().trim();
                var cantOpDespacho = $('input[name="cantOpDespacho-' + this.id_OP + '"]').val().trim();
                var operacion = $('input[name="operacion-' + this.id_OP + '"]').val().trim();


                console.log("operacion ", operacion);

                axios.post('/despacho/create/', {
                    id_OP: operacion,
                    selectIdTalla: OccionId_talla, //
                    selectIDPatinador: OccionId_pantinador, //l
                    usuario: this.usuario,
                    cant: cantOpDespacho //

                }).then(response => {
                    // console.log(response);
                    // this.response = response.data
                    this.success = 'Data saved successfully';




                    this.response = JSON.stringify(response, null, 2);

                    document.getElementById('despachoVue-' + idOp).innerHTML =
                        '<table class="table animated fadeIn border border-info ">' +
                        '<thead class="thead-dark">' +
                        '<tr>' +
                        '<th class="text-center">Nombre Talla</th>' +
                        '<th class="text-center">Talla Total</th>' +
                        '<th class="text-center">Talla Restante</th>' +
                        '</tr>' +
                        '</thead><tbody calss="table-striped table  table-sm  table-bordered table-hover" id="listKill' + idOp + '">' +
                        '<tr v-for="allTallaOP in allTallaOPs" :key="allTallaOP.id">' +

                        '<td>[[allTallaOP.nom_talla]]</td>' +
                        '<td>[[allTallaOP.can_talla]]' +
                        '</td><td>[[allTallaOP.res_talla]]</td></tr>' +
                        '</tbody></table>';


                    tallasOP(idOp);
                    axios
                        .get('/talla/tallaOP-Incosistente/?idOperacion=' + idOp)
                        .then((resp) => {
                            this.cantRestante = resp.data.TotalOpRestante;
                            //document.getElementById('canRestante-' + idOp).innerHTML = "Restante";
                            //console.log(this.cantRestante)
                        })
                        .catch(error => console.log(error));

                }).catch(error => {
                    this.response = 'Error: ' + error.response.status
                })





            }



        },

        mounted: function() {
            this.getDespachoData();




        }
    });

};




function deleteDespacho(id_despacho) {



    axios.delete('eliminar_despachos/' + id_despacho + '/').then(response => {
        console.log(response);
        //this.response = response.data
        this.success = 'Data eliminada';
        this.response = JSON.stringify(response, null, 2)
    }).catch(error => {
        this.response = 'Error: ' + error.response.status
    })



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

function tallasOP(idOp) {

    new Vue({
        el: '#despachoVue-' + idOp,
        delimiters: ['[[', ']]'],

        data: function() {
            return {
                allTallaOPs: [],


            }

        },


        methods: {

            getDespachosTallas: function() {

                axios
                    .get('/talla/tallaOP-list/?idOp=' + idOp)
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

            this.getDespachosTallas()



        }

    });

}