<template>
<el-row
  type="flex"
  align="middle"
>
  <el-col
    :span="1"
  >
    <span
      class="el-icon-plus"
      v-if="!newItemFocused"
    ></span>
    <span
      class="el-icon-circle-plus"
      v-else
    ></span>
  </el-col>
  <el-col
    :span="4"
  >
    <el-input
      v-on:focus="newItemFocused=!newItemFocused"
      v-on:blur="newItemFocused=!newItemFocused"
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
      newItemFocused: false,

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
