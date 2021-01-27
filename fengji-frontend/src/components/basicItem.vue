<template>
<!--  main item container-->
  <div>
<!--    item title text card-->
    <div style="display: flex; justify-content: flex-start">
<!--      the checkbox-->
      <div
        v-on:mouseenter="checkboxStatus = 'mouseOver'"
        v-on:mouseleave="checkboxStatus = 'mouseLeave'"
      >
        <div
          v-if="checkboxStatus === 'mouseOver'"
        >
          <svg class="icon" aria-hidden="true">
            <use xlink:href="#icon-yigouxuan"></use>
          </svg>
        </div>
        <div
          v-else
        >
          <svg class="icon" aria-hidden="true">
            <use xlink:href="#icon-weigouxuan"></use>
          </svg>
        </div>
      </div>
<!--      title content here-->
      <div
        style="flex: 1 1 auto; text-align: start"
        v-on:click="showDetailPanel = !showDetailPanel"

      >
        {{ item.titleText }}
      </div>
<!--maneuver button set -->
      <div
        style="flex: 0 0 auto; text-align: start"
      >
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
<!--      tag preview-->
      <div></div>
    </div>
  </div>
<!--      detail panel-->
    <el-collapse-transition>
      <div
          v-show="showDetailPanel"
          style="width: 100%"
      >
        <div>
          <el-divider>设置标签</el-divider>
          <div>
            <el-tag
                v-for="tag in itemTags"
                :key="tag.name"
                closable
            >
              {{ tag.name }}
            </el-tag>
            <el-input
                v-if="tagInputVisible"
                v-model="tagInputValue"
                ref="saveTagInput"
                @keyup.enter.native="handleInputConfirm"
                @blur="handleInputConfirm"
            >
            </el-input>
            <el-button
                v-else
                @click="showTagInput"
                size="small"
            >
              + 新标签
            </el-button>
            <el-button
                size="small"
                v-on:click="tagDialogVisible = true"
            >更多 >></el-button>
          </div>
        </div>
<!--        detail panel button set-->
        <div>
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
      </div>
    </el-collapse-transition>

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
        {name: '报告组'},
        {name: '⏱工时'},
        {name: '✋举手'},
      ],
      showDetailPanel: false,
      tagInputVisible: false,
      tagInputValue: null,
      tagDialogVisible: false,
      checkboxStatus: 'mouseLeave',

    }
  },
  computed: {

  },
  methods: {
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
