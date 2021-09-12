<template>
  <el-tag
    closable
    v-on:click="handleTagEdit"
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
    'editTag'
  ],
  methods: {
    handleTagEdit() {
      this.$emit('editTag')
    }
  }
};
</script>

<style scoped>

</style>