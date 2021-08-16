import types from "../types";

const state = {
  tagTemplateList: [],
  convertedTagTemplateList: [],
}

let getters = {
  getTagTemplateList(state) {
    return state.tagTemplateList
  },
  getConvertedTagTemplateList(state) {
    return state.convertedTagTemplateList
  },
}

const mutations = {
  setTagTemplateList(state, payload) {
    state.tagTemplateList = payload
  },
  setConvertedTagTemplateList(state, payload) {
    state.convertedTagTemplateList = payload
  }
}

const actions = {

}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}