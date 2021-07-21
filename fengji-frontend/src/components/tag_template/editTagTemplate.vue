<template>
  <div>
    <!--  title here-->
    <el-page-header content="标签管理"></el-page-header>
    <div>
      <el-button v-on:click="handleTagCreate">添加标签</el-button>
      <el-button v-on:click="handleTagGroupCreate">添加标签组</el-button>
    </div>
    <tag-template-edit-panel ref="editTagTemplatePanel"
                             v-bind:dialogFormVisible="dialogFormVisible"
                             v-bind:tagGroupList="tagGroupList"
                             v-on:closeDialog="dialogFormVisible = false"
                             v-on:refreshTagList="getTagList"></tag-template-edit-panel>
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
      </el-card>
    </div>

    <!-- <el-table stripe
              :data="tagList">
      <el-table-column label="标签名"
                       prop="tag_name"></el-table-column>
      <el-table-column label="类型"
                       prop="tag_field_type"></el-table-column>
      <el-table-column label="默认值"
                       prop="tag_default_value"></el-table-column>
      <el-table-column label="必选标签"
                       prop="tag_required"></el-table-column>
      <el-table-column label="标签预览"
                       prop="tag_preview"></el-table-column>
      <el-table-column label="操作">
        <template #default="scope">
          <el-button type="text"
                     size="small"
                     v-on:click="handleTagEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button type="text"
                     size="small"
                     v-on:click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table> -->
  </div>
</template>

<script>
import tagTemplateEditPanel from "./tagTemplateEditPanel.vue";
import tagGroupEditPanel from './tagGroupEditPanel.vue';
import api from "../../api";
import { ElMessage } from "element-plus";

export default {
  name: "showTags",
  data () {
    return {
      dialogFormVisible: false,
      tagGroupDialogVisible: false,
      tagGroupList: [],
      tagList: [],
    };
  },
  components: {
    tagTemplateEditPanel: tagTemplateEditPanel,
    TagGroupEditPanel: tagGroupEditPanel,
  },
  created () {
    this.getTagData()
  },
  mounted () {

  },
  methods: {
    // use a promise to send async request
    getTagData () {
      let p1 = new Promise(this.getTagGroupList)
      let p2 = new Promise(this.getTagList)
      Promise.all([p1, p2]).then(
        console.log('oh wow')
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
    getTagList (resolve, reject) {
      api.tag.getTagTemplate({
        type: "all",
      }).then((response) => {
        if (response.data.status === "success") {
          this.tagList = response.data.tag_template_list;
          resolve('success');
        } else {
          reject("出现了问题（*゜ー゜*）" + response.data.messages[0]);
        }
      });
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
            this.tagList.splice(index, 1);
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
