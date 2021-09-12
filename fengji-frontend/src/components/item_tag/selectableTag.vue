<template>
  <el-tag
    v-on:click="handleTagSelect"
  >
    {{ tagTemplate.name }}
  </el-tag>
</template>

<script>
export default {
  name: "selectableTag",
  props: [
    'tagTemplate'
  ],
  emits: [
    'selectTag'
  ],
  methods: {
    handleTagSelect() {
      this.$emit('selectTag')
    }
  }
};
</script>

<style scoped>

</style>