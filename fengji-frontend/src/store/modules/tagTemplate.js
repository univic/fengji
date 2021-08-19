import types from "../types";
import api from "../../api";

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
  getTagTemplateList(context) {
    api.tagTemplate.getTagTemplate({
      type: 'all',
    }).then((response) => {
      context.commit('setTagTemplateList', response.data.tag_template_list);
      return response
    })
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}