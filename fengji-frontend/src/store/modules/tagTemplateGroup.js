import api from "../../api";

const state = {
  tagTemplateGroupList: [],
  convertedTagTemplateGroupList: [],
};

let getters = {
  getTagTemplateGroupList(state) {
    return state.tagTemplateGroupList;
  },
  getConvertedTagTemplateGroupList(state) {
    return state.convertedTagTemplateGroupList;
  },
};

const mutations = {
  setTagTemplateGroupList(state, payload) {
    state.tagTemplateGroupList = payload;
  },
  setConvertedTagTemplateGroupList(state, payload) {
    state.convertedTagTemplateGroupList = payload;
  }
};

const actions = {
  getTagTemplateGroupList(context) {
    return new Promise(((resolve, reject) => {
        api.tagTemplateGroup.getTagTemplateGroup({
          type: 'all',
          with_tags: true,
        }).then((response) => {
          context.commit('setTagTemplateGroupList', response.data.tag_group_list);
          resolve();
          return response;
        });
      })
    );
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};