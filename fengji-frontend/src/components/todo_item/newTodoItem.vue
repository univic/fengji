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


</template>

<script>
import basicTag from '../item_tag/basicTag.vue';
import reportGroupTag from "../report_group/reportGroupTag.vue";
import itemQuickEditPanel from "./itemQuickEditPanel.vue";
import itemAddTagPanel from "./itemAddTagPanel.vue";

export default {
  name: "newTodoItem",
  props: [
  ],
  components: {
    reportGroupTag,
    basicTag,
    itemAddTagPanel,
    itemQuickEditPanel,
  },
  emits: [
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
  computed: {

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
  mounted() {
    this.initializeTagList();
  },
  methods: {

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
