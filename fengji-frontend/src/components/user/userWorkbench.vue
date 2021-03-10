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
      tagTemplateList: null,
      requiredTags: [],
    }
  },
  created() {
    this.getTagTemplate();
  },
  computed: {
  },
  methods: {
    getTagTemplate() {
      api.tag.getTagTemplate({
        type: 'all',
      }).then(
          (response) => {
            if (response.data.status === 'success') {
              this.tagTemplateList = response.data.tag_template_list;
              console.log(this.tagTemplateList)
              this.setRequiredTags()
              console.log(this.requiredTags)
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              });
            }
          }
      )
    },
    setRequiredTags() {
      this.tagTemplateList.forEach((item) => {
        if (item.tag_required === true) {
          this.requiredTags = []
          this.requiredTags.push(item);
        }
      })
    }
  },

}
</script>

<style scoped>

</style>
