import myAxios from "../utilities/request";
import message from "../utilities/message";
import {ElMessage} from 'element-plus';

let tagTemplate = {
  getTagTemplate(params) {
    return myAxios.get(
      '/api/tag_template/',
      {
        params: params
      }
    ).then((response)=> {
      if (response.data.status === "success") {
        return response
      } else {
        message.emitErrorMessage(response.data.messages[0]);
    }}).catch((error) => {
        message.emitErrorMessage(error)
      })
  },

  submitNewTag(dataObj) {
    return myAxios.post(
      '/api/tag_template/',
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
  deleteTagTemplate(params) {
    return myAxios.delete(
      'api/tag_template/',
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
  editTagTemplate(dataObj) {
    return myAxios.put(
      'api/tag_template/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      }
    )
  }
}

export default tagTemplate
