
import myAxios from "../utilities/request";
import message from "../utilities/message";
import {ElMessage} from "element-plus";

const todoItem = {
  addTodoItem(dataObj) {
    return myAxios.post(
      'api/todo_item/',
      dataObj
    ).then((response)=> {
      if (response.data.status === "success") {
        return response;
      } else {
        message.emitErrorMessage(response.data.messages[0]);
        return response;
      }
    }).catch( (error) => {
      message.emitErrorMessage(error.messages);
      return error;
    })
  },
  deleteTodoItem(params) {
    return myAxios.delete(
      'api/todo_item/',
      {
        params: params
      }
    ).then(
      (response) => {
        if (response.data.status !== 'success') {
          message.emitErrorMessage(response.data.messages[0]);
        }
        return response
      }
    ).catch( (error) => {
      message.emitErrorMessage(error.messages);
      return error;
    })
  },
  editTodoItem(dataObj) {
    return myAxios.put(
      'api/todo_item/',
      dataObj,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
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
  getTodoItem(params) {
    return myAxios.get(
      '/api/todo_item/',
      {
        params: params
      }
    ).catch( (error) => {
      message.emitErrorMessage(error.messages);
      return error;
    })
  },
}

export default todoItem;
