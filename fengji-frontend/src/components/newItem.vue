<template>

    <div
      v-on:mouseover="newItemHighLighted=true"
      v-on:mouseout="newItemHighLighted = newItemFocused ? true : false"
    >
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
          v-model="newItemText"
          v-on:keypress.enter="addRecordItem"
          v-on:focus="newItemFocused=true"
          v-on:blur="newItemFocused=false"
          style="width: 80%"
          type="flex"
          align="right"
      >
      </el-input>
    </div>

</template>

<script>

export default {
  name: "newItem",
  props: [],
  emits: [
    'addItem'
  ],
  data () {
    return {
      newItemHighLighted: false,
      newItemFocused: false,
      newItemText: null,

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
      this.$emit('addItem', this.newItemText)
      this.recordItemList.push(this.newItemText)
      this.newItemText = null
    }
  }
}
</script>

<style scoped>

</style>
