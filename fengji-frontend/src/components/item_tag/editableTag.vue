<template>
  <el-tag
    closable
    v-on:click="handleTagEdit"
    v-on:close="handleDelete"
  >
    {{ tag.name }}
  </el-tag>
</template>

<script>
export default {
  name: "editableTag",
  props: {
    'tag': {
      type: Object
    }
  },
  emits: [
    'editTag',
    'deleteTag'
  ],
  methods: {
    handleTagEdit() {
      this.$emit('editTag')
    },
    handleDelete() {
      this.$emit('deleteTag')
    }
  }
};
</script>

<style scoped>

</style>