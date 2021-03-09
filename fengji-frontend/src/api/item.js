
import myAxios from "../utilities/request";

const itemAPI = {
  addRecordItem(dataObj) {
    return myAxios.post(
      'api/item/',
      dataObj
    );
  },
  deleteRecordItem(params) {
    return myAxios.delete(
      'api/item/',
      {
        params: params
      }
    )
  },
  editRecordItem(dataObj) {
    return myAxios.put(
      'api/item/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      }
    )
  },
  getRecordItem(params) {
    return myAxios.get(
      '/api/item/',
      {
        params: params
      }
    )
  },
}

export default itemAPI;
