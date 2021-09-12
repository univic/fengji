import { createStore } from "vuex"
import getters from "./getters"
import mutations from "./mutations"
import actions from "./actions"
import user from "./modules/user"
import tagTemplate from "./modules/tagTemplate"
import tagTemplateGroup from "./modules/tagTemplateGroup";
import reportGroup from "./modules/reportGroup";
import todoItem from "./modules/todoItem";

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
    reportGroup,
    todoItem,
  }
})

export default store
