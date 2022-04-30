//script vue y axios


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";






//script datatable





function DetailFormatterButInfoOperacionDespacho(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +
        '<div class="col-sm-1">' +
        '</div>' +
        '<div class="col-sm-6">' +
        '<div id="despachoVue"><template>' +
        '<table class="table border border-info ">' +
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

        '<div class="col-sm-3"><div id="FormuTallaOP"><template>' +

        '<form @submit.prevent="submitFormDespacho" class="form dark"><div hidden=True>{% csrf_token %}</div>' +

        '<div>' +
        '<select  class="form-control" v-model="selectIDPatinador"><option disabled value="">Selecciones Patinador</option>' +
        '<option id="id_pantinador"  v-for="option in allPatinadoresOPs" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select>' +

        '<select  class="form-control" v-model="selectIdTalla"><option  value="">Selecciones Talla</option>' +

        '<option id="id_talla"  v-for="(optionTalla) in allTallasOPs"  v-bind:value="optionTalla.talla"  >[[optionTalla.num_talla]] / [[optionTalla.nom_talla]]</option></select>' +
        '<input class="form-control" autocomplete="off" placeholder="Cantidad terminada" id="cant" type="number" v-model="cant" required/>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number" required/>' +
        '<br><input class="form-control btn btn-block" type="submit"  value="Guardar"></form></div></div>' + '</div>' +

        '</div></template>' +

        '</div>';

}






function DetailFormatterButAccionDespacho(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +



        '<div class="col-md-10">' +
        '<table id="items-table' + row.id +
        '"><thead><tr>' +


        '<th>Patinador</th>' +
        '<th>Talla</th>' +
        '<th>Cantidad</th>' +
        '<th>Fecha</th>' +
        '<th>Eliminar</th>' +
        '</tr></thead><tbody></tbody></table>' +

        '</div>' +



        '<center><div class="col-md-2 col-md-offset-4 align-self-center">' +
        '<button class="btn btn-sm btn-block btn-outline-danger  icofont-ui-remove" type="submit" onclick="deleteDespacho(' + row.id + ')">' +
        '</div></center>' +
        '<script type="application/javascript">' +
        '$(document).ready(function() {' +

        'var table= $("#items-table' + row.id +
        '").removeAttr("width").dataTable({  "searching": true' +
        ',serverSide: true, scrollY: "250px", scrollCollapse: true,' +




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



        '});' +


        '$("#items-table' + row.id + '").on("click", "button", function(){ table.reload() ; console.log($(this).attr("id"));' +

        '});' +


        '});' +

        '</script>' +
        '</div>';

}


function deleteDespachoUnico(id_despacho) {
    alert(id_despacho);
    axios.delete('eliminar_despachos/' + id_despacho + '/')
        .then(res => {
            console.log(res)
        })

}

function formOP(idOp, usuario) {


    new Vue({
        el: '#FormuTallaOP',
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
                        this.allTallasOPs = resp.data
                    })
                    .catch(error => console.log(error));



            },

            submitFormDespacho() {


                axios.post('/despacho/create/', {
                    id_OP: this.id_OP,
                    selectIdTalla: this.selectIdTalla,
                    selectIDPatinador: this.selectIDPatinador,
                    usuario: this.usuario,
                    cant: this.cant

                }).then(response => {
                    // console.log(response);
                    // this.response = response.data
                    this.success = 'Data saved successfully';
                    this.response = JSON.stringify(response, null, 2);

                    document.getElementById('despachoVue').innerHTML =
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
    alert(id_despacho);


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
        el: '#despachoVue',
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
                            document.getElementById('despachoVue').innerHTML = '<h3>No hay tallas cargada</h3>';

                        }
                        console.log(resp.data);



                    })
                    .catch(error => console.log(error))
            }

        },

        mounted: function() {

            this.getDespachosTallas()



        }

    });

}