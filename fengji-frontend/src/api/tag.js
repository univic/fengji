import myAxios from "../utilities/request"
import {ElMessage} from 'element-plus';

let tag = {
  getTagList() {
    return myAxios.get(
      '/api/item_tag/',
      {
        params: {
          'user': ''
        }
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
