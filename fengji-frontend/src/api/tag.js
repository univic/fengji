import myAxios from "../utilities/request"

let tag = {
  getTagTemplate(params) {
    return myAxios.get(
      '/api/tag_template/',
      {
        params: params
      }
    )
  },
  submitNewTag(dataObj) {
    return myAxios.post(
      '/api/tag_template/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
    })
  },
  deleteTagTemplate(params) {
    return myAxios.delete(
      'api/tag_template/',
      {
        params: params
      }
    )
  }
}

export default tag
