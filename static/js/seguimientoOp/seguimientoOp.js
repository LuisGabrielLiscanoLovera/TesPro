axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

function DetailFormatterButTareaSeguimiento(index, row) {

    return 'Caras de culos';
}

function DetailFormatterButInfoseguimientoOp(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'SeguimientoOp(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="SeguimientoOp-' + row.id + '">' +
        '<template><div class=" ">  <div class="row">' +


        '<div class="col-sm-4 md-1" style="overflow-x:auto;">' +
        '<label>Despaacho</label>' +
        '<table id="tableSdespacho-' + row.id + '" class="thead-dark table fixed_header">' +
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







        '<div class="col-sm-4 md-1 " style="overflow-x:auto;position:relative">' +
        '<label>Trea en produccion</label>' +
        '<div class="tableContainer">' +

        '<table id="tableSpatinador-' + row.id + '" class="thead-dark table fixed_header ">' +
        '<thead class="">' +
        '<tr>' + '<th scope="col" class="text-center">Tarea</th>' +
        '<th scope="col" class="text-center">Talla</th>' +
        '<th scope="col" class="text-center">Cantidad</th>' +
        '</tr>' +
        '</thead>' +
        '<tbody>' +
        '<tr v-for="inteP in patinadorOPListSeguimiento">' +
        '<td class="text-center">[[inteP.nomPatinador]]</td>' +
        '<td class="text-center">[[inteP.apellPatinador]]</td>' +
        '<td class="text-center">[[inteP.cedulaPatinador]]</td>' +
        '</tr>' +
        '</tbody>' +
        '</table>' +
        '</div>' +
        '</div>' +


        '<script type="application/javascript">' +
        '</' + 'script>' +

        '</div>' +
        '</div>' +
        '</div>' +
        '</div>';
}





/*

        '<div class="col-sm-4 md-1 " style="overflow-x:auto;position:relative">' +
        '<label>Integrantes en produccion</label>' +


        '<table id="tableSintegrante-' + row.id + '" class=" thead-dark table fixed_header  ">' +
        '<thead class="">' +
        '<tr>' + '<th scope="col" class="text-center">Nombre</th>' +
        '<th scope="col" class="text-center">Apellido</th>' +
        '<th scope="col" class="text-center">Cedula</th>' +
        '</tr>' +
        '</thead>' +
        '<tbody>' +
        '<tr v-for="inte in integranteOPListSeguimiento">' +
        '<td class="text-center">[[inte.nomIntegrante]]</td>' +
        '<td class="text-center">[[inte.apeIntegrante]]</td>' +
        '<td class="text-center">[[inte.cedulaIntegrante]]</td>' +
        '</tr>' +
        '</tbody>' +
        '</table>' +
        '</div>' +

                '<div class="col-sm-4 md-1 " style="overflow-x:auto;position:relative">' +
                '<label>Patinador en produccion</label>' +
                '<div class="tableContainer">' +

                '<table id="tableSpatinador-' + row.id + '" class="thead-dark table fixed_header ">' +
                '<thead class="">' +
                '<tr>' + '<th scope="col" class="text-center">Nombre</th>' +
                '<th scope="col" class="text-center">Apellido</th>' +
                '<th scope="col" class="text-center">Cedula</th>' +
                '</tr>' +
                '</thead>' +
                '<tbody>' +
                '<tr v-for="inteP in patinadorOPListSeguimiento">' +
                '<td class="text-center">[[inteP.nomPatinador]]</td>' +
                '<td class="text-center">[[inteP.apellPatinador]]</td>' +
                '<td class="text-center">[[inteP.cedulaPatinador]]</td>' +
                '</tr>' +
                '</tbody>' +
                '</table>' +
                '</div>' +
                '</div>' +
*/




function SeguimientoOp(idOperacion, idUsuario) {
    new Vue({
        el: '#SeguimientoOp-' + idOperacion,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                tallaOPListSeguimiento: [],
                integranteOPListSeguimiento: [],
                patinadorOPListSeguimiento: [],
                usuario: idUsuario,
                idOperacion: idOperacion,

            }
        },

        created() {
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


            axios.get('patinadoresOp-listSeguimiento/', {
                    params: {
                        idOperacionSeguimientoP: idOperacion,
                    }
                }).then((resp) => {
                    this.patinadorOPListSeguimiento = resp.data;
                    console.log(this.patinadorOPListSeguimiento);
                })
                .catch(error => console.log(error));


        },

    })
}