<template>
  <el-popover>
    <div>
      <el-select>

      </el-select>
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
  name: "reportGroupTag",
  data() {
    return {
      popoverVisible: false,
    }
  }
}
</script>

<style scoped>

</style>