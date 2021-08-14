<template>
  <el-popover
    trigger="manual"
    v-model:visible="popoverVisible"
  >
    <div>
      <el-select
          v-model="selectedReportGroup"
          multiple
          placeholder="请选择报告组"
      >
        <el-option
          v-for="item in myReportGroup"
          v-bind:key="item.id"
          v-bind:label="item.name"
          v-bind:value="item.id"
        >

        </el-option>

      </el-select>
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
export default {
  name: "reportGroupTag",
  emits: [
    'selectReportGroup'
  ],
  data() {
    return {
      popoverVisible: false,
      selectedReportGroup: [],
    }
  },
  watch: {
    selectedReportGroup: {
      deep:  true,
      handler(newValue, oldValue) {
        this.$emit('selectReportGroup', this.selectedReportGroup)
      }
    }
  },
  computed: {
    myReportGroup() {
      return this.$store.state.user.myReportGroup
    },
    selectedReportGroupText() {
      // determine the tag display text, according to the length of the report group name
      // and the number of selected report group
      let text = "无";
      let firstReportGroupName = null;
      let maxStrLength = 8;
      if (this.selectedReportGroup.length > 0) {
        // find the name of the selected report group with the GUID
        this.myReportGroup.forEach((iterItem, iterIndex, IterArr) => {
          if (iterItem.id === this.selectedReportGroup[0]) {
            firstReportGroupName = iterItem.name
          }
        })
        // slice the report group name, if it is too long
        if (firstReportGroupName.length > maxStrLength) {
          text = firstReportGroupName.slice(0, maxStrLength) + "...";
        } else {
          text = firstReportGroupName;
        }
        // if multiple report groups are selected, display total number
        if (this.selectedReportGroup.length > 1) {
          text = text + " 等" + this.selectedReportGroup.length + "个";
        }

      }
      return text
    }
  }
}
</script>

<style scoped>

</style>