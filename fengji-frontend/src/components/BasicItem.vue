<template>
  <el-row
  >
    <el-col
        :span="8"
    >
      <el-card>
        <template #default>
          <div>
            <span> Title </span>
          </div>
          <div>
            <div>
              <el-divider>标签</el-divider>
              <div>
                <el-tag
                  v-for="tag in itemTags"
                  :key="tag.name"
                  closable
                >
                  {{ tag.name }}
                </el-tag>
                <el-input
                  v-if="tagInputVisible"
                  v-model="tagInputValue"
                  ref="saveTagInput"
                  @keyup.enter.native="handleInputConfirm"
                  @blur="handleInputConfirm"
                >
                </el-input>
                <el-button
                  v-else
                  @click="showTagInput"
                >
                  + 新标签
                </el-button>
                <el-button
                  v-on:click="tagDialogVisible = true"
                >更多 >></el-button>
              </div>
            </div>
            <el-dialog
              title="编辑标签"
              v-model="tagDialogVisible"
            >
              <div>
                <el-divider>标签属性</el-divider>
                <div></div>
              </div>
            </el-dialog>

          </div>
        </template>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: "BasicItem",
  data () {
    return {
      itemTags: [
        {name: '标签1'},
        {name: '标签2'},
      ],
      tagInputVisible: false,
      tagInputValue: null,
      tagDialogVisible: false,

    }
  },
  computed: {

  },
  methods: {
    handleClose() {

    },
    showTagInput() {
      this.tagInputValue = true
    },
    handleInputConfirm() {

    }
  }
}
</script>

<style scoped>

</style>
