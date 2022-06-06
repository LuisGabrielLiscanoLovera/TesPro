axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoseguimientoOp(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'SeguimientoOp(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="SeguimientoOp-' + row.id + '">' +
        '<template>' +


        '<div class="col-md-4" style="overflow-x:auto;">' +

        '<table class="thead-dark table-fill">' +
        '<thead class="">' +
        '<tr>' + '<th scope="col" class="text-center">Talla</th>' +
        '<th scope="col" class="text-center">Can Total</th>' +
        '<th scope="col" class="text-center">Can Restante</th>' +
        '</tr>' +
        '</thead>' +
        '<tbody>' +
        '<tr v-for="i in tallaOPListSeguimiento">' +
        '<td class="text-center">[[i.nom_talla]]</td>' +
        '<td class="text-center">[[i.can_talla]]</td>' +
        '<td class="text-center">[[i.res_talla]]</td>' +
        '</tr>' +
        '</tbody>' +
        '</table>' +
        '</div>' +
        '</div>' +
        '</div>';
}


function SeguimientoOp(idOperacion, idUsuario) {
    new Vue({
        el: '#SeguimientoOp-' + idOperacion,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                tallaOPListSeguimiento: [],
                usuario: idUsuario,
                idOperacion: idOperacion,

            }
        },
        methods: {



            getProduccionData: function() {
                axios.get('/talla/tallaOP-list/', {
                        params: {
                            idOp: idOperacion,
                        }
                    }).then((resp) => {
                        this.tallaOPListSeguimiento = resp.data;
                        console.log(this.tallaOPListSeguimiento);
                    })
                    .catch(error => console.log(error));


            },

        },
        mounted: function() {
            this.getProduccionData();
        }
    })
}