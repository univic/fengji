import myAxios from "../utilities/request";
import {ElMessage} from 'element-plus';

let reportGroup = {
  addNewGroup(dataObj) {
    return myAxios.post(
      '/api/report_group/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      })
  },
  getReportGroup(params) {
    return myAxios.get(
      '/api/report_group/',
      {
        params: params
      }
    ).catch(
      function (error) {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + error.message,
          type: 'error'
        })
      }
    )
  },
  deleteReportGroup(params) {
    return myAxios.delete(
      'api/report_group/',
      {
        params: params
      }
    )
  },
  editReportGroup(dataObj) {
    return myAxios.put(
      'api/report_group/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      }
    )
  }

}

export default reportGroup
