import api from "../../api";

const state = {
  myTodoItemList: [],
}

let getters = {
  getMyTodoItemList(state) {
    return state.todoItemList
  },

}

const mutations = {
  setMyTodoItemList(state, payload) {
    state.myTodoItemList = payload;
  },
  removeTodoItem(state, payload) {
    state.myTodoItemList.some((item, index) => {
      if(item.id === payload.id) {
        state.myTodoItemList.splice(index, 1);
        return true;
      }
    })
  },
  appendNewTodoItem(state, payload) {
    state.myTodoItemList.push(payload);
  },
}

const actions = {
  getMyTodoItemList(context) {
    return new Promise((resolve, reject) => {
      api.todoItem.getTodoItem({
        type: 'my',
      }).then((response) => {
        context.commit('setMyTodoItemList', response.data.todo_item_list);
        resolve();
        return response
      })
    })
  },
  // postNewTodoItem(context) {
  //   return new Promise((resolve, reject) => {
  //     api.todoItem.addTodoItem(context.state.newTodoItem)
  //       .then((response) => {
  //       resolve();
  //       return response;
  //     })
  //   })
  // },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}