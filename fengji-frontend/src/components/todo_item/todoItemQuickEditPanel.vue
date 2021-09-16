<template>
  <div

      style="width: 100%"
  >
    <!-- tag display and edit panel    -->
    <div>

      <!--          tag container -->
      <div style="width: 70%">
        <report-group-tag
            v-on:selectReportGroup="handleReportGroupSelection"
            v-bind:predefined-report-group="this.todoItem.report_group"
        ></report-group-tag>
        <editable-tag
          v-for="tag in this.todoItem.tag_list"
          v-bind:tag="tag"
          v-on:deleteTag="handleDeleteTag(tag)"
        >

        </editable-tag>
        <add-tag-panel
          v-bind:todoItem="todoItem"
          v-bind:popoverVisible = "addTagPopoverVisible"
          v-on:closePopover = "handleCloseAddTagPopover"
          v-on:selectTag="handleTagSelection"
        >
          <el-button
            @click="addTagPopoverVisible = true"
            size="small"
          >
            + 新标签
          </el-button>
        </add-tag-panel>

      </div>
      </div>


  </div>
</template>

<script>
import addTagPanel from "./addTagPanel.vue";
import reportGroupTag from "../report_group/reportGroupTag.vue";
import editableTag from "../item_tag/editableTag.vue";

export default {
  name: "todoItemQuickEditPanel",
  components: {
    editableTag,
    addTagPanel,
    reportGroupTag
  },
  props: {
    'todoItem': {
      type: Object,
      default: () => {
        return { id: null }
      },
    }
  },
  emits: [
    'closeQuickEditPanel',
    'saveQuickEditPanel',
    'selectTag',
    'selectReportGroup'
  ],
  data () {
    return {
      addTagPopoverVisible: false,
      tagInputVisible: false,
      showAddTagSelector: false,
      itemTags: [],
      selectedTags : [],
      indexOfTagSelected: null,
      tagInputValue: null,
    }
  },
  computed: {

  },
  methods: {
    handleTagSelection(tagTemplate) {

      // construct a new tag list here, emit to the parent component and replace the old one
      let tagList = [];
      if (this.todoItem.tag_list) {
        tagList = this.todoItem.tag_list;
      }
      let tag = {
        name: tagTemplate.name,
        field_value: tagTemplate.default_value,
        ref_tag_template: tagTemplate,
      }
      tagList.push(tag);
      this.$emit('selectTag', tagList);
    },
    handleReportGroupSelection (reportGroupID) {
      this.$emit('selectReportGroup', reportGroupID);
    },
    handleTagValueChange(index, newValue) {
      this.tagList[index].tag_value = newValue;
    },
    handleCloseQuickEditPanel () {
      this.$emit('closeQuickEditPanel')
    },
    handleCloseAddTagPopover () {
      this.addTagPopoverVisible = false
    },
    updateTagValue: function (index, newTagValue) {
      this.tagList[index].tag_value = newTagValue;
    },
    handleDeleteTag (tag) {
      let tagList = this.todoItem.tag_list;
      this.todoItem.tag_list.some((item, index) => {
        if(item.id === tag.id) {
          tagList.splice(index, 1);
          return true;
        }
      })
      this.$emit('selectTag', tagList);
    }
  }
}
</script>

<style scoped>

.add-tag-area {
  float: right;
  width: 30%;
  height: 50px;
}
.tag-container {
  float: left;
  width: 70%;
}

</style>