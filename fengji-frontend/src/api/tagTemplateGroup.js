import myAxios from '../utilities/request';
import { ElMessage } from 'element-plus';

let tagTemplateGroup = {
  addNewTagTemplateGroup(dataObj) {
    return myAxios
      .post('/api/tag_template_group/', dataObj, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      })
      .catch(function (error) {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + error,
          type: 'error',
        });
      });
  },
  getTagTemplateGroup(params) {
    return myAxios
      .get('/api/tag_template_group/', {
        params: params,
      }).then((response)=> {
        if (response.data.status === "success") {
          return response
        } else {
          ElMessage({
            message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
            type: 'error'
          });
        }
      })
      .catch(function (error) {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + error.message,
          type: 'error',
        });
      });
  },
  deleteTagTemplateGroup(params) {
    return myAxios
      .delete('api/tag_template_group/', {
        params: params,
      })
      .catch(function (error) {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + error,
          type: 'error',
        });
      });
  },
  editTagTemplateGroup(dataObj) {
    return myAxios
      .put('api/tag_template_group/', dataObj, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      })
      .catch(function (error) {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + error,
          type: 'error',
        });
      });
  },
};

export default tagTemplateGroup;
