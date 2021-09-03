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
      let p2 = this.$store.dispatch('reportGroup/getMyReportGroupList');
      Promise.all([p1, p2]).then(()=>{

      })
    },
  }
}
</script>

<style scoped>

</style>
