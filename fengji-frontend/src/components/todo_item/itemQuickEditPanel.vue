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
          v-for="tag in this.todoItem.tag_list">

        </editable-tag>
        <el-divider></el-divider>
        <el-input
            v-if="tagInputVisible"
            v-model="tagInputValue"
            ref="saveTagInput"
            @keyup.enter.native="handleInputConfirm"
            @blur="handleInputConfirm"
        >
        </el-input>
        <item-add-tag-panel
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
        </item-add-tag-panel>

      <!--          edit tag-->
        <div>
          <!--            if no tag is selected...-->
          <div
              v-if="tagSelected === null"
          >
          </div>
          <!--            if a tag is selected, show the tag's fields and values-->
          <div
              v-else
          >
            <!--              tag title -->
            <div>{{ tagSelected.name }}</div>
            <!--              wrapper of tag value and fields-->
            <div>
              <!--                wrapper of each tag value and field item-->
              <div
                  v-for="(tagField, tagFieldIndex) in tagSelected.tag_field_list"
              >
                <div>{{ tagField.tag_field_name }}</div>
                <div>
                  <el-input
                      :placeholder="'请输入' + tagSelected.tag_name"
                      :disabled="!tagField.tag_field_editable"
                      v-model="itemTags[indexOfTagSelected].tag_field_list[tagFieldIndex].tag_field_value"
                  ></el-input>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>


  </div>
</template>

<script>
import itemAddTagPanel from "./itemAddTagPanel.vue";
import reportGroupTag from "../report_group/reportGroupTag.vue";
import editableTag from "../item_tag/editableTag.vue";

export default {
  name: "tagQuickEditPanel",
  components: {
    editableTag,
    itemAddTagPanel,
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
      tagSelected : null,
      indexOfTagSelected: null,
      tagInputValue: null,
      postForm: {
        report_group_list: [],
        tag_list: [],
      }
    }
  },
  computed: {

  },
  methods: {
    handleTagSelection(tagTemplate) {
      let tagList = this.todoItem.tag_list;
      let tag = {
        name: tagTemplate.name,
        field_value: tagTemplate.default_value
      }
      tagList.push(tag)
      this.$emit('selectTag', tagList)
    },
    handleReportGroupSelection (reportGroupID) {
      this.$emit('selectReportGroup', reportGroupID)
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