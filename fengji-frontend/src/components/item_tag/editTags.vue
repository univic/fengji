<template>
  <!--  title here-->
  <el-page-header content="标签管理"></el-page-header>
  <div>
    <el-button v-on:click="handleTagCreate">添加标签</el-button>
    <el-button v-on:click="handleTagGroupCreate">添加标签组</el-button>
  </div>
  <div>
    <!--  tag group card here-->
    <el-card>
      <template #header>
        <div>
          <span> card header </span>
          <el-button></el-button>
        </div>
      </template>
    </el-card>
  </div>
  <tag-edit-panel
    ref="tagEditPanel"
    v-bind:dialogFormVisible="dialogFormVisible"
    v-on:closeDialog="dialogFormVisible = false"
    v-on:refreshTagList="getTagList"
  ></tag-edit-panel>
  <tag-group-edit-panel
    ref="tagGroupEditPanel"
    v-bind:dialogVisible="tagGroupDialogVisible"
    v-on:closeDialog="tagGroupDialogVisible = false"
  ></tag-group-edit-panel>
  <el-table stripe :data="tagList">
    <el-table-column label="标签名" prop="tag_name"></el-table-column>
    <el-table-column label="类型" prop="tag_field_type"></el-table-column>
    <el-table-column label="默认值" prop="tag_default_value"></el-table-column>
    <el-table-column label="必选标签" prop="tag_required"></el-table-column>
    <el-table-column label="标签预览" prop="tag_preview"></el-table-column>
    <el-table-column label="操作">
      <template #default="scope">
        <el-button
          type="text"
          size="small"
          v-on:click="handleTagEdit(scope.$index, scope.row)"
          >编辑</el-button
        >
        <el-button
          type="text"
          size="small"
          v-on:click="handleDelete(scope.$index, scope.row)"
          >删除</el-button
        >
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import tagEditPanel from "./tagEditPanel.vue";
import tagGroupEditPanel from './tagGroupEditPanel.vue';
import api from "../../api";
import { ElMessage } from "element-plus";

export default {
  name: "showTags",
  data() {
    return {
      dialogFormVisible: false,
      tagGroupDialogVisible: false,
      tagGroupList: [],
      tagList: [],
    };
  },
  components: {
    tagEditPanel: tagEditPanel,
    TagGroupEditPanel: tagGroupEditPanel,
  },
  created() {
    this.getTagList();
  },
  mounted() {},
  methods: {
    getTagGroupList() {
      api.TagGroup.getTagGroupList({
        type: 'all',
      }).then((response) => {
          if (response.data.status === "success") {
            this.tagGroupList = response.data.tag_group_list;
          } else {
            ElMessage({
              message: "出现了问题（*゜ー゜*）" + response.data.messages[0],
              type: "error",
            });
          }
      })
    },
    getTagList() {
      api.tag.getTagTemplate({
        type: "all",
      }).then((response) => {
        if (response.data.status === "success") {
          this.tagList = response.data.tag_template_list;
        } else {
          ElMessage({
            message: "出现了问题（*゜ー゜*）" + response.data.messages[0],
            type: "error",
          });
        }
      });
    },
    handleDelete(index, row) {
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
    deleteTagTemplate(index, row) {
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
    handleTagEdit(index, row) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.tagEditPanel.handleEdit(row);
      this.dialogFormVisible = true;
    },
    handleTagGroupEdit(index, row) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.tagGroupEditPanel.handleEdit(row);
      this.tagGroupDialogVisible = true;
    },
    handleTagCreate() {
      // call the handleCreate function in child component, let it prepare the dialog title
      this.$refs.tagEditPanel.handleCreate();
      this.dialogFormVisible = true;
    },
    handleTagGroupCreate() {
      this.$refs.tagGroupEditPanel.handleCreate();
      this.tagGroupDialogVisible = true;
    },
    
  },
};
</script>

<style scoped>
</style>
