<template>
  <div style="display: flex; justify-content: flex-start">
    <div> {{ item.titleText }} </div>
    <div style="margin-left: auto">
      <i class="el-icon-more-outline"/>
      <i
        class="el-icon-close"
        style="margin-left: 20px"
        v-on:click="handleRemove"
      />
    </div>

  </div>
  <el-divider></el-divider>
</template>

<script>
export default {
  name: "basicItem",
  props: [
    'item'
  ],
  data () {
    return {
      itemTags: [
        {name: '标签1'},
        {name: '标签2'},
      ],
      tagInputVisible: false,
      tagInputValue: null,
      tagDialogVisible: false,

    }
  },
  computed: {

  },
  methods: {
    handleRemove() {
      this.$emit('removeItem', this.item.uuid)
    },
    showTagInput() {
      this.tagInputValue = true
    },
    handleInputConfirm() {

    }
  }
}
</script>

<style scoped>

</style>
