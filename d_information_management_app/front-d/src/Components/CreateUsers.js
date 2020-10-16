import  React, { Component } from  'react';
import  UsuariosService  from  './UsuariosService';
const  usuariosService  =  new  UsuariosService();

class  CreateUsers  extends  Component {

    constructor(props) {
        super(props);
        this.username= React.createRef();
        this.email= React.createRef();
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    componentDidMount(){
        const { match: { params } } =  this.props;
        if(params  &&  params.pk)
        {
            usuariosService.getUsuario(params.pk).then((u)=>{
                this.username.value  =  u.username;
                this.email.value  =  u.email;
            })
        }
    }




    handleSubmit(event) {
        const { match: { params } } =  this.props;
        if(params  &&  params.pk){
            this.handleUpdate(params.pk);
        }
        else
        {
            this.handleCreate();
        }
        event.preventDefault();
    }
    handleCreate(){
        usuariosService.createUsuario(
            {
            "username":  this.username.value,
            "email":  this.email.value,
            }).then((result)=>{
                    alert("User created!");
            }).catch(()=>{
                    alert('There was an error! Please re-check your form.');
            });
    }
    handleUpdate(pk){
        usuariosService.updateUsuario(
            {
            "pk":  pk,
            "username":  this.username.value,
            "email":  this.email.value,
            }
            ).then((result)=>{
        
                alert("Usuario updated!");
            }).catch(()=>{
                alert('There was an error! Please re-check your form.');
            });
        }
    render() {
            return (
              <form onSubmit={this.handleSubmit}>
              <div className="form-group">
                <label>
                  Username</label>
                  <input className="form-control" type="text" ref={this.username} />
                <label>
                  Email</label>
                  <input className="form-control" type="email" ref={this.email}/>

                  <input className="btn btn-primary" type="submit" value="Submit" />
                </div>
              </form>
            );
    }



}

export default CreateUsers;
