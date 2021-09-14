<template>
  <el-popover
      trigger="manual"
      v-model:visible="popoverVisible"
  >
    <div>
      <div>
        <el-cascader
            ref="cascader"
            v-bind:options="tagTemplateGroupList"
            v-bind:props="cascaderProps"
            v-on:change="handleNodeClick"
            clearable
        ></el-cascader>
        <div>
          <el-button
              type="primary"
          >确定
          </el-button>
          <el-button
              type="info"
              v-on:click="handleClosePopover"
          >取消
          </el-button>
        </div>

      </div>
      <div>
        <el-card v-if="selectedTagTemplateGroup">
          <selectable-tag
            v-for="item in selectedTagTemplateGroup.data.tag_template_list"
            v-on:selectTag="handleTagSelection(item)"
            v-bind:tag-template="item"
            v-bind:disabled="findDisableStatus(item)"
            key="item.id"
          ></selectable-tag>
        </el-card>
      </div>


    </div>
    <template #reference>
      <slot></slot>
    </template>

  </el-popover>

</template>

<script>
import selectableTag from "../item_tag/selectableTag.vue";

export default {
  name: "addTagPanel",
  components: {
    selectableTag
  },
  props: [
    'popoverVisible',
    'todoItem'
  ],
  emits: [
    'closePopover',
    'selectTag',
  ],
  data() {
    return {
      showAddTagSelector: false,
      selectedTagTemplateGroupID: null,
      selectedTagTemplateGroup: null,
      cascaderProps: {
        checkStrictly: true,      // can select parent nodes
        emitPath: false,            // return selected node only
        multiple: false,
        value: 'id',
        label: 'name',
        children: 'child_group',
      }
    };
  },
  computed: {
    tagTemplateGroupList() {
      return this.$store.getters['tagTemplateGroup/getTagTemplateGroupList'];
    },
  },
  methods: {
    handleClosePopover() {
      this.$emit('closePopover');
    },
    handleNodeClick(data) {
      this.selectedTagTemplateGroupID = data;
      this.selectedTagTemplateGroup = this.$refs.cascader.getCheckedNodes()[0];
    },
    handleTagSelection(tagTemplate) {
      // inject the pathValues here, to help upper components find where this tag template is
      tagTemplate.pathValues = this.selectedTagTemplateGroup.pathValues
      this.$emit('selectTag', tagTemplate)
    },
    findDisableStatus(tagTemplate) {
      this.todoItem.tag_list.forEach((tag) => {
        return (tag.ref_tag_template.id === tagTemplate.id)
      })
    },
  }

};
</script>

<style scoped>

</style>