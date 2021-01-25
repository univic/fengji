<template>

  <el-card
    style="width: 50%"
  >
    <template #header>工作记录</template>
    <basic-item
      v-for="item in recordItemList"
      :key="item.titleText"
      :item="item"
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
  name: "ItemList",
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

    }
  }
}
</script>

<style scoped>

</style>
