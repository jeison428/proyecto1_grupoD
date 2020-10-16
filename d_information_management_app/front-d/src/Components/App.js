import React, { Component } from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '../css/sb-admin-2.css'
import '../css/sb-admin-2.min.css'
import '../vendor/fontawesome-free/css/all.min.css'
import { BrowserRouter } from  'react-router-dom'
import { Route} from  'react-router-dom'
import CrearPais from './Lugares/CrearPais'
import Home from './Home';

class App extends Component {
  
  render(){
      return(

          
        <BrowserRouter>

        
              <div className="content">
                <Route path="/pais/nombre"  component={CrearPais} />
                <Route path="/pais/" exact component={CrearPais} />
                <Route path="/" exact component={Home} />


              </div>
        </BrowserRouter>
        

        // <Router>
        //   <Switch>
        //   {/* <Route exact path ="/" render= {props => <Home {...props}/>}/>
        //   <Route exact path ="/administrar" render= {props => <AdministarGrupoInvestigacion {...props}/>}/> */}
        //   <Route  path="/GrupoInvestigacion/:pk"  component={CrearGrupoInvestigacion}  />
        //   <Route exact path ="/CrearGrupoInvestigacion" exact component={CrearGrupoInvestigacion}/> 
        //   </Switch>
        // </Router>




/*<body id="page-top">
    <div id="wrapper">    

        <SideBar/>

        <div id="content-wrapper" class="d-flex flex-column">
          <div id="content">
            <Topbar/>
            <div class="container-fluid">
               <AdministarGrupoInvestigacion/>
            </div>
          </div>
        </div>
  </div>
</body>
  */

      )
  }

}

export default App;