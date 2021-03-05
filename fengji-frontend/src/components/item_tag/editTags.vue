<template>
  <!--  title here-->
  <div>标签管理</div>
  <div>
    <el-button
        v-on:click="dialogFormVisible = true"
    >添加标签</el-button>
  </div>
  <edit-tag-panel
    :dialogFormVisible = "dialogFormVisible"
    v-on:closeDialog="dialogFormVisible = false"
  ></edit-tag-panel>
  <el-table
    stripe
    :data="tagList"
  >
    <el-table-column label="标签名" prop="tag_name"></el-table-column>
    <el-table-column label="类型" prop="tag_type"></el-table-column>
    <el-table-column label="默认值" prop="tag_default_value"></el-table-column>
    <el-table-column label="必选标签" prop="tag_required"></el-table-column>
    <el-table-column label="标签预览" prop="tag_preview"></el-table-column>
    <el-table-column label="操作">
      <template #default>
        <el-button type="text" size="small">编辑</el-button>
        <el-button type="text" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import editTagPanel from './editTagPanel.vue';
import api from '../../api';
import { ElMessage } from 'element-plus';

export default {
  name: "showTags",
  data () {
    return {
      dialogFormVisible: false,
      tagList: [],
    }
  },
  components: {
    'editTagPanel': editTagPanel,
  },
  created() {
    this.getTagList();
  },
  mounted() {
  },
  methods: {
    getTagList() {
      api.tag.getTagList({
        type: 'all',
      }).then(
        (response) => {
          if (response.data.status === 'success') {
            this.tagList = response.data.tag_template_list
            console.log(this.tagList)
            ElMessage({
              message: response.data.messages[0],
              type: 'success'
            });
          } else {
            ElMessage({
              message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
              type: 'error'
            });
          }
        }
      ).catch(
        function (error) {
          ElMessage({
            message: '出现了问题（*゜ー゜*）' + error,
            type: 'error'
          });
        }
      )
    }


  }
}
</script>

<style scoped>

</style>
