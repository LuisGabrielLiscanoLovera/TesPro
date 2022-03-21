//script vue y axios
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";




//script datatable



$('#despachoTable').SetEditable();

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
        '</table>' + '<script type="application/javascript">' + 'tallasOP(' + row.id + '); formOP(' + row.id + ');' +
        '</' + 'script>' +
        '</div>' +
        '<div class="col-sm-3"><div id="FormuTallaOP"><template><form @submit.prevent="submitForm" class="form-inlin">' +
        '<div>' +
        '<select  class="form-control" v-model="selectedPatinador"><option disabled value="">Selecciones Patinador</option>' +
        '<option  v-for="option in allPatinadoresOPs" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select>' +

        '<select  class="form-control" v-model="selectedTalla"><option disabled value="">Selecciones Talla</option>' +
        '<option  v-for="optionTalla in allTallasOPs" :value="optionTalla.id">[[optionTalla.nom_talla]]</option></select>' +


        '<input class="form-control" placeholder="Cantidad terminada" id="name" type="number" v-model="name" required/>' +
        '</div></div>' + '</div>' +

        '</div></template>' +

        '</div>';

}






function formOP(idOp) {


    new Vue({
        el: '#FormuTallaOP',
        delimiters: ['[[', ']]'],

        data: function() {
            return {
                selectedPatinador: '',
                selectedTalla: '',
                allPatinadoresOPs: [],
                allTallasOPs: [],
                name: ''

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
                    .get('/talla/talla-list/')
                    .then((resp) => {
                        this.allTallasOPs = resp.data
                    })
                    .catch(error => console.log(error));

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