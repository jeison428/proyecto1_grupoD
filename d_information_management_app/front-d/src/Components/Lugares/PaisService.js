import axios from 'axios';
const API_URL = 'http://localhost:8000';


export default class PaisService{


    contructor(){}
    crearPais(pais){
        const url = `${API_URL}/api/1.0/crear_pais/`;
        return axios.post(url,pais);
    }
}