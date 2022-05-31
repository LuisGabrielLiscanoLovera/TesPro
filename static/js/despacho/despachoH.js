//script vue y axios


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

//script datatable


function DetailFormatterButAccionDespachoHistorial(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +



        '<div class="col-md-10">' +
        '<table class="animated fadeIn table thead-dark text-center " id="items-table' + row.id +
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

        '<button class="btn btn-outline-success " type="submit" onclick="abrirOp(' + row.id + ')"> <h5>Activar op</h5></button>' +
        '<div class="">' + '<button value="" onclick="deleteAllDespachoHistorial(' + row.id + ')"  id="buttonEliminarAllacumulado" class="btn btn-outline-danger icofont-ui-remov ">Eliminar</button>' +
        '</div>' +
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
        '{name:"btnDelDespacho",data:4,visible:false },' +


        '],' +

        '"language": {"sProcessing": "Procesando...","sLengthMenu": "Mostrar _MENU_ registros","sZeroRecords": "No se encontraron resultados","sEmptyTable": "Ningún dato disponible","sInfo": "Registros del _START_ al _END_ de un total de _TOTAL_ registros","sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros","sInfoFiltered": "(filtrado de un total de _MAX_ registros)","sInfoPostFix": "","sSearch": "Buscar:","sUrl": "","sInfoThousands": ",","sLoadingRecords": "Cargando...","oPaginate": {"sFirst": "Primero","sLast": "Último","sNext": "Siguiente","sPrevious": "Anterior"},"oAria": {"sSortAscending": ": Activar para ordenar la columna de manera ascendente","sSortDescending": ": Activar para ordenar la columna de manera descendente"}},' +
        '"columnDefs": [{ "className": "dt-center", "targets": "_all" }],' +

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







function deleteAllDespachoHistorial(id_despacho) {
    $.ajax({
        url: 'deleteAllDespachoHistorial/',

        data: {
            'id_despacho': id_despacho,
        },
        dataType: 'json',
        success: function(data) {
            window.location.reload();

        }
    });
}




function abrirOp(id_OP) {

    axios.get('/operacion/abrirOP/?idOP=' + id_OP)
        .then((resp) => {

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

function formOPHistorial(idOp, usuario) {
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


                if (cantOpDespacho && OccionId_pantinador && operacion) {
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
                        document.getElementById('despachoVueHistorial-' + idOp).innerHTML =
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

function tallasOP(idOp) {
    new Vue({
        el: '#despachoVueHistorial-' + idOp,
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
                            document.getElementById('despachoVueHistorial-' + idOp).innerHTML = '<h3>No hay tallas cargada</h3>';

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
/* function despachoOP(idOp, usuario) {
    new Vue({
        el: '#despachoVueHistorialAccion',
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