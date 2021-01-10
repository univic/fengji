<template>

<BasicItem></BasicItem>

<el-row
  type="flex"
  align="middle"
>
  <el-col
    :span="8"
  >
    <el-card
      v-on:mouseover="newItemHighLighted=true"
      v-on:mouseout="newItemHighLighted = newItemFocused ? true : false"
    >
      <div>
        <span
          class="el-icon-plus"
          v-if="!newItemFocused"
          style="width: 10%"
        ></span>
        <span
          class="el-icon-circle-plus"
          v-else
          style="width: 10%"
        ></span>
        <el-input
          v-model="newRecordItemText"
          v-on:keypress.enter="addRecordItem"
          v-on:focus="newItemFocused=true"
          v-on:blur="newItemFocused=false"
          style="width: 80%"
          type="flex"
          align="right"
        >
        </el-input>
      </div>
    </el-card>

  </el-col>

</el-row>

</template>

<script>
  import BasicItem from "./BasicItem.vue"

export default {
  name: "ItemList",
  components: {BasicItem},
  data () {
    return {
      newItemHighLighted: false,
      newItemFocused: false,
      newRecordItemText: null,

      recordItemList: [{
          name: "A"
        }
      ]
    }
  },
  computed: {

  },
  methods: {
    addRecordItem: function () {
      this.recordItemList.push(this.newRecordItemText)

    }
  }
}
</script>

<style scoped>

</style>
