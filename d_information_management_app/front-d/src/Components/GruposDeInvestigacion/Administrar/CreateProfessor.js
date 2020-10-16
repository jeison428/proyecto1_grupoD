/*import React, { Component } from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '../css/sb-admin-2.css'
import '../css/sb-admin-2.min.css'
import '../vendor/fontawesome-free/css/all.min.css'
import '../../../js/validarForm'


class CreateProfessor extends Component {
  
  constructor(args){
    super(args)
    this.state = {

    }
  }
  
  render(){
    return (
    <div class="row">  
        <div class="col-xl-6 col-md-7 mb-7 xs-12">
            <div class="card border-left-primary shadow h-100 py-2">
                <div class="card-body">
                    <div class="row no-gutters align-items-center">
                        <div class="col mr-4">
                            <div class="text-xs font-weight-bold text-primary text-uppercase mb-1 ">
                                <form class="needs-validation" methor novalidate>
                                    <div class="form-group row ">
                                        <div class="col-sm-12 ">
                                            <input type="number" class="form-control mb-2 col-xl-12 col-md-12 mb-12" name="inputCedula" id="inputCedula" placeholder="Cedula" required/>

                                            <input type="text" class="form-control   mb-2 col-xl-12 col-md-12 mb-12" name="inputNombres" id="inputNombres" placeholder="Nombres" required/>

                                            <input type="text" class="form-control   mb-2 col-xl-12 col-md-12 mb-12" name="inputApellidos" id="inputApellidos" placeholder="Apellidos" required/>

                                            <input type="text" class="form-control   mb-2 col-xl-12 col-md-12 mb-12" name="inputFormacionAcademica" id="inputFormacionAcademica" placeholder="Formacion academica" required/>




                                        </div>
                                    </div>
                                                    
                                    <div class="form-group row ">
                                        <input type="text" class="form-control  m-2 col-xl-6 col-md-6 mb-6" name="inputInstitucionActual" id="inputInstitucionActual" placeholder="Institucion actual" required/>
                                        <div class="form-check form-check-inline pl-4">
                                            <label class="col-form-label-sm pr-2 text-xs">¿Es interno?</label>
                                            <input class="form-check-input pl-1" type="radio" name="EsInterno" id="inlineRadioSi" value="Si"/>
                                            <label class="form-check-label" for="inlineRadioSi">Si</label>
                                        </div>
                                        <div class="form-check form-check-inline">
                                            <input class="form-check-input" type="radio" name="EsInterno" id="inlineRadioNo" value="No"/>
                                            <label class="form-check-label" for="inlineRadioNo">No</label>
                                        </div>
                                    </div>
                                                    
                                    <div class="form-group row ">


                                        <select class="custom-select pl-2  col-xl-6 col-md-6 mb-6" id="GrupoDeInvestigacion">
                                            <option selected>Grupo de investigacion</option>
                                            <option value="1">IRIS</option>
                                            <option value="2">ISIS</option>
                                            <option value="3">Requerimiento SW</option>

                                        </select>

                                        <div class="form-check form-check-inline pl-4">
                                            <label class="col-form-label-sm pr-2 text-xs">¿Es director?</label>
                                            <input class="form-check-input pl-1" type="radio" name="EsDirector" id="inlineRadioNo" value="No"/>
                                            <label class="form-check-label" for="inlineRadioSi">No</label>
                                        </div>
                                        <div class="form-check form-check-inline">
                                            <input class="form-check-input" type="radio" name="EsDirector" id="inlineRadioSi" value="Si"/>
                                            <label class="form-check-label" for="inlineRadioSi">Si</label>
                                        </div>
                                    </div>
                                            {   }        
                                    <div class="form-group row text-center">
                                        <div class="col-12">
                                            <button type="submit" class="btn btn-primary col-4">Crear</button>
                                        </div>
                                    </div>
                                </form>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>







    </div>

    )} 
}

export default CreateProfessor
*/