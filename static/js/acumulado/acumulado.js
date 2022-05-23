axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";


function DetailFormatterButInfoAcumulado(index, row) {
    //crea y renderiza la tabla
    return '' +
        '<script type="application/javascript">' + 'formAcumulado(' + row.id + ',' + row.usuario + ');' +
        '</' + 'script>' +
        '<div id="FormuAcumulado-' + row.id + '">' +
        '<template>' +
        '<form @submit.prevent="submitFormAcumulado" class="form animated fadeIn border-info ">' +
        '<div hidden=True>{% csrf_token %}</div>' +

        '<input hidden=True id="usuario"   value="' + row.usuario + '" type="number"/>' +
        '<div class="row">' +
        '<div class="col-md-6 " style="position:absolute; left:0; margin: 10px 0 0 10px">' +


        '<div id="sectIntegreOC-' + row.id + '" class="resutatatIntegranteAcu-' + row.id +
        '">' +
        '<table class="thead-dark animated fadeIn">' +
        '<thead class="">' +
        '<tr><th scope="col" class="text-center">Tareas</th>' +
        '<th scope="col" class="text-center">Cantidad</th></tr>' + '</thead>' +


        '<tbody>' +
        '<tr v-for="i in allTareaAcumulados">' +
        '<td class="text-center">[[i.tarea]]</td>' +
        '<td class="text-center">[[i.cat_total_tarea]]</td>' +
        '</tr>' +

        '</tbody>' +
        '</table>' +
        '</div>' +
        '</div>' +
        '<div class="col-sm-6   offset-6" >' +
        '<div class="form-group"> ' + //<label>Integrante</label>
        '<select  id="OccionId_integrante_Acu-' + row.id +
        '" class="sectIntegrenteOnChanAcu-' + row.id + ' form-select form-select-sm form-control" v-model="selectIdIntegranteAcumulado"><option value="">Selecciones Integrante</option>' +

        '<option id="id_integrante"  v-for="(optionIntegranteACU) in allIntegrantesAcumuladoss" v-bind:value="optionIntegranteACU.id">[[optionIntegranteACU.nombres]]  [[optionIntegranteACU.apellidos]]</option></select></div>' +
        '</div>' +
        '<div class="col-sm-6 mb-2 offset-6  ">' +
        '<div class="form-group">' +
        '<select  class="form-select form-select-sm form-control" v-model="selectIDPatinadorAcumulado" id="OccionId_pantinador_Acu-' + row.id +
        '"><option  value="">Selecciones Patinador</option>' +
        '<option  v-for="option in allPatinadoresAcumulados" :value="option.id">[[option.nomPatinador]] [[option.apellPatinador]]</option></select></div>' +
        '</div>' +

        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<select  id="OccionId_tarea_Acu-' + row.id +
        '" class="form-select form-select-sm form-control " v-model="selectIdTareaAcumulado"><option value="">Selecciones Tarea</option>' +
        '<option id="id_tarea"  v-for="(optionTareaAcu) in allTareasAcumulados" v-bind:value="optionTareaAcu.id">[[optionTareaAcu.nom_tarea]] / [[optionTareaAcu.detalle]]</option></select></div>' +
        '</div>' +
        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<select  id="OccionId_talla_Acu-' + row.id +
        '" class="form-select form-control form-select-sm" v-model="selectIdTallaAcumulado"><option value="">Selecciones Talla</option>' +
        '<option id="id_talla"  v-for="(opcTareaAcu) in allTallasAcumulados"  v-bind:value="opcTareaAcu.id">[[opcTareaAcu.num_talla]] / [[opcTareaAcu.nom_talla]]</option></select></div>' +
        '</div>' +


        '<div class="col-sm-6 mb-2 offset-6">' +
        '<div class="form-group">' +
        '<input class="form-control big-button" autocomplete="off" placeholder="Cantidad terminada" id="cant_prod_Acum" name="cant_prod_Acum-' + row.id +
        '" type="number" v-model="cant_prod_Acum" required/> </div>' +
        '</div>' +



        '<div class="col-sm-6 mb-3 offset-6">' +
        '<div class="form-group  "><input class="form-control btn btn-block" type="submit"  value="Guardar"></div>' +
        '</div>' +
        '</form>' +
        '</div>' +
        '</div>' +
        '</template>';
}



