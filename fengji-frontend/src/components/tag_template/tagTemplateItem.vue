<template>
  <div>
    <el-popover>
      <template #reference>
        <el-tag>
          {{ tagTemplateItem.name }}
        </el-tag>
      </template>
      <el-button size="mini"
                 v-on:click="handleEdit">编辑</el-button>
      <el-button size="mini"
                 v-on:click="handleDelete">删除</el-button>
    </el-popover>
  </div>
</template>

<script>
import api from "../../api";
import { ElMessage } from "element-plus";

export default {
  name: 'tagTemplateItem',
  props: [
    'tagTemplateItem',
  ],
  emits: [
    'deleteTagTemplate',
    'editTagTemplate',
  ],
  data () {
    return {

    }
  },
  methods: {
    handleEdit () {
      this.$emit('editTagTemplate')
    },

    handleDelete () {
      this.$confirm("将永久删除该标签，是否继续", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.deleteTagTemplate();
        })
        .catch(() => {
          this.$message({
            message: "已取消删除",
            type: "info",
          });
        });
    },
    deleteTagTemplate () {
      api.tagTemplate.deleteTagTemplate({
        id: this.tagTemplateItem.id,
      }).then((response) => {
        if (response.data.status === "success") {
          ElMessage({
            message: response.data.messages[0],
            type: "success",
          });
          this.$emit('deleteTagTemplate');
        } else {
          ElMessage({
            message: "出现了问题（*゜ー゜*）" + response.data.messages[0],
            type: "error",
          });
        }
      });
    },
  }

}
</script>

<style>
</style>