<template>
  <el-popover
      trigger="manual"
      v-model:visible="popoverVisible"
  >
    <div>
      <div>
        <el-cascader v-model="selectedReportGroup"
                     placeholder="请选择归属报告组"
                     v-bind:options="myReportGroupList"
                     v-bind:props="cascaderProps"
        >
        </el-cascader>
        <div>
          <el-button
              type="primary"
              v-on:click="handleConfirm"
          >确定
          </el-button>
          <el-button
              type="info"
              v-on:click="handleCancel"
          >取消
          </el-button>
        </div>

      </div>
    </div>
    <template #reference>
      <el-tag
          v-on:click="popoverVisible = !popoverVisible"
      >
        <slot></slot>
        报告组:{{ selectedReportGroupText }}

      </el-tag>
    </template>
  </el-popover>
</template>

<script>
import treeTool from "../../utilities/treeTool";

export default {
  name: "reportGroupTag",
  emits: [
    'selectReportGroup'
  ],
  data() {
    return {
      popoverVisible: false,
      selectedReportGroup: null,
      cascaderProps: {
        checkStrictly: true,      // can select parent nodes
        emitPath: false,            // return selected node only
        value: 'id',
        label: 'name',
        children: 'member_node',
      }
    };
  },
  watch: {
    selectedReportGroup: {
      deep: true,
      handler(newValue, oldValue) {
        this.$emit('selectReportGroup', this.selectedReportGroup);
      }
    }
  },
  computed: {
    myReportGroupList() {
      return this.$store.state.reportGroup.myReportGroupList;
    },
    selectedReportGroupText() {
      // determine the tag display text, according to the length of the report group name
      // and the number of selected report group
      let text = "无";
      let firstReportGroupName = null;
      let maxStrLength = 8;
      if (this.selectedReportGroup) {
        // use recursive search to find the name of the selected report group with the GUID
        let treeSearchResult = treeTool.treeSearch(this.myReportGroupList, 'member_node', 'id', this.selectedReportGroup)
        console.log(treeSearchResult);
        if (treeSearchResult && treeSearchResult.name) {
          firstReportGroupName = treeSearchResult.name;
        }

        // slice the report group name, if it is too long
        if (firstReportGroupName && firstReportGroupName.length > maxStrLength) {
          text = firstReportGroupName.slice(0, maxStrLength) + "...";
        } else {
          text = firstReportGroupName;
        }
        // if multiple report groups are selected, display total number
        // if (this.selectedReportGroup.length > 1) {
        //   text = text + " 等" + this.selectedReportGroup.length + "个";
        // }
      } else {
        text = "无";
      }
      return text;
      }

    },

  methods: {
    handleConfirm() {
      this.popoverVisible = false
    },
    handleCancel() {
      this.popoverVisible = false
      this.selectedReportGroup = null
    },
  }
};
</script>

<style scoped>

</style>