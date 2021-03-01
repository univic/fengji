<template>
  <!--  title here-->
  <div>标签管理</div>
  <div>
    <el-button
        v-on:click="dialogFormVisible = true"
    >添加标签</el-button>
  </div>
  <edit-tag-panel
    :dialogFormVisible = "dialogFormVisible"
    v-on:closeDialog="dialogFormVisible = false"
  ></edit-tag-panel>
</template>

<script>
import editTagPanel from './editTagPanel.vue';

export default {
  name: "showTags",
  data () {
    return {
      dialogFormVisible: false
    }
  },
  components: {
    'editTagPanel': editTagPanel
  },
}
</script>

<style scoped>

</style>
