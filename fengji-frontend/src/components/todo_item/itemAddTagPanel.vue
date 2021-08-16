<template>
  <el-popover
    trigger="manual"
    v-model:visible="popoverVisible"
  >
    <div>
      <div>
          <el-cascader
            v-bind:options="convertedTagTemplateList"
            v-bind:props="elCascaderProps"
            clearable
          ></el-cascader>

      </div>

      <div>
        <el-button
            type="primary"
        >确定</el-button>
        <el-button
            type="info"
            v-on:click="handleClosePopover"
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
  props: [
    'popoverVisible'
  ],
  emits: [
      'closePopover'
  ],
  data () {
    return {
      showAddTagSelector: false,
      selectedTags: [],
      elCascaderProps: {
        multiple: true,
      },
    }
  },
  computed: {
    tagTemplateList () {
      return this.$store.getters['tagTemplate/getTagTemplateList']
    },
    convertedTagTemplateList () {
      return this.$store.getters['tagTemplate/getConvertedTagTemplateList']
    },
  },
  methods: {
    handleClosePopover () {
      this.$emit('closePopover')
    },
  }

}
</script>

<style scoped>

</style>