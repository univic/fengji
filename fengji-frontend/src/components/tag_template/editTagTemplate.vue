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
                            v-on:closeDialog="tagGroupDialogVisible = false"></tag-group-edit-panel>

      <div>
        <!--  tag group card here-->
        <el-card v-for="tagGroup in tagGroupList"
                 v-bind:key="tagGroup.id">
          <template #header>
            <div>
              <span> {{tagGroup.tag_group_name}} </span>
              <el-button>编辑</el-button>
              <el-button>删除</el-button>
            </div>
          </template>
          <div v-if="tagGroup.tag_template_list && tagGroup.tag_template_list.length > 0">
            <tag-template-item v-for="item in tagGroup.tag_template_list"
                               v-bind:key="item.id"
                               v-bind:tagTemplateItem="item"></tag-template-item>
          </div>
          <div v-else>
            <el-empty></el-empty>
          </div>

        </el-card>
      </div>
    </div>

  </div>
</template>

<script>

import api from "../../api";
import { ElMessage } from "element-plus";
import tagTemplateEditPanel from "./tagTemplateEditPanel.vue";
import tagGroupEditPanel from './tagGroupEditPanel.vue';
import tagTemplateItem from './tagTemplateItem.vue';

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
    tagTemplateItem: tagTemplateItem,
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
    handleTagGroupEdit (index, row) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.tagGroupEditPanel.handleEdit(row);
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

  },
};
</script>

<style scoped>
</style>
