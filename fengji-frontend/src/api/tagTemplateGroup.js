import myAxios from '../utilities/request';
import message from "../utilities/message";

let tagTemplateGroup = {
  addNewTagTemplateGroup(dataObj) {
    return myAxios
      .post('/api/tag_template_group/', dataObj, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }).catch((error) => {
        message.emitErrorMessage(error);
      });
  },
  getTagTemplateGroup(params) {
    return myAxios
      .get('/api/tag_template_group/', {
        params: params,
      }).then((response)=> {
        if (response.data.status === "success") {
          return response;
        } else {
          message.emitErrorMessage(response.data.messages[0]);
        }
      }).catch((error) => {
        message.emitErrorMessage(error);
      });
  },
  deleteTagTemplateGroup(params) {
    return myAxios
      .delete('api/tag_template_group/', {
        params: params,
      }).catch((error) => {
        message.emitErrorMessage(error);
      });
  },
  editTagTemplateGroup(dataObj) {
    return myAxios
      .put('api/tag_template_group/', dataObj, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }).catch((error) => {
        message.emitErrorMessage(error);
      })
  },
};

export default tagTemplateGroup;
