import React, {Component} from 'react'

import PaisService from './PaisService'

const paisService = new PaisService();






export default class CrearPais extends Component{

    constructor (props){
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.nombre = React.createRef();
    }

    handleCreate(){
        paisService.crearPais({
            "nombre":this.nombre.current.value
        }).then((result)=>{
            alert ("pais creado!");
        }).catch(()=>{
            alert("Error");
        });
    }

    handleSubmit(event){
        this.handleCreate();
        event.preventDefault();
    }

    render(){
        return(
            <form onSubmit={this.handleSubmit}>
            <div className="form-group">
                <label>
                Nombre:</label>
                <input className="form-control" type="text" ref={this.nombre} />
                <input className="btn btn-primary" type="submit" value="Submit" />
            </div>  
            
            </form>
        )
    }




}


