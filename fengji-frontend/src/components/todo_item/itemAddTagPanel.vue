<template>
  <el-popover
      trigger="manual"
      v-model:visible="popoverVisible"
  >
    <div>
      <div>
        <el-cascader
            ref="cascader"
            v-bind:options="tagTemplateGroupList"
            v-bind:props="cascaderProps"
            v-on:change="handleNodeClick"
            clearable
        ></el-cascader>
        <div>
          <el-button
              type="primary"
          >确定
          </el-button>
          <el-button
              type="info"
              v-on:click="handleClosePopover"
          >取消
          </el-button>
        </div>

      </div>
      <div>
        <el-card v-if="selectedTagTemplateGroup">
          <el-tag v-for="item in selectedTagTemplateGroup.data.tag_template_list"
                  key="item.id"
          >{{ item.name }}</el-tag>
        </el-card>

      </div>


    </div>
    <template #reference>
      <slot></slot>
    </template>

  </el-popover>

</template>

<script>

export default {
  name: "itemAddTagPanel",
  components: {},
  props: [
    'popoverVisible'
  ],
  emits: [
    'closePopover'
  ],
  data() {
    return {
      showAddTagSelector: false,
      selectedTagTemplateGroupID: null,
      selectedTagTemplateGroup: null,
      selectedTags: [],
      cascaderProps: {
        checkStrictly: true,      // can select parent nodes
        emitPath: false,            // return selected node only
        multiple: false,
        value: 'id',
        label: 'name',
        children: 'child_group',
      }
    };
  },
  computed: {
    tagTemplateGroupList() {
      return this.$store.getters['tagTemplateGroup/getTagTemplateGroupList'];
    },
  },
  methods: {
    handleClosePopover() {
      this.$emit('closePopover');
    },
    handleNodeClick(data) {
      this.selectedTagTemplateGroupID = data;
      this.selectedTagTemplateGroup = this.$refs.cascader.getCheckedNodes()[0];
    },
  }

};
</script>

<style scoped>

</style>