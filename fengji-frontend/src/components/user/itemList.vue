<template>

  <el-card
    style="width: 50%"
  >
    <template #header><slot></slot></template>
    <basic-item
      v-for="item in recordItemList"
      :key="item.item_title"
      :item="item"
      v-on:removeItem="handleRemoveItem(item)"
      v-on:showDetailDialog="openDetailDialog(item)"
    ></basic-item>

    <new-item
      ref="newItemInput"
      v-on:add-item="addItem"
      :required-tags="requiredTags"
    ></new-item>
  </el-card>
  <el-dialog
    v-model="showDetailDialog"
  >
    <tag-detailed-dialog
      v-bind:tagItem="selectedTagItem"
    ></tag-detailed-dialog>
  </el-dialog>


</template>

<script>
  import basicItem from "./basicItem.vue";
  import newItem from "./newItem.vue";
  import tagDetailedDialog from "../tagDetailedDialog.vue";
  import { ElMessage } from "element-plus";
  import api from "../../api";

export default {
  name: "recordItemList",
  props: [
    'workMode',
    'requiredTags',
    'tagTemplates',
  ],
  emits: [

  ],
  components: {
    newItem,
    basicItem,
    tagDetailedDialog,
  },
  data () {
    return {
      recordItemList: [],
      showDetailDialog: false,
      selectedTagItem: null,
    };
  },

  created() {
    this.getRecordItems()
  },
  computed: {

  },
  methods: {
    addItem(newItem) {
      // a simple walk around to solve the "this" pointing problem inside axios
      // binding the right "this" pointer to "that", to avoid "this" pointing all over the place
      let that = this
      let dataObj = newItem
      console.log(dataObj)
      api.itemAPI.addRecordItem(
          dataObj
      ).then(
          (response) => {
            if (response.data.status === 'success') {
              // if new item is saved successfully, push it to the item list directly to avoid additional request
              this.recordItemList.push(
                  {
                    // unpack the newItem dict, get titleText and TagList
                    ...newItem,
                    id: response.data.id
                  }
              )
            } else if (response.data.status === 'error') {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              })
              that.triggerRollback();
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              })
              that.triggerRollback();
            }
          }
      ).catch(
          function (error) {
            ElMessage({
              message: '出现了问题（*゜ー゜*）' + error.message,
              type: 'error'
            })
            that.triggerRollback();
          }
      )
    },
    triggerRollback() {
      this.$refs.newItemInput.rollBack();
    },
    openDetailDialog(item) {
      this.showDetailDialog = true
      this.selectedTagItem = item
    },
    getRecordItems() {
      //TODO: gei all the items when created
      api.itemAPI.getRecordItem({
        type: 'all'
      }).then((response) => {
        console.log(response.data)
        this.recordItemList = response.data.record_item_list
      }
      )
    },
    handleRemoveItem(item) {
      this.$confirm(
          '将删除该条目，是否继续', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
        this.removeItem(item)
      }).catch(()=> {
        this.$message({
          message: '已取消删除',
          type: 'info'
        })
      })
    },
    removeItem(item) {
      api.itemAPI.deleteRecordItem({
        id: item.id
      }).then(
          (response) => {
            if (response.data.status === 'success') {
              this.recordItemList.forEach(function (iterItem, iterIndex, IterArr) {
                if (iterItem.id === item.id) {
                  IterArr.splice(iterIndex, 1)
                }
              })
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
