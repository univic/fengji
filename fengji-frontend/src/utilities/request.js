import qs from 'qs';
import axios from "axios";
import Router from '../router';
import { ElMessage } from 'element-plus';

// create a customized axios instance
let myAxios = axios.create();

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
    const token = 'Bearer ' + window.localStorage.getItem('access_token');
    // equal to a if statement that check the existence of the token, if token exists, then assign it to the header
    token && (config.headers.Authorization = token);
    return config;
  }
)

myAxios.interceptors.response.use(
  (response) => {
      return response;
    },
    (error) => {
    // 402 for unauthorized, 422 for bad header or invalid token
    if (error.response.status === 401 || 422) {
      ElMessage({
        message: '出现了问题（*゜ー゜*）登陆状态异常',
        type: 'error'
      });
      Router.push({path: '/login'});
    } else {
      return error;
    }
  }
)

export default myAxios
