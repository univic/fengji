
import myAxios from "../utilities/request";
import message from "../utilities/message";
import {ElMessage} from "element-plus";

const todoItem = {
  addTodoItem(dataObj) {
    return myAxios.post(
      'api/todo_item/',
      dataObj
    );
  },
  deleteTodoItem(params) {
    return myAxios.delete(
      'api/todo_item/',
      {
        params: params
      }
    ).catch(
        function (error) {
            ElMessage({
                message: '出现了问题（*゜ー゜*）' + error,
                type: 'error'
            });
        }
    )
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
    ).catch(
        function (error) {
          ElMessage({
            message: '出现了问题（*゜ー゜*）' + error,
            type: 'error'
          });
        }
    )
  },
}

export default todoItem;
