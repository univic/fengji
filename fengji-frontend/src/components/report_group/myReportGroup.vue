<template>
  <div>
    <el-page-header content="我的报告组"></el-page-header>
    <el-divider></el-divider>
    <el-button v-on:click="handleCreateReportGroup"
    >创建报告组</el-button>
    <el-button
        v-on:click="dialogVisible = true">加入报告组</el-button>
    <div>
      <el-tree
          v-bind:data="myReportGroupList"
          v-bind:props="treeProps"
          v-on:node-click="handleNodeClick"
      >
      </el-tree>
    </div>
    <edit-report-group ref="editReportGroup"
                       v-on:refreshList="handleInitialization"></edit-report-group>
    <join-report-group-dialog v-bind:dialog-visible="dialogVisible"
                              v-on:closeDialog="dialogVisible = false"
                              v-on:refreshList="handleInitialization"></join-report-group-dialog>
    <div>我创建的报告组</div>
    <report-group-display-card
        v-for="item in myReportGroupList"
        v-bind:report-group="item"
        key="item.id"
        v-on:editReportGroup="handleEditReportGroup(item)"
    ></report-group-display-card>
    <div>我加入的报告组</div>
  </div>

</template>

<script>

// TODO show all the tag groups joined by the user, exhibit the group name and user's role
// TODO need to differentiate between ordinary report groups and project-like groups

import reportGroupDisplayCard from "./reportGroupDisplayCard.vue";
import joinReportGroupDialog from './joinReportGroupDialog.vue';
import editReportGroup from "./editReportGroup.vue";

export default {
  name: "myReportGroup.vue",
  components: {
    'joinReportGroupDialog': joinReportGroupDialog,
    'editReportGroup': editReportGroup,
    'reportGroupDisplayCard': reportGroupDisplayCard,
  },
  data () {
    return {
      dialogVisible: false,
      editDialogVisible: false,
      selectedNode: null,
      treeProps: {
        value: 'id',
        label: 'name',
        children: 'member_node',
      },
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
    },
    handleEditReportGroup (reportGroupObject) {
      this.$refs.editReportGroup.handleEdit(reportGroupObject)
    },
    handleNodeClick(data) {
      console.log(data);
      this.selectedNode = data;
    },
  }

}
</script>

<style scoped>
</style>
