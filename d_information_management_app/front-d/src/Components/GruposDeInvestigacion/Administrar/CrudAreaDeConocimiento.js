import React, { Component } from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '../../../css/sb-admin-2.css'
import '../../../css/sb-admin-2.min.css'
import '../../../vendor/fontawesome-free/css/all.min.css'
import '../../../js/validarForm'

export default class AgregarAreaConocimiento extends Component{
    
  render(){
  return (
        <div className="row">
          <form className="p-5 col-lg-6 col-md-8 col-sm-12" onSubmit={this.onSubmit}>
    
            <div className="form-group">
              
              <input type="text" class="form-control" id="TituloAreaDeConocimiento" placeholder="Titulo area de conocimiento"/>
              
            </div>
            <div className="form-group">
              <textarea className="form-control" id="DescripcionAreaDeConocimiento" placeholder="Descripción"/>
    
            </div>
    
            <div className="form-group">
              <label for="Fecha Inicio">Fecha Inicio</label>
              <input type="date" className="form-control col-lg-5 col-md-10 col-sm-10" id="FechaInicioAreaDeConocimiento"/>
              <label for="Fecha Fin">Fecha Fin</label>
              <input type="date" className="form-control col-lg-5 col-md-10 col-sm-10" id="FechaFinAreaDeConocimiento"/>
            </div>
            <div className="form-group">
            <label for="Estado">Estado</label>
            <select className="form-control col-lg-5 col-md-10 col-sm-10" id="EstadoAreaDeConocimiento">
              <option>En Proceso</option>
              <option>Por Iniciar</option>
              <option>No Definido</option>
            </select>
          </div>
            <div className="form-group">
              <input type="submit" className="form-control" id="AgrearAreaDeConocimiento" placeholder="Agregar"/>
            </div>
          </form>
        </div> 
        )
      }
} 

