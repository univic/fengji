<template>
  <div class="card">
    <el-card>
      <template #header>
        <div>
          <span> {{reportGroup.name}} </span>
          <el-button v-on:click="handleEdit"
                     icon="el-icon-edit"
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
  emits:[
      'editReportGroup'
  ],
  methods: {
    handleEdit() {
      this.$emit('editReportGroup')
    },
    handleDelete() {

    }
  }
};
</script>

<style scoped>

.card{
  height: 200px;
  width: 260px;
}

</style>