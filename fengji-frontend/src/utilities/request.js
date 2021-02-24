import qs from 'qs';
import axios from "axios";

// create a customized axios instance
let myAxios = axios.create()

// set base URL according to the NODE_ENV
if (process.env.NODE_ENV === 'development') {
  myAxios.defaults.baseURL = 'http://localhost:3000';
} else if (process.env.NODE_ENV === 'production') {
  myAxios.defaults.baseURL = 'http://localhost:3000';
} else {
  console.log('NODE_ENV:' + process.env.NODE_ENV);
}

// request interceptor
myAxios.interceptors.request.use(
  (config) => {
    const token = window.localStorage.getItem('access_token');
    // equal to a if statement that check the existence of the token, if token exists, then assign it to the header
    token && (config.headers.access_token = token);
  }
)

myAxios.interceptors.response.use(
  (response) => {
    if (response.status === 200) {
      return response
    }
  }
)

export default myAxios
