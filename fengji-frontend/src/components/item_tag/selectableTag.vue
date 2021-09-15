<template>
  <el-tag
    v-on:click="handleTagSelect"
    v-bind:type="disabledType"
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
  computed: {
    disabledType () {
      // if tag is disabled, use info type
      return (this.disabled ? 'info' : '');
    }
  },
  methods: {
    handleTagSelect() {
      // if tag is disabled, prohibit event emit
      if (!this.disabled) {
        this.$emit('selectTag');
      }
    }
  }
}
</script>

<style scoped>

</style>