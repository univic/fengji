import api from "../../api";

const state = {
  reportGroupList: [],
  myReportGroupList: [],
};

let getters = {};

const mutations = {
  setReportGroupList(state, payload) {
    state.reportGroupList = payload;
  },
  setMyReportGroupList(state, payload) {
    state.myReportGroupList = payload;
  },
};

const actions = {
  getReportGroupList(context) {
    return new Promise((resolve, reject) => {
      api.reportGroup.getReportGroup({
        type: 'all',
        with_descendant: true,
      }).then((response) => {
          context.commit('setReportGroupList', response.data.report_group_list);
          resolve();
        }
      );
    });
  },
  getMyReportGroupList(context) {
    return new Promise((resolve, reject) => {
      api.reportGroup.getReportGroup({
        type: 'my',
        with_descendant: true,
      }).then((response) => {
          context.commit('setMyReportGroupList', response.data.report_group_list);
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