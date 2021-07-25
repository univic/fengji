<template>
  <div>
    <!--  tag group card here-->
    <el-card>
      <template #header>
        <div>
          <span> {{tagGroupElement.tag_group_name}} </span>
          <el-button v-on:click="handleEditTagGroup"
                     icon="el-icon-edit"
                     circle></el-button>
          <el-button v-on:click="handleDeleteTagGroup"
                     icon="el-icon-delete"
                     circle></el-button>
        </div>
      </template>
      <div v-if="tagGroupElement.tag_template_list && tagGroupElement.tag_template_list.length > 0">
        <tag-template-item v-for="(tagTemplateElement, index) in tagGroupElement.tag_template_list"
                           v-bind:key="tagTemplateElement.id"
                           v-bind:tagTemplateItem="tagTemplateElement"
                           v-on:editTagTemplate="handleEditTagTemplate(index)"
                           v-on:deleteTagTemplate="handleDeleteTagTemplate(index)"></tag-template-item>
      </div>
      <div v-else>
        <el-empty description="暂无数据">
        </el-empty>
      </div>

    </el-card>
  </div>
</template>

<script>
import api from "../../api";
import { ElMessage } from "element-plus";
import tagTemplateItem from './tagTemplateItem.vue';

export default {
  name: 'tagGroupDisplayCard',
  props: [
    'tagGroupElement'
  ],
  emits: [
    'deleteTagGroup',
    'editTagGroup',
    'deleteTagTemplate',
    'editTagTemplate',
  ],
  components: {
    tagTemplateItem: tagTemplateItem,
  },
  data () {
    return {}
  },
  methods: {
    handleDeleteTagGroup () {
      this.$confirm("将永久删除该标签组，是否继续", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      }).then(() => {
        if (this.tagGroupElement.tag_template_list.length === 0) {
          this.deleteTagGroup(this.tagGroupElement.id)
        } else {
          this.$message({
            message: "无法在组内有标签的情况下删除标签组",
            type: "error",
          })
        }
      }).catch(() => {
        this.$message({
          message: "已取消删除",
          type: "info",
        })
      }).catch((err) => {
        console.log(err)
      })
    },
    deleteTagGroup (tagGroupID) {
      api.tagGroup.deleteTagGroup({ id: tagGroupID }).then((response) => {
        if (response.data.status === "success") {
          this.$emit('deleteTagGroup')
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
    handleEditTagGroup () {
      this.$emit('editTagGroup')
    },
    handleEditTagTemplate (tagTemplateIndex) {
      this.$emit('editTagTemplate', tagTemplateIndex)
    },
    handleDeleteTagTemplate (tagTemplateIndex) {
      this.$emit('deleteTagTemplate', tagTemplateIndex)
    },
  }

}
</script>

<style>
</style>