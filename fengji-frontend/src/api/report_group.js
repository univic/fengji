import myAxios from "../utilities/request";

let reportGroup = {
  addNewGroup(dataObj) {
    return myAxios.post(
      '/api/report_group/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      })
  },
  getReportGroup(params) {
    return myAxios.get(
      '/api/report_group/',
      {
        params: params
      }
    )
  },
  deleteReportGroup(params) {
    return myAxios.delete(
      'api/report_group/',
      {
        params: params
      }
    )
  },
  editReportGroup(dataObj) {
    return myAxios.put(
      'api/report_group/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      }
    )
  }

}

export default reportGroup
