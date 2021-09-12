<template>

  <!--    main input area-->
  <div
    v-on:mouseover="newItemHighLighted=true"
    v-on:mouseout="newItemHighLighted = newItemFocused"
  >
        <span
          class="el-icon-plus"
          v-if="!newItemFocused"
          style="width: 10%"
        >
        </span>
    <span
      class="el-icon-circle-plus"
      v-else
      style="width: 10%"
    ></span>
    <el-input
      v-model="newItemText"
      v-on:keypress.enter="addRecordItem"
      v-on:focus="newItemFocused=true"
      v-on:blur="newItemFocused=false"
      style="width: 80%"
      type="flex"
      align="right"
    >
    </el-input>
  </div>
  <item-quick-edit-panel></item-quick-edit-panel>
<!--  <report-group-tag-->
<!--    v-on:selectReportGroup="updateReportGroupList"-->
<!--  ></report-group-tag>-->
<!--  <item-add-tag-panel-->
<!--    v-bind:popoverVisible="addTagPopoverVisible"-->
<!--    v-on:closePopover="handleCloseAddTagPopover"-->
<!--  >-->
<!--    <el-button-->
<!--      @click="addTagPopoverVisible = true"-->
<!--      size="small"-->
<!--    >-->
<!--      + 新标签-->
<!--    </el-button>-->
<!--  </item-add-tag-panel>-->

</template>

<script>
import basicTag from '../item_tag/basicTag.vue';
import reportGroupTag from "../report_group/reportGroupTag.vue";
import itemQuickEditPanel from "./itemQuickEditPanel.vue";
import itemAddTagPanel from "./itemAddTagPanel.vue";

export default {
  name: "newTodoItem",
  props: [
    'requiredTags'
  ],
  components: {
    reportGroupTag,
    basicTag,
    itemAddTagPanel,
    itemQuickEditPanel,
  },
  emits: [
    'addItem'
  ],
  data() {
    return {
      newItemHighLighted: false,
      newItemFocused: false,
      newItemText: null,
      rollBackText: null,
      addTagPopoverVisible: false,
      tagList: [],
      // key name must align with backstage
      newItem: {
        title: null,
        tag_list: null,
        report_group: null,
      },
    };
  },
  // the prop value of requiredTags is async assigned, so the value is assigned after the component is mounted
  // use deep watch to force the value get updated
  watch: {
    requiredTags: {
      deep: true,
      handler(newValue, oldValue) {
        this.initializeTagList();
      }
    }
  },
  computed: {},
  mounted() {
    this.initializeTagList();
  },
  methods: {
    initializeTagList() {
      this.tagList = [];
      this.requiredTags.forEach((item) => {
        // use shallow copy, or the newTagItem will point to the same address as requiredTags
        // in that case the tagList will be initialized instantly after value change due to the watcher
        let newTagItem = {...item};
        newTagItem.tag_value = item.default_value;
        this.tagList.push(newTagItem);
      });
    },
    addRecordItem() {
      this.rollBackText = this.newItemText;
      this.newItem.title = this.newItemText;
      this.newItem.tag_list = this.tagList;
      this.$emit('addItem', this.newItem);
      this.newItemText = null;
    },
    rollBack: function () {
      this.newItemText = this.rollBackText;
    },
    updateTagValue: function (index, newTagValue) {
      this.tagList[index].tag_value = newTagValue;
    },
    // upon reportGroupTag emit 'selectReportGroup', update report_group_list with the payload
    updateReportGroupList: function (new_item) {
      this.newItem.report_group = new_item;
    },
    handleCloseAddTagPopover() {
      this.addTagPopoverVisible = false
    },
  }
};
</script>

<style scoped>

</style>
