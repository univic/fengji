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
        {{ item.title }}
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

    </div>
  </div>
<!--      detail panel-->
    <el-collapse-transition>
      <item-quick-edit-panel
          v-show="showDetailPanel"
      ></item-quick-edit-panel>
    </el-collapse-transition>

  <el-divider></el-divider>
</template>

<script>

import itemQuickEditPanel from "../record_item/itemQuickEditPanel.vue";
// TODO: show corresponding tags

export default {
  name: "basicItem",
  props: [
    'item'
  ],
  components: {
    itemQuickEditPanel,
  },
  emits: [
    'removeItem',
    'showDetailDialog',
  ],
  data () {
    return {
      quickTagList: null,
      showDetailPanel: false,
      tagDialogVisible: false,
      checkboxStatus: 'mouseLeave',
    }
  },
  computed: {

  },
  methods: {


  }
}
</script>

<style scoped>

</style>
