<template>

  <el-card
    style="width: 50%"
  >
    <template #header>工作记录</template>
    <basic-item
      v-for="item in recordItemList"
      :key="item.titleText"
      :item="item"
      v-on：removeItem="handleRemoveItem(item.uuid)"
    ></basic-item>

    <new-item
      v-on:add-item="addItem"
    ></new-item>
  </el-card>



</template>

<script>
  import basicItem from "./basicItem.vue"
  import newItem from "./newItem.vue"
  import uuid from '../utilities/uuid.js'

export default {
  name: "recordItemList",
  components: {
    newItem,
    basicItem,
  },
  data () {
    return {
      recordItemList: [{
        titleText: "A",
        uuid: uuid()
        }]
    }
  },
  computed: {

  },
  methods: {
    addItem(newItemText) {
      this.recordItemList.push(
          {
            titleText: newItemText,
            uuid: uuid()
          }
      )
    },
    handleRemoveItem(itemUUID) {
      this.recordItemList.forEach(function (item, index, arr) {
        if (item.uuid === itemUUID) {
          arr.splice(index, 1)
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
