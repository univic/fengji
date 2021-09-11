<template>
  <el-card>
    {{ tagTemplate.name }}
  </el-card>
</template>

<script>
export default {
  name: "selectableTag",
  props: [
    'tagTemplate'
  ],
  emits: [
    'selectTag'
  ]
};
</script>

<style scoped>

</style>