import api from "../../api";
import {ElMessage} from "element-plus";

const state = {
  tagTemplateGroupList: [],
  convertedTagTemplateGroupList: [],
}

let getters = {
  getTagTemplateGroupList(state) {
    return state.tagTemplateList
  },
  getConvertedTagTemplateGroupList(state) {
    return state.convertedTagTemplateList
  },
}

const mutations = {
  setTagTemplateGroupList(state, payload) {
    state.tagTemplateList = payload
  },
  setConvertedTagTemplateGroupList(state, payload) {
    state.convertedTagTemplateList = payload
  }
}

const actions = {
  getTagTemplateGroupList(context) {
    api.tagTemplateGroup.getTagTemplateGroup({
      type: 'all',
    }).then((response) => {
      if (response.data.status === "success") {
        context.commit('setTagTemplateGroupList', response.data.tag_group_list)
        ElMessage({
          message: response.data.messages[0],
          type: 'success'
        });
      } else {
        ElMessage({
          message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
          type: 'error'
        });
      }
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