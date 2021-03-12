<template>
  <el-page-header content="管理报告组成员角色"></el-page-header>
  <el-divider></el-divider>
  <div>
    <el-button
        v-on:click="handleCreate"
    >添加报告组角色</el-button>
  </div>
  <el-table
      stripe
      :data="roleList"
  >
    <el-table-column label="角色名" prop="role_name"></el-table-column>
    <el-table-column label="描述" prop="role_description"></el-table-column>
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
export default {
  name: "manageGroupRole",
  data () {
    return {
      roleList: [],
      editPanelVisible: false
    }
  },
  created() {
    this.getRoleList();
  },
  methods: {
    getRoleList() {

    },
    handleDelete(index, row) {
      this.$confirm(
          '将永久删除该标签，是否继续', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
        this.deleteTagTemplate(index, row)
      }).catch(()=> {
        this.$message({
          message: '已取消删除',
          type: 'info'
        })
      })
    },
    handleEdit(index, row) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.tagEditPanel.handleEdit(row)
      this.dialogFormVisible = true
    },
    handleCreate() {
      this.editPanelVisible = true
    }
  }

}
</script>

<style scoped>

</style>
