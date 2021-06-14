
import myAxios from "../utilities/request";
import {ElMessage} from "element-plus";

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
    ).catch(
        function (error) {
          ElMessage({
            message: '出现了问题（*゜ー゜*）' + error,
            type: 'error'
          });
        }
    )
  },
}

export default itemAPI;