function formAcumulado(idAcumulado, idUsuario) {

    new Vue({
        el: '#FormuAcumulado-' + idAcumulado,
        delimiters: ['[[', ']]'],
        data: function() {
            return {
                allTareaAcumulados: [],
                allTareasAcumulados: [],
                allTallasAcumulados: [],
                allPatinadoresAcumulados: [],
                allIntegrantesAcumuladoss: [],
                selectIdIntegranteAcumulado: '',
                selectIDPatinadorAcumulado: '',
                selectIdTareaAcumulado: '',
                selectIdTallaAcumulado: '',
                cant_prod_Acum: '',
                usuario: idUsuario,
                idAcumulado: idAcumulado,

            }
        },
        methods: {

            getAcumuladoDataIntegrante: function() {

                //evento de escucha de integrante
                const selectElement = document.querySelector(".sectIntegrenteOnChanAcu-" + idAcumulado);
                selectElement.addEventListener("change", (event) => {
                    const resutatatIntegranteAcu = document.
                    querySelector(".resutatatIntegranteAcu-" + idAcumulado);
                    const idIntegranteSelect = event.target.value;
                    //variable global prototype idIntegranteSelect
                    Vue.prototype.$varGlobalSelectIntegrAcu = idIntegranteSelect;
                    axios.get('dataAcumuladoInte-list/', {
                        params: {
                            idIntegranteSelect: this.$varGlobalSelectIntegrAcu,
                            idAcumulado: idAcumulado,
                        }
                    }).then((resp) => {
                        this.allTareaAcumulados = resp.data;
                    }).catch(error => console.log(error));







                });
            },


            getAcumuladoData: function() {
                ProduccionOP(idAcumulado);


                axios
                    .get('/integrante/integrante-list/')
                    .then((resp) => {
                        this.allIntegrantesAcumuladoss = resp.data
                    }).catch(error => console.log(error));
                axios
                    .get('/produccion/lista_patinadoresAct-prod/')
                    .then((resp) => {
                        this.allPatinadoresAcumulados = resp.data
                    }).catch(error => console.log(error));
                axios
                    .get('/tarea/tarea-list/')
                    .then((resp) => {
                        this.allTareasAcumulados = resp.data;
                    })
                    .catch(error => console.log(error));
                axios
                    .get('/talla/tallaEmpresa-list/?idOp=' + idAcumulado)
                    .then((resp) => {
                        this.allTallasAcumulados = resp.data;
                        console.log(this.allTallasAcumulados);
                    }).catch(error => console.log(error));

            },

            submitFormAcumulado: function() {
                var OccionId_integrante_Acu = $('select[id="OccionId_integrante_Acu-' + this.idAcumulado + '"]').val().trim();
                var OccionId_pantinador_Acu = $('select[id="OccionId_pantinador_Acu-' + this.idAcumulado + '"]').val().trim();
                var OccionId_tarea_Acu = $('select[id="OccionId_tarea_Acu-' + this.idAcumulado + '"]').val().trim();
                var OccionId_talla_Acu = $('select[id="OccionId_talla_Acu-' + this.idAcumulado + '"]').val().trim();
                var Cantidad_Acu = $('input[name="cant_prod_Acum-' + this.idAcumulado + '"]').val().trim();
                //crear la evaluacion de solo puede guardar los datos si cantidad esta llenna con if
                axios.post('/acumulado/cproAcumulado/', {
                    idAcumulado: idAcumulado,
                    usuario: idUsuario,
                    acumulado_id: idAcumulado,
                    OccionId_integrante_Acu: OccionId_integrante_Acu,
                    OccionId_pantinador_Acu: OccionId_pantinador_Acu, //l
                    OccionId_tarea_Acu: OccionId_tarea_Acu,
                    OccionId_talla_Acu: OccionId_talla_Acu,
                    Cantidad_Acu: Cantidad_Acu,
                }).then(response => {


                    axios.get('dataAcumuladoInte-list/', {
                        params: {
                            idIntegranteSelect: this.$varGlobalSelectIntegrAcu,
                            idAcumulado: idAcumulado,
                        }
                    }).then((resp) => {
                        this.allTareaAcumulados = resp.data;
                    }).catch(error => console.log(error));
                })
            }
        },
        mounted: function() {
            this.getAcumuladoDataIntegrante();
            this.getAcumuladoData();
        }
    })





}