<template>

  <item-list>
    工作记录
  </item-list>
  <item-list>
    待办事项
  </item-list>
</template>

<script>
import itemList from './itemList.vue';
import api from '../../api';
import {ElMessage} from 'element-plus';

export default {
  name: "userWorkbench",
  components: {
    itemList,
  },
  data () {
    return {
      tagTemplateList: {

      },
    }
  },
  created() {
    this.getTagTemplate()
  },
  computed: {
    requiredTags() {
      let requiredTagList = []
      this.tagTemplateList.forEach((item) => {
        if (item.is_required === true) {
          requiredTagList.push(item)
        }
      })
      return requiredTagList
    }
  },
  methods: {
    getTagTemplate() {
      api.tag.getTagTemplate({
        type: 'all',
      }).then(
          (response) => {
            if (response.data.status === 'success') {
              this.tagTemplateList = response.data.tag_template_list;
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              });
            }
          }
      )
    }
  },

}
</script>

<style scoped>

</style>
