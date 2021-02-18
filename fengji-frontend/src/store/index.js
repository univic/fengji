import { createStore } from "vuex"
import getters from "./getters"
import mutations from "./mutations"
import actions from "./actions"
import user from "./modules/user"

const store = createStore({
  state() {
    return {}
  },
  getters,
  mutations,
  actions,
  modules: {
    user,
  }

})

export default store
