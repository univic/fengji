<template>
  <div>
    <!--  title here-->
    <el-page-header content="标签管理"></el-page-header>
    <el-skeleton v-if="loading === true"
                 :rows="5"
                 animated />
    <div v-else>
      <div>
        <el-button v-on:click="handleTagCreate">添加标签</el-button>
        <el-button v-on:click="handleTagGroupCreate">添加标签组</el-button>
      </div>
      <tag-template-edit-panel ref="editTagTemplatePanel"
                               v-bind:dialogFormVisible="dialogFormVisible"
                               v-bind:tagGroupList="tagGroupList"
                               v-on:closeDialog="dialogFormVisible = false"
                               v-on:refreshTagList="getTagTemplateList"></tag-template-edit-panel>
      <tag-group-edit-panel ref="tagGroupEditPanel"
                            v-bind:dialogVisible="tagGroupDialogVisible"
                            v-on:closeDialog="tagGroupDialogVisible = false"
                            v-on:refreshTagGroupList="handleListRefresh"></tag-group-edit-panel>

      <tag-group-display-card v-for="(tagGroup, index) in tagGroupList"
                              v-bind:tagGroupElement="tagGroup"
                              v-bind:key="tagGroup.id"
                              v-on:deleteTagGroup="tagGroupList.splice(index, 1)"
                              v-on:editTagGroup="handleTagGroupEdit(tagGroup)"></tag-group-display-card>
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
      dialogFormVisible: false,
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
    handleDelete (index, row) {
      this.$confirm("将永久删除该标签，是否继续", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.deleteTagTemplate(index, row);
        })
        .catch(() => {
          this.$message({
            message: "已取消删除",
            type: "info",
          });
        });
    },
    deleteTagTemplate (index, row) {
      api.tag
        .deleteTagTemplate({
          id: row.id,
        })
        .then((response) => {
          if (response.data.status === "success") {
            this.tagTemplateList.splice(index, 1);
            ElMessage({
              message: response.data.messages[0],
              type: "success",
            });
          } else {
            ElMessage({
              message: "出现了问题（*゜ー゜*）" + response.data.messages[0],
              type: "error",
            });
          }
        });
    },
    handleTagEdit (index, row) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.editTagTemplatePanel.handleEdit(row);
      this.dialogFormVisible = true;
    },
    handleTagGroupEdit (tagGroupElement) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.tagGroupEditPanel.handleEdit(tagGroupElement);
      this.tagGroupDialogVisible = true;
    },
    handleTagCreate () {
      // call the handleCreate function in child component, let it prepare the dialog title
      this.$refs.editTagTemplatePanel.handleCreate();
      this.dialogFormVisible = true;
    },
    handleTagGroupCreate () {
      this.$refs.tagGroupEditPanel.handleCreate();
      this.tagGroupDialogVisible = true;
    },
    handleListRefresh () {
      console.log('1')
      this.loading = true;
      this.getTagTemplateData();
    }

  },
};
</script>

<style scoped>
</style>
