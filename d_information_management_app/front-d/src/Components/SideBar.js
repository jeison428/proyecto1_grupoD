import React,{Component} from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import '../App.css';
import '../css/sb-admin-2.css'
import '../css/sb-admin-2.min.css'
import '../vendor/fontawesome-free/css/all.min.css'
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import AdministarGrupoInvestigacion from './GruposDeInvestigacion/Administrar/AdministarGrupoInvestigacion'
import Topbar from './Topbar';




function SideBar(){

const [selectedTab, setSelectedTab]= React.useState(0);

const handleChange = (event, newValue) =>{
  setSelectedTab(newValue);
}
    return(
      <>
      <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

      <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.html">
        <div class="sidebar-brand-icon rotate-n-15">
          <i class="fas fa-laugh-wink"></i>
        </div>
        <div class="sidebar-brand-text mx-3">ADMINISTRADOR</div>
      </a>

      <hr class="sidebar-divider my-0"/>

      <li class="nav-item active">
        <a class="nav-link" href="index.html">
          <i class="fas fa-fw fa-tachometer-alt"></i>
          <span>Dashboard</span></a>
      </li>
      <hr class="sidebar-divider"/>

      <div class="sidebar-heading">
        Administrar
      </div>
      <li class="nav-item">
        <Tabs orientation="vertical" indicatorColor="info" textColor="info" value={selectedTab}
              onChange={handleChange}>
                <Tab label="Grupo de investigacion"/>
                <Tab label="Profesores"/>
        </Tabs>
        
      </li>

    </ul>
    <div id="content-wrapper" class="d-flex flex-column">
        <div id="content">
          <Topbar/>
          <div class="container-fluid">
            {selectedTab===0 && <AdministarGrupoInvestigacion/>}
          </div>
        </div>
    </div>
    
    


    </>
    )
  }

  export default SideBar;



