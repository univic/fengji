<template>

  <el-card
    style="width: 50%"
  >
    <template #header>工作记录</template>
    <basic-item
      v-for="item in recordItemList"
      :key="item.titleText"
      :item="item"
      v-on:removeItem="handleRemoveItem(item.uuid)"
      v-on:showDetailDialog="openDetailDialog(item)"
    ></basic-item>

    <new-item
      v-on:add-item="addItem"
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
  import axios from "axios";
  import basicItem from "./basicItem.vue"
  import newItem from "./newItem.vue"
  import uuid from '../utilities/uuid.js'
  import tagDetailedDialog from "./tagDetailedDialog.vue";
  import { ElMessage } from "element-plus"
  import api from "../api";

export default {
  name: "recordItemList",
  components: {
    newItem,
    basicItem,
    tagDetailedDialog,
  },
  data () {
    return {
      recordItemList: [{
        titleText: "A",
        uuid: uuid()
        }],
      showDetailDialog: false,
      selectedTagItem: null,
    }
  },
  created() {
    console.log(this.$store.state.user.userIdentity)
  },
  computed: {

  },
  methods: {
    addItem(newItemText) {
      let dataObj = newItemText
      api.itemAPI.addRecordItem(
          dataObj
      ).then(
          (response) => {
            if (response.data.status === 'success') {
              this.recordItemList.push(
                  {
                    titleText: newItemText,
                    uuid: response.data.uuid
                  }
              )
            } else if (response.data.status === 'error') {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              })
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              })
            }
          }
      ).catch(
          function (error) {
            ElMessage({
              message: '出现了问题（*゜ー゜*）' + error.message,
              type: 'error'
            })
          }
      )

    },
    handleRemoveItem(itemUUID) {
      this.recordItemList.forEach(function (item, index, arr) {
        if (item.uuid === itemUUID) {
          arr.splice(index, 1)
        }
      })
    },
    openDetailDialog(item) {
      this.showDetailDialog = true
      this.selectedTagItem = item
    },
    getRecordItems() {

    }
  }
}
</script>

<style scoped>

</style>
