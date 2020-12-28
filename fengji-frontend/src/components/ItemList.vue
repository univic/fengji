<template>
<el-row>
  <el-col>
    <span
      class="el-icon-plus"
      v-if="!newItemFocused"
    ></span>
    <el-checkbox
      v-else
    ></el-checkbox>
  </el-col>
  <el-col>
    <el-input
        v-on:click="newItemFocused=!newItemFocused"
    >
    </el-input>
  </el-col>

</el-row>

</template>

<script>
export default {
  name: "ItemList",
  data () {
    return {
      newItemFocused: true,

      exampleData: [{
          name: "A"
        },
        {
          name: "B"
        }
      ]
    }
  },
  computed: {

  },
  methods: {
  }
}
</script>

<style scoped>

</style>
