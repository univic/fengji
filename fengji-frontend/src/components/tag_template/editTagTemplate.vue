<template>
  <div>
    <!--  title here-->
    <el-page-header content="标签管理"></el-page-header>
    <el-skeleton v-if="loading === true"
                 :rows="5"
                 animated />
    <div v-else>
      <div>
        <el-button v-on:click="handleTagTemplateCreate">添加标签</el-button>
        <el-button v-on:click="handleTagGroupCreate">添加标签组</el-button>
      </div>
      <tag-template-edit-panel ref="editTagTemplatePanel"
                               v-bind:dialogFormVisible="tagTemplateDialogVisible"
                               v-bind:tagGroupList="tagGroupList"
                               v-on:closeDialog="tagTemplateDialogVisible = false"
                               v-on:refreshTagList="getTagTemplateData"></tag-template-edit-panel>
      <tag-group-edit-panel ref="tagGroupEditPanel"
                            v-bind:dialogVisible="tagGroupDialogVisible"
                            v-on:closeDialog="tagGroupDialogVisible = false"
                            v-on:refreshTagGroupList="handleListRefresh"></tag-group-edit-panel>

      <tag-group-display-card v-for="(tagGroup, index) in tagGroupList"
                              v-bind:tagGroupElement="tagGroup"
                              v-bind:key="tagGroup.id"
                              v-on:deleteTagGroup="handleTagGroupDelete(index)"
                              v-on:editTagGroup="handleTagGroupEdit(tagGroup)"
                              v-on:editTagTemplate="handleEditTagTemplate(index, $event)"
                              v-on:deleteTagTemplate="handleDeleteTagTemplate(index, $event)"></tag-group-display-card>
    </div>

  </div>
</template>

<script>

import api from "../../api";
import { ElMessage } from "element-plus";
import tagTemplateEditPanel from "./tagTemplateEditPanel.vue";
import tagGroupEditPanel from './tagGroupEditPanel.vue';
import tagGroupDisplayCard from './tagGroupDisplayCard.vue'

export default {
  name: "showTags",
  data () {
    return {
      tagTemplateDialogVisible: false,
      tagGroupDialogVisible: false,
      tagGroupList: [],
      tagTemplateList: [],
      loading: true,
    };
  },
  components: {
    tagTemplateEditPanel: tagTemplateEditPanel,
    TagGroupEditPanel: tagGroupEditPanel,
    tagGroupDisplayCard: tagGroupDisplayCard,
  },
  created () {
    this.getTagTemplateData()
  },
  mounted () {

  },
  methods: {
    // use a promise to send async request
    getTagTemplateData () {
      let p1 = new Promise(this.getTagGroupList)
      let p2 = new Promise(this.getTagTemplateList)
      Promise.all([p1, p2]).then(
        this.assignTagTemplateToTagGroup,
        this.loading = false
      ).catch((result) => {
        ElMessage({
          message: result,
          type: "error",
        })
      })
    },
    getTagGroupList (resolve, reject) {
      api.tagGroup.getTagGroup({
        type: 'all',
      }).then((response) => {
        if (response.data.status === "success") {
          this.tagGroupList = response.data.tag_group_list;
          resolve('success');
        } else {
          reject("出现了问题（*゜ー゜*）" + response.data.messages[0]);
        }
      })
    },
    getTagTemplateList (resolve, reject) {
      api.tag.getTagTemplate({
        type: "all",
      }).then((response) => {
        if (response.data.status === "success") {
          this.tagTemplateList = response.data.tag_template_list;
          resolve('success');
        } else {
          reject("出现了问题（*゜ー゜*）" + response.data.messages[0]);
        }
      });
    },
    assignTagTemplateToTagGroup () {
      this.tagGroupList.forEach((tagGroupElement, index) => {
        this.tagGroupList[index].tag_template_list = this.filterTagTemplate(tagGroupElement.id, this.tagTemplateList)
      });
    },
    filterTagTemplate (tagGroupID, tagTemplateList) {
      let filteredList = tagTemplateList.filter((item) => {
        return item.tag_group_assignment.id === tagGroupID
      })
      return filteredList
    },
    handleTagTemplateCreate () {
      // call the handleCreate function in child component, let it prepare the dialog title
      this.$refs.editTagTemplatePanel.handleCreate();
      this.tagTemplateDialogVisible = true;
    },
    handleEditTagTemplate (tagGroupIndex, tagTemplateIndex) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.editTagTemplatePanel.handleEdit(this.tagGroupList[tagGroupIndex].tag_template_list[tagTemplateIndex]);
      this.tagTemplateDialogVisible = true;
    },
    handleDeleteTagTemplate (tagGroupIndex, tagTemplateIndex) {
      this.tagGroupList[tagGroupIndex].tag_template_list.splice(tagTemplateIndex, 1)
    },
    handleTagGroupCreate () {
      this.$refs.tagGroupEditPanel.handleCreate();
      this.tagGroupDialogVisible = true;
    },
    handleTagGroupDelete (index) {
      this.tagGroupList.splice(index, 1)
    },
    handleTagGroupEdit (tagGroupElement) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.tagGroupEditPanel.handleEdit(tagGroupElement);
      this.tagGroupDialogVisible = true;
    },
    handleListRefresh () {
      this.loading = true;
      this.getTagTemplateData();
    }

  },
};
</script>

<style scoped>
</style>
