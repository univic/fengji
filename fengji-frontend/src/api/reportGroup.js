import myAxios from "../utilities/request";
import message from "../utilities/message";

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
    ).then((response) => {
      if (response.data.status === "success") {
        return response;
      } else {
        message.emitErrorMessage(response.data.messages[0]);
        return response;
      }
    }).catch((error) => {
      message.emitErrorMessage(error);
      return error;
    })
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
