//script vue y axios


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";



//script datatable




function DetailFormatterButInfoOperacionDespacho(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +
        '<div class="col-sm-1">' +
        '</div>' +

        '<div class="col-sm-6"><div id="despachoVue"><template>' +
        '<table class="table border border-info ">' +
        '<thead class="thead-dark">' +
        '<tr>' +
        '<th class="text-center">Nombre Talla</th>' +
        '<th class="text-center">Can Tallas</th>' +
        '<th class="text-center">Can Restante</th>' +
        '</tr>' +
        '</thead><tbody calss="table-striped table  table-sm  table-bordered table-hover" id="listKill' + row.id + '">' +
        '<tr v-for="allTallaOP in allTallaOPs" :key="allTallaOP.id">' +
        '<td>[[allTallaOP.nom_talla]]</td><td>[[allTallaOP.can_talla]]' +
        '</td><td>[[allTallaOP.res_talla]]</td></tr>' +
        '</tbody></template></div>' +
        '</table>' + '<script type="application/javascript">' + 'tallasOP(' + row.id + '); formOP(' + row.id + ',' + row.empresa + ');' +
        '</' + 'script>' +
        '</div>' +
        '<div class="col-sm-3"><div id="FormuTallaOP"><template>' +


        '<form @submit.prevent="submitFormDespacho" class="form dark"><div hidden=True>{% csrf_token %}</div>' +

        '<div>' +
        '<select  class="form-control" v-model="selectIDPatinador"><option disabled value="">Selecciones Patinador</option>' +
        '<option id="id_pantinador"  v-for="option in allPatinadoresOPs" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select>' +

        '<select  class="form-control" v-model="selectIdTalla"><option  value="">Selecciones Talla</option>' +
        '<option id="id_talla"  v-for="(optionTalla) in allTallasOPs"  v-bind:value="optionTalla.id"  >[[optionTalla.num_talla]] / [[optionTalla.nom_talla]]</option></select>' +
        '<input class="form-control" autocomplete="off" placeholder="Cantidad terminada" id="cant" type="number" v-model="cant" required/>' +
        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number" required/>' +
        '<pre>{{data}}</pre>' +


        '<br><input class="form-control btn btn-block" type="submit" value="Guardar"></div></div>' + '</div>' +

        '</div></template>' +

        '</div>';

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
                name: '',
                id_OP: idOp,
                selectIdTalla: '',
                usuario: usuario,
                cant: '',

            }

        },
        methods: {


            getDespachoPatinadores: function() {

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
                    this.response = JSON.stringify(response, null, 2)
                }).catch(error => {
                    this.response = 'Error: ' + error.response.status
                })

            }



        },




        mounted: function() {
            this.getDespachoPatinadores();


        }

    });





};


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
                        this.allTallaOPs = resp.data
                    })
                    .catch(error => console.log(error))
            }



        },

        mounted: function() {

            this.getDespachosTallas()


        }

    });





}