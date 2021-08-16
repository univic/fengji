<template>
  <el-popover
    placement="top"
    :width="160"
    v-model:visible="popoverVisible"
    title="修改标签值"
    trigger="click"
  >
    <div>

      <el-input v-model="tagValueInput">

      </el-input>
      <el-button
          v-on:click="updateTagValue"
          v-on:keyup.enter="updateTagValue"
      >确定</el-button>
    </div>

    <template #reference>
      <el-tag>
        <slot></slot>
      </el-tag>
    </template>
  </el-popover>

</template>

<script>
//TODO: need a confirm button, save the value when clicked or enter is being pressed
export default {
  name: "basicTag",
  emits: [
      'updateTagValue'
  ],
  data() {
    return {
      popoverVisible: false,
      tagValueInput: null,
      convertedTagTemplateList: [],
    }
  },

  methods: {
    updateTagValue: function () {
      this.$emit('updateTagValue', this.tagValueInput)
    }
  }
}
</script>

<style scoped>

</style>
