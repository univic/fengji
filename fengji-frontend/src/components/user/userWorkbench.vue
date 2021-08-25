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
    // this.getTagTemplate();
    // this.getMyReportGroup();
  },
  computed: {
  },
  methods: {
    handleInitialization() {
      this.$store.dispatch('tagTemplateGroup/getTagTemplateGroupList').then(this.loading = false);
    },
    getMyReportGroup() {
      api.reportGroup.getReportGroup({
        type: 'my',
      }).then((response) => {
            if (response.data.status === 'success') {
              this.$store.commit('user/setMyReportGroup', response.data.report_group_list)
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              });
            }
          }
      )
    },
  }
}
</script>

<style scoped>

</style>
