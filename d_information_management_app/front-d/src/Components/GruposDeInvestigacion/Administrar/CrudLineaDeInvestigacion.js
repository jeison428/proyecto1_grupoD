import React, { Component } from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '../../../css/sb-admin-2.css'
import '../../../css/sb-admin-2.min.css'
import '../../../vendor/fontawesome-free/css/all.min.css'
import '../../../js/validarForm'


export default class AgregarLineaInvestigacion extends Component {
  render(){      
  return (
        <div className="row">

        <form className="p-3 col-lg-6 col-md-8 col-sm-12" onSubmit={this.onSubmit}>
          <div className="form-group">
            <input type="text" class="form-control" id="TituloLineaDeInvestigacion" placeholder="Titulo Linea de investigacion"/>
            
          </div>
          <div className="form-group">
            <textarea className="form-control" id="DescripcionLineaDeInvestigacion" placeholder="Descripción"/>
    
          </div>
          <div className="form-group">
            <input type="submit" className="form-control" id="AgrearLineaDeInvestigacion" placeholder="Agregar"/>
          </div>
        </form>
        </div> 
        )
  }
}

