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
  appendNewTodoItem(state, payload) {
    state.todoItemList.push(payload);
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