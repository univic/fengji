<template>
  <el-tag
    v-on:click="handleTagSelect"
    v-bind:disabled="disabled"
  >
    {{ tagTemplate.name }}
  </el-tag>
</template>

<script>
export default {
  name: "selectableTag",
  props: {
    'tagTemplate': {

    },
    'disabled': {
      type: Boolean,
      default: false,
    },

  },
  emits: [
    'selectTag'
  ],
  methods: {
    handleTagSelect() {
      if (!this.disabled) {
        this.$emit('selectTag')
      }
    }
  }
};
</script>

<style scoped>

</style>