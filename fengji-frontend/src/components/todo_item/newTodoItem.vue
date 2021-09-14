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
      v-on:keypress.enter="handleSubmit"
      v-on:focus="newItemFocused=true"
      v-on:blur="newItemFocused=false"
      style="width: 80%"
      type="flex"
      align="right"
    >
    </el-input>
  </div>
  <todo-item-quick-edit-panel
    v-bind:todo-item="newItem"
    v-on:selectTag="handleTagSelection"
    v-on:selectReportGroup="handleReportGroupSelection"
  ></todo-item-quick-edit-panel>


</template>

<script>
import api from '../../api';
import basicTag from '../item_tag/basicTag.vue';
import reportGroupTag from "../report_group/reportGroupTag.vue";
import todoItemQuickEditPanel from "./todoItemQuickEditPanel.vue";
import itemAddTagPanel from "./addTagPanel.vue";

export default {
  name: "newTodoItem",
  props: [
  ],
  components: {
    reportGroupTag,
    basicTag,
    itemAddTagPanel,
    todoItemQuickEditPanel,
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
  //   requiredTags: {
  //     deep: true,
  //     handler(newValue, oldValue) {
  //       this.initializeTagList();
  //     }
  //   }
  },
  mounted() {

  },
  methods: {
    handleTagSelection(tagList) {
      this.newItem.tag_list = tagList
    },
    handleReportGroupSelection(reportGroupID) {
      this.newItem.report_group = reportGroupID
    },
    handleSubmit() {
      this.newItem.title = this.newItemText;
      api.todoItem.addTodoItem(this.newItem)
        .then((response) => {
          this.$store.commit('todoItem/appendNewTodoItem', this.newItem)
          // reset variables
          this.newItemText = null;
          this.newItem = {
            title: null,
            tag_list: null,
            report_group: null,
          }
      })
    },
  }
};
</script>

<style scoped>

</style>
