<template>

  <el-card>
    <template #header>工作记录</template>

    <new-item></new-item>
  </el-card>



</template>

<script>
  import BasicItem from "./BasicItem.vue"
  import newItem from "./newItem.vue"

export default {
  name: "ItemList",
  components: {
    newItem,
    BasicItem,
  },
  data () {
    return {

      recordItemList: [{
          name: "A"
        }]
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
