<template>
  <el-popover>
    <div>
      <div>
        <el-select
            placeholder="请选择标签"
            v-model="selectedTags"
            multiple
        >
          <el-option>

          </el-option>
        </el-select>
      </div>

      <div>
        <el-button
            type="primary"
        >确定</el-button>
        <el-button
            type="info"
            v-on:click="showAddTagSelector = false"
        >取消</el-button>
      </div>
    </div>
    <template #reference>
      <slot></slot>
    </template>
  </el-popover>

</template>

<script>
export default {
  name: "itemAddTagPanel",
  data () {
    return {
      showAddTagSelector: false,
      selectedTags: [],
    }
  }

}
</script>

<style scoped>

</style>