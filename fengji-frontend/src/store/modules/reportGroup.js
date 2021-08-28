import api from "../../api";

const state = {
  reportGroupList: [],
};

let getters = {};

const mutations = {
  setReportGroupList(state, payload) {
    state.reportGroupList = payload;
  },
};

const actions = {
  getReportGroupList(context) {
    return new Promise((resolve, reject) => {
      api.reportGroup.getReportGroup({
        type: 'all',
        with_tags: true,
      }).then((response) => {
          context.commit('setReportGroupList', response.data.report_group_list);
          resolve();
        }
      );
    });
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};