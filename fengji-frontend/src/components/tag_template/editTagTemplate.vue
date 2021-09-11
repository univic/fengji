<template>
  <div>
    <!--  title here-->
    <el-page-header content="标签管理"></el-page-header>
    <el-skeleton v-if="loading === true"
                 :rows="5"
                 animated/>
    <div v-else>
      <div>
        <el-button v-on:click="handleTagTemplateCreate">添加标签</el-button>
        <el-button v-on:click="handleTagGroupCreate">添加标签组</el-button>
      </div>
      <tag-template-edit-panel ref="editTagTemplatePanel"
                               v-bind:dialogFormVisible="tagTemplateDialogVisible"
                               v-bind:tagGroupList="tagGroupList"
                               v-on:closeDialog="tagTemplateDialogVisible = false"
                               v-on:refreshTagList="handleInitialization"></tag-template-edit-panel>
      <tag-group-edit-panel ref="tagGroupEditPanel"
                            v-bind:dialogVisible="tagGroupDialogVisible"
                            v-on:closeDialog="tagGroupDialogVisible = false"
                            v-on:refreshTagGroupList="handleListRefresh"></tag-group-edit-panel>
      <div>
        <el-tree
            v-bind:data="this.$store.state.tagTemplateGroup.tagTemplateGroupList"
            v-bind:props="treeProps"
            v-on:node-click="handleNodeClick"
        >
        </el-tree>
      </div>
      <div v-if="!selectedNode">
        TEMP
      </div>
      <tag-group-display-card
          v-else
          v-bind:tagGroupElement="selectedNode"
          v-bind:key="selectedNode.id"
          v-on:deleteTagGroup="handleTagGroupDelete(selectedNode.id)"
          v-on:editTagGroup="handleTagGroupEdit(selectedNode)"
          v-on:editTagTemplate="handleEditTagTemplate(selectedNode.id, $event)"
          v-on:deleteTagTemplate="handleDeleteTagTemplate(selectedNode.id, $event)"></tag-group-display-card>
    </div>

  </div>
</template>

<script>

import api from "../../api";
import {ElMessage} from "element-plus";
import tagTemplateEditPanel from "./tagTemplateEditPanel.vue";
import tagGroupEditPanel from './tagTemplateGroupEditPanel.vue';
import tagGroupDisplayCard from './tagTemplateGroupDisplayCard.vue';

export default {
  name: "showTags",
  data() {
    return {
      tagTemplateDialogVisible: false,
      tagGroupDialogVisible: false,
      tagGroupList: [],
      tagTemplateList: [],
      loading: true,
      treeProps: {
        value: 'id',
        label: 'name',
        children: 'child_group',
      },
      selectedNode: null,
    };
  },
  components: {
    tagTemplateEditPanel: tagTemplateEditPanel,
    TagGroupEditPanel: tagGroupEditPanel,
    tagGroupDisplayCard: tagGroupDisplayCard,
  },
  created() {
    this.handleInitialization();
  },
  mounted() {

  },
  computed() {

  },
  methods: {
    handleInitialization() {
      // this.$store.dispatch('tagTemplate/getTagTemplateList')
      this.$store.dispatch('tagTemplateGroup/getTagTemplateGroupList').then(this.loading = false);
    },
    handleNodeClick(data) {
      this.selectedNode = data;
    },
    handleTagTemplateCreate() {
      // call the handleCreate function in child component, let it prepare the dialog title
      this.$refs.editTagTemplatePanel.handleCreate();
      this.tagTemplateDialogVisible = true;
    },
    handleEditTagTemplate(tagGroupIndex, tagTemplateIndex) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.editTagTemplatePanel.handleEdit(this.tagGroupList[tagGroupIndex].tag_template_list[tagTemplateIndex]);
      this.tagTemplateDialogVisible = true;
    },
    handleDeleteTagTemplate(tagGroupIndex, tagTemplateIndex) {
      this.tagGroupList[tagGroupIndex].tag_template_list.splice(tagTemplateIndex, 1);
    },
    handleTagGroupCreate() {
      this.$refs.tagGroupEditPanel.handleCreate();
      this.tagGroupDialogVisible = true;
    },
    handleTagGroupDelete(index) {
      this.tagGroupList.splice(index, 1);
    },
    handleTagGroupEdit(tagGroupElement) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.tagGroupEditPanel.handleEdit(tagGroupElement);
      this.tagGroupDialogVisible = true;
    },
    handleListRefresh() {
      this.loading = true;
      this.handleInitialization();
    }

  },
};
</script>

<style scoped>
</style>
