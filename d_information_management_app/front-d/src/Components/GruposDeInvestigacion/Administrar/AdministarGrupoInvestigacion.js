import React from 'react';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import CrudAreaDeConocimiento from './CrudAreaDeConocimiento'
import AgregarLineaInvestigacion from './CrudLineaDeInvestigacion'
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

function TabPanel(props) {
    const { children, value, index, ...other } = props;
  
    return (
      <div
        role="tabpanel"
        hidden={value !== index}
        id={`tabpanel-${index}`}
        aria-labelledby={`tab-${index}`}
        {...other}
      >
        {value === index && (
          <Box p={3}>
            <Typography>{children}</Typography>
          </Box>
        )}
      </div>
    );
  }
  
  TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.any.isRequired,
    value: PropTypes.any.isRequired,
  };
  
  function opciones(index) {
    return {
      id: `tab-${index}`,
      'aria-controls': `tab-${index}`,
    };
  }
  
  const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      backgroundColor: theme.palette.background.paper,
    },
  }));
  
  export default function SimpleTabs() {
    const classes = useStyles();
    const [value, setValue] = React.useState(0);
  
    const handleChange = (event, newValue) => {
      setValue(newValue);
    };
  
    return (
      <div className={classes.root}>
      <div className= "m-5">
        <h3>Administrar Grupo de investigación</h3>
      </div>

        
        <AppBar position="static" color="info">
          <Tabs indicatorColor="primary" textColor="primary" value={value} onChange={handleChange}>
            <Tab label="Agregar Area de conocimiento"  {...opciones(0)} />
            <Tab label="Agregar Linea de investigacion"  {...opciones(1)} />
          </Tabs>
        </AppBar>

        <TabPanel value={value} index={0}>
          <CrudAreaDeConocimiento/>
        </TabPanel>
        <TabPanel value={value} index={1}>
            <AgregarLineaInvestigacion/>
      </TabPanel>
    </div> 

    );
  }
