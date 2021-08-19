import { ElMessage } from "element-plus";

let messagePrefix = '出现了问题（*゜ー゜*）'

function emitErrorMessage(msg) {
  ElMessage({
    message: messagePrefix + msg,
    type: 'error'
  });
}

function emitSuccessMessage(msg) {
  ElMessage({
    message: msg,
    type: 'success'
  });
}

export default {
  emitErrorMessage,
  emitSuccessMessage
}