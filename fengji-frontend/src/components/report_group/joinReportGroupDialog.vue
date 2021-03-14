<template>
  <el-dialog
    title="加入报告组"
    v-model="dialogVisible"
    :before-close="handleClose"
  >
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
              v-on:click="handleJoin(scope.$index, scope.row)"
          >加入</el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-dialog>

</template>

<script>
// TODO fetch all available report groups and list them with a join button
// TODO need pagination

import api from '../../api';
import {ElMessage} from 'element-plus';

export default {
  name: "joinReportGroup",
  props: [
    'dialogVisible',
  ],
  emits: [
    'closeDialog',
    'refreshList'
  ],
  data() {
    return {
      reportGroupList: null,
    }
  },
  methods: {
    handleJoin() {

    },
    handleClose() {
      this.$emit('closeDialog')
    },
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
    }
  }
}
</script>

<style scoped>

</style>
