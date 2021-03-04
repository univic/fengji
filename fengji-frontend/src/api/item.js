
import myAxios from "../utilities/request";

const itemAPI = {
  getRecordItems() {
  },
  addRecordItem(dataObj) {
    return myAxios.post(
      'http://localhost:5000/api/item/',
      dataObj
    );
  },
}

export default itemAPI;
