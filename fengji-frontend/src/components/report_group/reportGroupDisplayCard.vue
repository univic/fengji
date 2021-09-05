<template>
  <div>
    <el-card>
      <template #header>
        <div>
          <span> {{reportGroup.name}} </span>
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
  name: "reportGroupDisplayCard",
  props: [
    'reportGroup'
  ],
  methods: {
    handleEdit() {

    },
    handleDelete() {

    }
  }
};
</script>

<style scoped>

</style>