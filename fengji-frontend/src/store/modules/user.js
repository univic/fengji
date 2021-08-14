import types from "../types";

const state = {
  userIdentity: '123',
  myReportGroup: null,
}

let getters = {
  count(state) {
    return state.count
  },
  myReportGroup(state) {
    return state.myReportGroup
  },
}

const mutations = {
  [types.SET_USER_IDENTITY](state, payload) {
    state.userIdentity = payload;
  },
  setMyReportGroup(state, payload) {
    state.myReportGroup = payload;
  }
}

const actions = {
  increment( { commit, state } ){
    commit(types.INCREMENT)
  },
  decrement( { commit, state }) {
    commit(types.DECREMENT)
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
