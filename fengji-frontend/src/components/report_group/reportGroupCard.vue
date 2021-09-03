<template>
  <div>
    <el-card v-for="item in myReportGroupList">
      <template #header>
        <div>
          <span> {{item.name}} </span>
          <el-button v-on:click="handleEdit"
                     icon="el-icon-edit"
                     circle></el-button>
          <el-button v-on:click="handleDelete"
                     icon="el-icon-delete"
                     circle></el-button>
        </div>
      </template>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "reportGroupCard"
};
</script>

<style scoped>

</style>