<template>
  <div

      style="width: 100%"
  >
    <!-- tag display and edit panel    -->
    <div>

      <!--          tag container -->
      <div style="width: 70%">
        <report-group-tag
            v-on:selectReportGroup="updateReportGroupList"
            v-bind:predefined-report-group="this.todoItem.report_group_list"
        ></report-group-tag>
        <el-tag
            v-for="(tagItem, tagItemIndex) in itemTags"
            :key="tagItem.tag_id"
            :closable="tagItem.tag_attr !== 'required'"
            v-on:click="handleTagSelection(tagItem, tagItemIndex)"
            v-on:close="handleTagDeletion(tagItem)"
        >
          {{ tagItem.tag_name }}
        </el-tag>
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
            <div>{{ tagSelected.tag_name }}</div>
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


    <!--    button set-->
    <div>
      <el-button
          type="primary"
          size="small"
          v-on:click="handleSave"
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
          v-on:click="handleCloseQuickEditPanel"
      >
        取消
      </el-button>
    </div>
  </div>
</template>

<script>
import itemAddTagPanel from "./itemAddTagPanel.vue";
import reportGroupTag from "../report_group/reportGroupTag.vue";

export default {
  name: "tagQuickEditPanel",
  components: {
    itemAddTagPanel,
    reportGroupTag
  },
  props: [
    'todoItem'
  ],
  emits: [
      'closeQuickEditPanel',
      'saveQuickEditPanel',
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
    handleTagSelection(tagSelected, indexOfTagSelected) {
      this.tagSelected = tagSelected
      this.indexOfTagSelected = indexOfTagSelected
    },
    handleTagDeletion(selectedTag) {
      this.itemTags.forEach(function (item, index, arr) {
        if (item.tag_id === selectedTag.tag_id) {
          arr.splice(index, 1)
        }
      })
    },
    handleSave() {
      // upon save, emit the postForm to the parent component
      this.$emit('saveQuickEditPanel', this.postForm)
    },
    showTagInput() {
      this.tagInputValue = true
    },
    handleInputConfirm() {
    },
    handleCloseQuickEditPanel () {
      this.$emit('closeQuickEditPanel')
    },
    handleCloseAddTagPopover () {
      this.addTagPopoverVisible = false
    },
    handleSubmit() {

    },
    updateReportGroupList: function (new_list) {
      this.postForm.report_group_list = new_list;
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