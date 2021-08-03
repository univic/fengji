<template>
  <div

      style="width: 100%"
  >
    <!-- tag display and edit panel    -->
    <div>

      <!--          tag container -->
      <div style="width: 70%">
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
        <item-add-tag-panel>
          <el-button
              @click="showTagInput"
              size="small"
          >
            + 新标签
          </el-button>
        </item-add-tag-panel>

        <el-button
            size="small"
            v-on:click="tagDialogVisible = true"
        >更多 >></el-button>

      <!--          edit tag-->
        <div>
          <!--            if no tag is selected...-->
          <div
              v-if="tagSelected === null"
          >
            点击上方标签，修改标签内容
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
          v-on:click="handleTagDetailPanelSave"
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
</template>

<script>
import itemAddTagPanel from "./itemAddTagPanel.vue";

export default {
  name: "tagQuickEditPanel",
  components: {
    itemAddTagPanel,
  },
  emits: [],
  data () {
    return {
      itemTags: [
        {
          tag_id: 'aaa',
          tag_name: '报告组',
          tag_attr: 'required',
          tag_priority: 1,
          tag_field_list: [
            {
              tag_field_name: '报告组ID',
              tag_field_value: 'abc',
              tag_field_type: 'text',
              tag_field_for_preview: false,
              tag_field_editable: false,
            },
            {
              tag_field_name: '报告组名称',
              tag_field_value: 'ERP产品域',
              tag_field_type: 'text',
              tag_field_for_preview: true,
              tag_field_editable: false,
            },
          ]
        },
        {
          tag_id: 'bbb',
          tag_name: '⏱工时',
          tag_attr: 'optional',
          tag_priority: 1,
          tag_field_list: [
            {
              tag_field_name: '花费工时（小时）',
              tag_field_value: 2,
              tag_field_type: 'number',
              tag_field_for_preview: true,
              tag_field_editable: true,
            },
          ]
        },
      ],
      tagSelected : null,
      indexOfTagSelected: null,
      tagInputVisible: false,
      tagInputValue: null,
      showAddTagSelector: false,
    }
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
    handleTagDetailPanelSave() {

    },
    showTagInput() {
      this.tagInputValue = true
    },
    handleInputConfirm() {
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