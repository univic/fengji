<template>
  <el-page-header content="管理报告组成员角色"></el-page-header>
  <el-divider></el-divider>
  <div>
    <el-button
        v-on:click="handleCreate"
    >添加报告组角色</el-button>
  </div>
  <edit-group-role-dialog
    :dialog-visible="dialogVisible"
    v-on:closeDialog="dialogVisible = false"
    v-on:refreshList="getRoleList"
    ref="editRoleDialog"
  ></edit-group-role-dialog>
  <el-table
      stripe
      :data="roleList"
  >
    <el-table-column label="角色缩写" prop="role_abbr"></el-table-column>
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

import api from '../../api';
import editGroupRoleDialog from './editGroupRoleDialog.vue';
import {ElMessage} from 'element-plus';

export default {
  name: "manageGroupRole",
  components: {
    'editGroupRoleDialog': editGroupRoleDialog
  },
  data() {
    return {
      roleList: [],
      dialogVisible: false
    }
  },
  created() {
    this.getRoleList();
  },
  methods: {
    getRoleList() {
      api.groupMemberRole.getRole({
        type: 'all',
      }).then((response) => {
        if (response.data.status === 'success') {
          this.roleList = response.data.group_role_list;
        } else {
          ElMessage({
            message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
            type: 'error'
          });
        }
      })
    },
    handleDelete(index, row) {
      this.$confirm(
          '将永久删除该标签，是否继续', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
        this.deleteRole(index, row)
      }).catch(() => {
        this.$message({
          message: '已取消删除',
          type: 'info'
        })
      })
    },
    handleEdit(index, row) {
      // call the handleEdit function in child component, let it prepare the dialog title and field values
      this.$refs.editRoleDialog.handleEdit(row)
      this.dialogVisible = true
    },
    handleCreate() {
      this.dialogVisible = true
    },
    deleteRole(index, row) {
      api.groupMemberRole.deleteRole({
        id: row.id
      }).then(
          (response) => {
            if (response.data.status === 'success') {
              this.roleList.splice(index, 1)
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
      )
    },

  }
}
</script>

<style scoped>

</style>
