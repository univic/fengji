<template>
  <el-popover
      trigger="manual"
      v-model:visible="popoverVisible"
  >
    <div>
      <div>
        <el-cascader v-model="reportGroupInput"
                     placeholder="请选择归属报告组"
                     v-bind:options="myReportGroupList"
                     v-bind:props="cascaderProps"
                     ref="cascader"
                     v-on:change="handleChange"
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
  props: [
      'predefinedReportGroup'
  ],
  data() {
    return {
      popoverVisible: false,
      reportGroupInput: null,
      selectedReportGroupNode: null,
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
    // selectedReportGroup: {
    //   deep: true,
    //   handler(newValue, oldValue) {
    //     this.$emit('selectReportGroup', this.selectedReportGroup);
    //   }
    // }
  },
  computed: {
    myReportGroupList() {
      return this.$store.state.reportGroup.myReportGroupList;
    },
    selectedReportGroup() {
      if(this.reportGroupInput === null && this.predefinedReportGroup) {
        return this.predefinedReportGroup.id
      } else {
        return this.reportGroupInput
      }
    },
    selectedReportGroupText() {
      // determine the tag display text, according to the length of the report group name
      // and the number of selected report group
      let text = "无";
      let firstReportGroupName = null;
      let maxStrLength = 8;
      if (this.selectedReportGroupNode) {
        // use recursive search to find the name of the selected report group with the GUID
        // let treeSearchResult = treeTool.treeSearch(this.myReportGroupList, 'member_node', 'id', this.selectedReportGroup)
        // console.log(treeSearchResult)
          firstReportGroupName = this.selectedReportGroupNode.name;

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
      this.reportGroupInput = null
    },
    handleChange() {
      this.selectedReportGroupNode = this.$refs.cascader.getCheckedNodes()
    }
  }
};
</script>

<style scoped>

</style>