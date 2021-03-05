import myAxios from "../utilities/request"

let tag = {
  getTagList(params) {
    return myAxios.get(
      '/api/item_tag/',
      {
        params: params
      }
    )
  },
  submitNewTag(dataObj) {
    return myAxios.post(
      '/api/item_tag/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
    })
  },
}

export default tag
