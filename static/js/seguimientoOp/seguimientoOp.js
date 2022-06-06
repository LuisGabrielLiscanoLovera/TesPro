axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoseguimientoOp(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'SeguimientoOp(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="SeguimientoOp-' + row.id + '">' +
        '<template><div class="container">  <div class="row">' +


        '<div class="col-sm" style="overflow-x:auto;">' +
        '<label>Despaacho</label>' +
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





        '<div class="col-sm " style="overflow-x:auto;position:relative">' +
        '<label>Integrantes</label>' +
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
                integranteOPListSeguimiento: [],
                usuario: idUsuario,
                idOperacion: idOperacion,

            }
        },
        methods: {

            //integranteOp-listSeguimiento

            getProduccionData: function() {
                axios.get('tallaOP-listSeguimiento/', {
                        params: {
                            idOp: idOperacion,
                        }
                    }).then((resp) => {
                        this.tallaOPListSeguimiento = resp.data;
                        console.log(this.tallaOPListSeguimiento);
                    })
                    .catch(error => console.log(error));


                axios.get('integranteOp-listSeguimiento/', {
                        params: {
                            idOperacionSeguimiento: idOperacion,
                        }
                    }).then((resp) => {
                        this.integranteOPListSeguimiento = resp.data;
                        console.log(this.integranteOPListSeguimiento);
                    })
                    .catch(error => console.log(error));


            },

        },
        mounted: function() {
            this.getProduccionData();
        }
    })
}