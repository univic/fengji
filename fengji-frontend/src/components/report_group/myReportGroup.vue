<template>
  <div>
    <el-page-header content="我的报告组"></el-page-header>
    <el-divider></el-divider>
    <el-button v-on:click="handleCreateReportGroup"
    >创建报告组</el-button>
    <el-button
        v-on:click="dialogVisible = true">加入报告组</el-button>
    <edit-report-group ref="editReportGroup"
                       v-on:refreshList="handleInitialization"></edit-report-group>
    <join-report-group-dialog v-bind:dialog-visible="dialogVisible"
                              v-on:closeDialog="dialogVisible = false"
                              v-on:refreshList="handleInitialization"></join-report-group-dialog>
    <div>我创建的报告组</div>
    <el-card v-for="item in myReportGroupList">
      <template #header>
        <div>
          <span> {{item.name}} </span>
          <el-button v-on:click="handleEdit"
                     icon="el-icon-edit"
                     circle></el-button>
          <el-button v-on:click="handleDelete"
                     icon="el-icon-delete"
                     circle></el-button>
        </div>
      </template>
    </el-card>
    <div>我加入的报告组</div>
  </div>

</template>

<script>

// TODO show all the tag groups joined by the user, exhibit the group name and user's role
// TODO need to differentiate between ordinary report groups and project-like groups

import joinReportGroupDialog from './joinReportGroupDialog.vue';
import editReportGroup from "./editReportGroup.vue";

export default {
  name: "myReportGroup.vue",
  components: {
    'joinReportGroupDialog': joinReportGroupDialog,
    'editReportGroup': editReportGroup,
  },
  data () {
    return {
      dialogVisible: false,
      editDialogVisible: false,
    }
  },
  computed: {
    myReportGroupList() {
      return this.$store.state.reportGroup.myReportGroupList;
    },
  },
  created() {
    this.handleInitialization();
  },
  methods: {
    handleInitialization() {
      this.loading = true;
      this.$store.dispatch('reportGroup/getMyReportGroupList').then(this.loading = false);
    },
    handleCreateReportGroup () {
      // call the handleCreate function in child component, let it prepare the dialog title
      this.$refs.editReportGroup.handleCreate()
    }

  }

}
</script>

<style scoped>
</style>
