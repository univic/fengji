<template>
  <el-popover
    placement="top"
    :width="160"
    v-model:visible="popoverVisible"
    title="修改标签值"
    trigger="click"
  >
    <div>
      <el-input>

      </el-input>
    </div>

    <template #reference>
      <el-tag>
        <slot></slot>
      </el-tag>
    </template>
  </el-popover>

</template>

<script>

export default {
name: "basicTag",
  data() {
  return {
    popoverVisible: false
  }
  }
}
</script>

<style scoped>

</style>
