<template>

  <el-card
    style="width: 50%"
  >
    <template #header><slot></slot></template>
    <todo-item
      v-for="item in recordItemList"
      :key="item.id"
      :item="item"
      v-on:removeItem="handleRemoveItem(item)"
      v-on:showDetailDialog="openDetailDialog(item)"
    ></todo-item>

    <new-todo-item
      ref="newItemInput"
      v-on:add-item="addItem"
      :required-tags="requiredTags"
    ></new-todo-item>
  </el-card>
  <el-dialog
    v-model="showDetailDialog"
  >
    <tag-detailed-dialog
      v-bind:tagItem="selectedTagItem"
    ></tag-detailed-dialog>
  </el-dialog>


</template>

<script>
  import todoItem from "./todoItem.vue";
  import newTodoItem from "./newTodoItem.vue";
  import tagDetailedDialog from "../tagDetailedDialog.vue";
  import { ElMessage } from "element-plus";
  import api from "../../api";

export default {
  name: "todoItemList",
  props: [
    'workMode',
    'requiredTags',
    'tagTemplates',
  ],
  emits: [

  ],
  components: {
    newTodoItem,
    todoItem,
    tagDetailedDialog,
  },
  data () {
    return {
      recordItemList: [],
      showDetailDialog: false,
      selectedTagItem: null,
      tagGroupList: [],
      tagTemplateList: [],
      convertedTagTemplateList: [],
    };
  },

  created() {
    this.getRecordItems()
    this.getTagTemplateData()

  },
  computed: {
    groupedTagTemplateList () {
      return this.$store.getters['tagTemplate/getTagTemplateList']
    },
  },
  methods: {
    // use a promise to send async request
    getTagTemplateData () {
      let p1 = new Promise(this.getTagGroupList)
      let p2 = new Promise(this.getTagTemplateList)
      Promise.all([p1, p2]).then(() => {
        this.assignTagTemplateToTagGroup();
        this.$store.commit('tagTemplate/setTagTemplateList', this.tagGroupList);
        this.convertTagTemplateList();
      }).catch((result) => {
        ElMessage({
          message: result,
          type: "error",
        })
      })
    },
    getTagGroupList (resolve, reject) {
      api.tagGroup.getTagGroup({
        type: 'all',
      }).then((response) => {
        if (response.data.status === "success") {
          this.tagGroupList = response.data.tag_group_list;
          resolve('success');
        } else {
          reject("出现了问题（*゜ー゜*）" + response.data.messages[0]);
        }
      })
    },
    getTagTemplateList (resolve, reject) {
      api.tag.getTagTemplate({
        type: "all",
      }).then((response) => {
        if (response.data.status === "success") {
          this.tagTemplateList = response.data.tag_template_list;
          resolve('success');
        } else {
          reject("出现了问题（*゜ー゜*）" + response.data.messages[0]);
        }
      });
    },
    assignTagTemplateToTagGroup () {
      this.tagGroupList.forEach((tagGroupElement, index) => {
        this.tagGroupList[index].tag_template_list = this.filterTagTemplate(tagGroupElement.id, this.tagTemplateList)
      });
    },
    filterTagTemplate (tagGroupID, tagTemplateList) {
      let filteredList = tagTemplateList.filter((item) => {
        return item.tag_group_assignment.id === tagGroupID
      })
      return filteredList
    },
    convertTagTemplateList () {
      let rawList = this.groupedTagTemplateList;
      let convertedList = [];
      if (rawList.length > 0 ) {
        rawList.forEach((element, index) => {
          let convertedDict = {
            label: element.tag_group_name,
            children: [],
          }
          if (element.tag_template_list && element.tag_template_list.length > 0) {
            element.tag_template_list.forEach((item, index) => {
              let convertedItem = {
                label: item.tag_template_name,
                value: item.id
              }
              console.log(convertedItem)
              convertedDict.children.push(convertedItem)
            })
          } else {

          }
          convertedList.push(convertedDict)
        });
      } else {

      }

      this.$store.commit('tagTemplate/setConvertedTagTemplateList', convertedList);
    },

    addItem(newItem) {
      // a simple walk around to solve the "this" pointing problem inside axios
      // binding the right "this" pointer to "that", to avoid "this" pointing all over the place
      let that = this
      let dataObj = newItem
      api.todoItem.addTodoItem(
          dataObj
      ).then(
          (response) => {
            if (response.data.status === 'success') {
              // if new item is saved successfully, push it to the item list directly to avoid additional request
              this.recordItemList.push(
                  {
                    // unpack the newItem dict, get titleText and TagList
                    ...newItem,
                    id: response.data.id
                  }
              )
            } else if (response.data.status === 'error') {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              })
              that.triggerRollback();
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              })
              that.triggerRollback();
            }
          }
      ).catch(
          function (error) {
            ElMessage({
              message: '出现了问题（*゜ー゜*）' + error.message,
              type: 'error'
            })
            that.triggerRollback();
          }
      )
    },
    triggerRollback() {
      this.$refs.newItemInput.rollBack();
    },
    openDetailDialog(item) {
      this.showDetailDialog = true
      this.selectedTagItem = item
    },
    getRecordItems() {
      //TODO: gei all the items when created
      api.todoItem.getTodoItem({
        type: 'my'
      }).then((response) => {
        console.log(response.data)
        this.recordItemList = response.data.todo_item_list
      }
      )
    },
    handleRemoveItem(item) {
      this.$confirm(
          '将删除该条目，是否继续', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
        this.removeItem(item)
      }).catch(()=> {
        this.$message({
          message: '已取消删除',
          type: 'info'
        })
      })
    },
    removeItem(item) {
      api.todoItem.deleteTodoItem({
        id: item.id
      }).then(
          (response) => {
            if (response.data.status === 'success') {
              this.recordItemList.forEach(function (iterItem, iterIndex, IterArr) {
                if (iterItem.id === item.id) {
                  IterArr.splice(iterIndex, 1)
                }
              })
              ElMessage({
                message: response.data.messages[0],
                type: 'success'
              });
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              });
            }
          }
      )
    },
  }
}
</script>

<style scoped>

</style>
