import types from "../types"

const state = {
  count: 5
}

let getters = {
  count(state) {
    return state.count
  }
}

const mutations = {
  [types.INCREMENT](state) {
    state.count++
  },
  [types.DECREMENT](state) {
    state.count--
  }
}

const actions = {
  increment( { commit, state } ){
    commit(types.INCREMENT)
  },
  decrement( { commit, state }) {
    commit(types.DECREMENT)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
