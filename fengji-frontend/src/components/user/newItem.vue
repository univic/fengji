<template>

  <!--  default tag-->
  <div>
    默认/必选标签
    <basic-tag
      v-for="(tag, index) in tagList"
      :key="tag.id"
      v-on:updateTagValue="updateTagValue(index, $event)"
    >
      {{ tag.tag_name }} : {{ tag.tag_value }}
    </basic-tag>
  </div>
<!--    main input area-->
    <div
      v-on:mouseover="newItemHighLighted=true"
      v-on:mouseout="newItemHighLighted = newItemFocused"
    >
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
          v-model="newItemText"
          v-on:keypress.enter="addRecordItem"
          v-on:focus="newItemFocused=true"
          v-on:blur="newItemFocused=false"
          style="width: 80%"
          type="flex"
          align="right"
      >
      </el-input>
    </div>

</template>

<script>
import basicTag from '../item_tag/basicTag.vue';

export default {
  name: "newItem",
  props: [
    'requiredTags'
  ],
  components: {
    basicTag
  },
  emits: [
    'addItem'
  ],
  data () {
    return {
      newItemHighLighted: false,
      newItemFocused: false,
      newItemText: null,
      rollBackText: null,
      tagList: [],
      // key name must align with backend
      newItem: {
        item_title: null,
        tag_list: null,
        report_group_list: null,
      },
    }
  },
  // the prop value of requiredTags is async assigned, so the value is assigned after the component is mounted
  // use deep watch to force the value get updated
  watch: {
    requiredTags: {
      deep:  true,
      handler(newValue, oldValue) {
        this.initializeTagList()
      }
    }
  },
  computed: {

  },
  mounted() {
    this.initializeTagList()
  },
  methods: {
    initializeTagList () {
      this.tagList = []
      this.requiredTags.forEach( (item) => {
        // use shallow copy, or the newTagItem will point to the same address as requiredTags
        // in that case the tagList will be initialized instantly after value change due to the watcher
        let newTagItem = {...item};
        newTagItem.tag_value = item.tag_default_value;
        this.tagList.push(newTagItem);
      })
    },
    addRecordItem () {
      this.rollBackText = this.newItemText;
      this.newItem.item_title = this.newItemText;
      this.newItem.tag_list = this.tagList;
      this.$emit('addItem', this.newItem);
      // this.recordItemList.push(this.newItem);
      this.newItemText = null;
    },
    rollBack: function () {
      this.newItemText = this.rollBackText;
    },
    updateTagValue: function (index, newTagValue) {
      this.tagList[index].tag_value = newTagValue
    }
  }
}
</script>

<style scoped>

</style>
