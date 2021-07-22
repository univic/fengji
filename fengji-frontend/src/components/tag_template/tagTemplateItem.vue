<template>
  <div>
    <el-popover>
      <template #reference>
        <el-tag>
          {{ tagTemplateItem.tag_template_name }}
        </el-tag>
      </template>
      <el-button size="mini"
                 v-on:click="handleModify">编辑</el-button>
      <el-button size="mini"
                 v-on:click="handleDelete">删除</el-button>
    </el-popover>
  </div>
</template>

<script>
export default {
  name: 'tagTemplateItem',
  props: [
    'tagTemplateItem',
  ],
  emits: [

  ],
  data () {
    return {

    }
  },
  methods: {
    handleModify () {

    },
    handleDelete () {

    },
  }

}
</script>

<style>
</style>