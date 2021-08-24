import myAxios from "../utilities/request";
import message from "../utilities/message";

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
        return response
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
    }).then((response)=> {
      if (response.data.status === "success") {
        return response
      } else {
        message.emitErrorMessage(response.data.messages[0]);
      }
    }).catch((error) => {
        message.emitErrorMessage(error)
      })
  },
  deleteTagTemplate(params) {
    return myAxios.delete(
      'api/tag_template/',
      {
        params: params
      }
    ).catch((error) => {
      message.emitErrorMessage(error)
    })
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
