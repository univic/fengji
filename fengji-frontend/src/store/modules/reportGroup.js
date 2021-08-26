import api from "../../api";

const state = {
  reportGroupList: [],
}

let getters = {}

const mutations = {
  setReportGroupList(state, payload) {
    state.reportGroupList = payload
  },
}

const actions = {
  getReportGroupList(context) {
    api.reportGroup.getReportGroup({
    }).then((response) => {
      context.commit('setReportGroupList', response.data.report_group_list)
      }
    )
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}