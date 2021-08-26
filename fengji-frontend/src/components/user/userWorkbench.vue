<template>
  <todo-item-list
      work-mode="Plan"
      :required-tags="requiredTags"
  >
    待办事项
  </todo-item-list>

</template>

<script>
import todoItemList from '../todo_item/todoItemList.vue';
import api from '../../api';
import {ElMessage} from 'element-plus';

export default {
  name: "userWorkbench",
  components: {
    todoItemList,
  },
  data () {
    return {
      tagTemplateList: null,
      requiredTags: [],
      loading: true,
    }
  },
  created() {
    this.handleInitialization()
  },
  computed: {
  },
  methods: {

    handleInitialization() {
      let p1 = this.$store.dispatch('tagTemplateGroup/getTagTemplateGroupList');
      let p2 = this.$store.dispatch('reportGroup/getReportGroupList');
      Promise.all([p1, p2]).then(()=>{
        console.log('resolved')
      })
    },
  }
}
</script>

<style scoped>

</style>
