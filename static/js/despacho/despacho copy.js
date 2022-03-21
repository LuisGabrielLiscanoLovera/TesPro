//script vue y axios
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";



new Vue({
    el: '#despachoVue',
    delimiters: ['[[', ']]'],

    data: function() {
        return {
            allDespachos: [],
            newDespacho: false,
            newDespachoValue: "",
            editId: null,
            oldDespacho: {}
        }



    },


    methods: {
        getDespachofromId: function(id) {
            for (var i = 0; i < this.allDespachos.length; i++) {
                if (this.allDespachos[i].id == id) {
                    return this.allDespachos[i];
                }
            }
        },
        getDespachos: function() {
            axios
                .get('/talla/tallaOP-list/?idOp=4')
                .then((resp) => {
                    this.allDespachos = resp.data
                })
                .catch(error => console.log(error))
        },





        editMode: function(id) {
            this.editId = id;
            this.oldDespacho = Object.assign({}, this.getDespachofromId(id));
        },
        deleteDespacho: function(id) {
            var despacchoList = [];
            axios
                .delete('/delete/' + id + '/')
                .then(() => {
                    for (var i = 0; i < this.allDespachos.length; i++) {
                        if (this.allDespachos[i].id !== id) {
                            despachoList.push(this.allDespachos[i]);
                        }
                    }
                    this.allDespachos = despachoList;
                })
                .catch(error => {
                    console.log(error);
                    alert("Unable to delete task. Some error occured!", error);
                })
        },
        save: function(id) {
            var newDespacho = this.getDespachofromId(id);
            axios
                .post('/update/' + id, newDespacho)
                .then(() => {
                    this.editId = null;
                    this.oldDespacho = {};
                })
                .catch(error => {
                    console.log("Error", error);
                })
        },

        cancel: function(id) {
            this.editId = null;
            for (var i = 0; i < this.allDespachos.length; i++) {
                if (this.allDespachos[i].id == id) {
                    this.allDespachos[i] = this.oldDespacho;
                    this.oldDespacho = {};
                    return
                }
            }
        },
        toggleAddDespacho: function() {
            this.newDespacho = !this.newDespacho;
            this.newDespachoValue = "";
        },
        submitNewDespacho: function() {
            var newDespacho = {
                'id': this.newDespachoValue,
                'completed': false
            }
            axios
                .post('create', newDespacho)
                .then(resp => {
                    this.newDespacho = false;
                    this.allDespachos.push(resp.data)
                })
                .catch(error => {
                    console.log("Error", error);
                })
        }
    },




    mounted: function() {

        this.getDespachos();




    }

});


//script datatable



$('#despachoTable').SetEditable();

function DetailFormatterButInfoOperacionDespacho(index, row) {
    //crea y renderiza la tabla
    return '<div class="row">' +
        '<div class="col-sm-3">' +
        '</div>' +

        '<div class="col-sm-6">' +
        '<table " class="table border border-info ">' +
        '<thead class="thead-dark">' +
        '<tr>' +
        '<th class="text-center">Talla</th>' +
        '<th class="text-center">Can total</th>' +
        '<th class="text-center">Can Restante</th>' + row.id + '-' + row.nom_operacion

        '</tr>' +
        '</thead><tbody calss="table-striped table  table-sm  table-bordered table-hover" id="listKill' + row.id + '"> </tbody>' +
        '</table>' + '<script>' + 'tallas(' + row.id + ');</' + 'script>' +
        '</div>' +

        '</div>';

}