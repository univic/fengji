import myAxios from "../utilities/request";
import axios from "axios"

const user = {
  addUser(dataObj) {
    // use axios for now, as the frontend is not complete for now
    return axios.post(
      'api/user/signup', dataObj, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      })
  },
  deleteUser(params) {
    return myAxios.delete(
      'api/user/',
      {
        params: params
      }
    )
  },
  editUser(dataObj) {
    return myAxios.put(
      'api/user/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      }
    )
  },
  getUser(params) {
    return myAxios.get(
      '/api/user/',
      {
        params: params
      }
    )
  },

}

export default user;
