import api from "../../api";
import message from "../../utilities/message";

const state = {
  tagTemplateGroupList: [],
  convertedTagTemplateGroupList: [],
}

let getters = {
  getTagTemplateGroupList(state) {
    return state.tagTemplateGroupList
  },
  getConvertedTagTemplateGroupList(state) {
    return state.convertedTagTemplateGroupList
  },
}

const mutations = {
  setTagTemplateGroupList(state, payload) {
    state.tagTemplateGroupList = payload
  },
  setConvertedTagTemplateGroupList(state, payload) {
    state.convertedTagTemplateGroupList = payload
  }
}

const actions = {
  getTagTemplateGroupList(context) {
    api.tagTemplateGroup.getTagTemplateGroup({
      type: 'all',
    }).then((response) => {
        context.commit('setTagTemplateGroupList', response.data.tag_group_list);
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