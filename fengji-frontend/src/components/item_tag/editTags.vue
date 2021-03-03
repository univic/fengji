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
  >
    <el-table-column label="标签名"></el-table-column>
    <el-table-column label="类型"></el-table-column>
    <el-table-column label="默认值"></el-table-column>
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
import myAxios from '../../utilities/request';
import {ElMessage} from 'element-plus';

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
    getTagList () {
      myAxios.get(
          '/api/item_tag/',
          {
            params: {
              'user': ''
            }
          }
      ).then(
          function (response) {
            console.log(response.data)
            if (response.data.status === 'success') {
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
