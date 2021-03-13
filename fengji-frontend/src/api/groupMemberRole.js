import myAxios from "../utilities/request";
import {ElMessage} from 'element-plus';

let groupMemberRole = {
  addNewRole(dataObj) {
    return myAxios.post(
      '/api/group_member_role/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      }).catch(
      function (error) {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + error,
          type: 'error'
        });
      }
    )
  },
  getRole(params) {
    return myAxios.get(
      '/api/group_member_role/',
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
  deleteRole(params) {
    return myAxios.delete(
      'api/group_member_role/',
      {
        params: params
      }
    )
  },
  editRole(dataObj) {
    return myAxios.put(
      'api/group_member_role/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      }
    ).catch(
      function (error) {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + error,
          type: 'error'
        });
      }
    )
  }

}

export default groupMemberRole
