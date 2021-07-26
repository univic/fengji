<template>
  <div>
    <el-page-header content="我的报告组"></el-page-header>
    <el-divider></el-divider>
    <el-button type="primary"
               v-on:click="dialogVisible = true">加入报告组</el-button>
    <join-report-group-dialog v-bind:dialog-visible="dialogVisible"
                              v-on:closeDialog="dialogVisible = false"
                              v-on:refreshList="getList"></join-report-group-dialog>
    <div>已经加入的报告组</div>
    <el-card>

    </el-card>
  </div>

</template>

<script>

// TODO show all the tag groups joined by the user, exhibit the group name and user's role
// TODO need to differentiate between ordinary report groups and project-like groups

import joinReportGroupDialog from './joinReportGroupDialog.vue';
import api from '../../api';
import { ElMessage } from 'element-plus';

export default {
  name: "myReportGroup.vue",
  components: {
    'joinReportGroupDialog': joinReportGroupDialog,
  },
  data () {
    return {
      dialogVisible: false,
    }
  },
  methods: {
    getList () {
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
  }

}
</script>

<style scoped>
</style>
