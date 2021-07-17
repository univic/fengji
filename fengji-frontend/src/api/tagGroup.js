import myAxios from "../utilities/request";
import {ElMessage} from 'element-plus';

let tagGroup = {
  addNewTagGroup(dataObj) {
    return myAxios.post(
      '/api/tag_group/',
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
  getTagGroup(params) {
    return myAxios.get(
      '/api/tag_group/',
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
  deleteTagGroup(params) {
    return myAxios.delete(
      'api/tag_group/',
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
  editTagGroup(dataObj) {
    return myAxios.put(
      'api/tag_group/',
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

export default tagGroup
