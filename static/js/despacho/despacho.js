//script vue y axios
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";




//script datatable



$('#despachoTable').SetEditable();

function DetailFormatterButInfoOperacionDespacho(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +
        '<div class="col-sm-3">' +
        '</div>' +

        '<div class="col-sm-6"><div id="despachoVue"><template>' +
        '<table class="table border border-info ">' +
        '<thead class="thead-dark">' +
        '<tr>' +
        '<th class="text-center">Talla</th>' +
        '<th class="text-center">Can total</th>' +
        '<th class="text-center">Can Restante</th>' +
        '</tr>' +
        '</thead><tbody calss="table-striped table  table-sm  table-bordered table-hover" id="listKill' + row.id + '">' +
        '<tr v-for="allTallaOP in allTallaOPs" :key="allTallaOP.id">' +
        '<td>[[allTallaOP.nom_talla]]</td><td>[[allTallaOP.can_talla]]' +
        '</td><td>[[allTallaOP.res_talla]]</td></tr>' +
        '</tbody></template></div>' +
        '</table>' + '<script type="application/javascript">' + 'tallasOP(' + row.id + ');</' + 'script>' +
        '</div>' +

        '</div>';

}

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