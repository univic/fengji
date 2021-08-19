import { createStore } from "vuex"
import getters from "./getters"
import mutations from "./mutations"
import actions from "./actions"
import user from "./modules/user"
import tagTemplate from "./modules/tagTemplate"
import tagTemplateGroup from "./modules/tagTemplateGroup";

const store = createStore({
  state() {
    return {
      count: 5
    }
  },
  getters,
  mutations,
  actions,
  modules: {
    user,
    tagTemplate,
    tagTemplateGroup,
  }
})

export default store
