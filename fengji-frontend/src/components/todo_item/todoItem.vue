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
        v-on:mouseenter="showCommandButtons = true"
        v-on:mouseleave="showCommandButtons = false"
        v-on:click="toggleQuickEditPanel"
      >
        {{ item.title }}
      </div>
<!--maneuver button set -->
      <div
        style="flex: 0 0 auto; text-align: start"
      >
        <div
            v-show="showCommandButtons"
          style="margin-left: auto">
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
          v-show="showQuickEditPanel"
          v-on:closeQuickEditPanel="toggleQuickEditPanel"
          v-on:saveQuickEditPanel="handleSaveQuickEditPanel"
          v-bind:todoItem="item"
      ></item-quick-edit-panel>
    </el-collapse-transition>

  <el-divider></el-divider>
</template>

<script>
import itemQuickEditPanel from "./itemQuickEditPanel.vue";
// TODO: show corresponding tags

export default {
  name: "todoItem",
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
      showQuickEditPanel: false,
      showDetailPanel: false,
      showCommandButtons: false,
      tagDialogVisible: false,
      checkboxStatus: 'mouseLeave',
      postForm: {
        id :null,
        title: null,
        tag_list: null,
        report_group_list: null,
      }
    }
  },
  computed: {

  },
  methods: {
    handleSelectReportGroup () {

    },
    handleSelectTag () {

    },
    handleSubmit () {

    },
    handleSaveQuickEditPanel (updatedElements) {
      // update the postForm
      this.postForm.tag_list = updatedElements.tag_list
      this.postForm.report_group_list = updatedElements.report_group_list
      // validate data

      //submit save
      this.handleSubmit()
    },
    toggleQuickEditPanel () {
      this.showQuickEditPanel = !this.showQuickEditPanel
    },
    handleOpenDetailPanel () {

    },
    handleCloseDetailPanel () {

    },

  }
}
</script>

<style scoped>

</style>
