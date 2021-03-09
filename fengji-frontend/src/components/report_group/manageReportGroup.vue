<template>
  <el-page-header content="管理报告组"></el-page-header>
  <el-divider></el-divider>

  <el-table
    stripe
    :data="reportGroupList"
  >
    <el-table-column label="组名" prop="group_name"></el-table-column>
    <el-table-column label="类型" prop="group_type"></el-table-column>
    <el-table-column label="操作">
      <template #default="scope">
        <el-button
            type="text"
            size="small"
            v-on:click="handleEdit(scope.$index, scope.row)"
        >编辑</el-button>
        <el-button
            type="text"
            size="small"
            v-on:click="handleDelete(scope.$index, scope.row)"
        >删除</el-button>
      </template>
    </el-table-column>
  </el-table>

</template>

<script>
import api from '../../api';
import {ElMessage} from 'element-plus';

export default {
  name: "editReportGroup",
  data () {
    return {
      reportGroupList: null,
    }
  },
  created() {
    this.getGroupList()
  },
  methods: {
    getGroupList() {
      api.reportGroup.getReportGroup({
        type: 'all',
      }).then(
          (response) => {
            if (response.data.status === 'success') {
              this.reportGroupList = response.data.group_list;
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              });
            }
          }
      )
    },
    handleDelete(index, row) {
      this.$confirm(
          '将永久删除该报告组，是否继续', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
        this.deleteReportGroup(index, row)
      }).catch(()=> {
        this.$message({
          message: '已取消删除',
          type: 'info'
        })
      })
    },
    deleteReportGroup(index, row) {
      api.reportGroup.deleteReportGroup({
        id: row.id
      }).then(
          (response) => {
            if (response.data.status === 'success') {
              this.getGroupList()
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
    },
    handleEdit(index, row) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      // this.$refs.tagEditPanel.handleEdit(row)
    },
    handleTagCreate() {
      // call the handleCreate function in child component, let it prepare the dialog title
      // this.$refs.tagEditPanel.handleCreate()
    }
  }
}
</script>

<style scoped>

</style>
