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
          v-model="newRecordItemText"
          v-on:keypress.enter="$emit"
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
