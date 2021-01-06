<template>
  <el-row>
    <el-col
      :span="8"
    >
      <el-card>
          <div>
            <span>待办事项</span>
          </div>
      </el-card>
    </el-col>
  </el-row>
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
export default {
  name: "ItemList",
  data () {
    return {
      newItemHighLighted: false,
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
