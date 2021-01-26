<template>
  <div>
    <div style="display: flex; justify-content: flex-start">
      <div
        style="flex: 1 1 auto; text-align: start"
        v-on:click="showDetailPanel = !showDetailPanel"
      >
        {{ item.titleText }}
      </div>
      <div style="margin-left: auto">
        <el-tooltip
          effect="dark"
          content="详情"
          placement="top"
        >
          <el-button
              icon="el-icon-more-outline"
              type="text"
              v-on:click="$emit('showDetailDialog')"
              style="margin-left: 20px"
          >
          </el-button>
        </el-tooltip>
        <el-tooltip
            effect="dark"
            content="删除"
            placement="top"
        >
          <el-button
            icon="el-icon-close"
            type="text"
            v-on:click="$emit('removeItem')"
          >
          </el-button>
        </el-tooltip>
      </div>

    </div>
    <el-collapse-transition>
      <div
          v-show="showDetailPanel"
      >
        <el-divider></el-divider>
        <div>
          详情
        </div>
        <el-button
          type="primary"
          size="small"
        >
          确定
        </el-button>
        <el-button
            type="primary"
            size="small"
            v-on:click="$emit('showDetailDialog')"
        >
          更多
        </el-button>
        <el-button
          size="small"
          v-on:click="showDetailPanel = false"
        >
          取消
        </el-button>
      </div>
    </el-collapse-transition>

  </div>
  <el-divider></el-divider>
</template>

<script>
export default {
  name: "basicItem",
  props: [
    'item'
  ],
  emits: [
    'removeItem',
    'showDetailDialog',
  ],
  data () {
    return {
      itemTags: [
        {name: '标签1'},
        {name: '标签2'},
      ],
      showDetailPanel: false,
      tagInputVisible: false,
      tagInputValue: null,
      tagDialogVisible: false,

    }
  },
  computed: {

  },
  methods: {
    showTagInput() {
      this.tagInputValue = true
    },
    switchDetailPanel() {
    },

  }
}
</script>

<style scoped>

</style>
