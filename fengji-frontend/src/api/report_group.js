import myAxios from "../utilities/request";

let reportGroup = {
  addNewTag(dataObj) {
    return myAxios.post(
      '/api/report_group/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      })
  }
}

export default reportGroup
