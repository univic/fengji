<template>

  <el-card
    style="width: 50%"
  >
    <template #header>
      <slot></slot>
    </template>
    <todo-item
      v-for="item in myTodoItemList"
      :key="item.id"
      :item="item"
      v-on:removeItem="handleRemoveItem(item)"
      v-on:showDetailDialog="openDetailDialog(item)"
    ></todo-item>

    <new-todo-item
      ref="newItemInput"
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
import message from "../../utilities/message";
import api from "../../api";

export default {
  name: "todoItemList",
  props: [
    'workMode',
    'requiredTags',
    'tagTemplates',
  ],
  emits: [],
  components: {
    newTodoItem,
    todoItem,
    tagDetailedDialog,
  },
  data() {
    return {
      showDetailDialog: false,
      selectedTagItem: null,
      tagGroupList: [],
      tagTemplateList: [],
      convertedTagTemplateList: [],
    };
  },

  created() {

  },
  computed: {
    groupedTagTemplateList() {
      return this.$store.getters['tagTemplate/getTagTemplateList'];
    },
    myTodoItemList() {
      return this.$store.state.todoItem.myTodoItemList;
    }
  },
  methods: {

    handleInitialization() {

    },

    addItem(newItem) {
      // a simple walk around to solve the "this" pointing problem inside axios
      // binding the right "this" pointer to "that", to avoid "this" pointing all over the place
      //   let that = this
      //   let dataObj = newItem
      //   api.todoItem.addTodoItem(
      //       dataObj
      //   ).then(
      //       (response) => {
      //         if (response.data.status === 'success') {
      //           // if new item is saved successfully, push it to the item list directly to avoid additional request
      //           this.recordItemList.push(
      //               {
      //                 // unpack the newItem dict, get titleText and TagList
      //                 ...newItem,
      //                 id: response.data.id
      //               }
      //           )
      //         } else if (response.data.status === 'error') {
      //           ElMessage({
      //             message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
      //             type: 'error'
      //           })
      //           that.triggerRollback();
      //         } else {
      //           ElMessage({
      //             message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
      //             type: 'error'
      //           })
      //           that.triggerRollback();
      //         }
      //       }
      //   ).catch(
      //       function (error) {
      //         ElMessage({
      //           message: '出现了问题（*゜ー゜*）' + error.message,
      //           type: 'error'
      //         })
      //         that.triggerRollback();
      //       }
      //   )
    },

    triggerRollback() {
      this.$refs.newItemInput.rollBack();
    },
    openDetailDialog(item) {
      this.showDetailDialog = true;
      this.selectedTagItem = item;
    },
    handleRemoveItem(item) {
      this.$confirm(
        '将删除该条目，是否继续', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
        this.removeItem(item);
      }).catch(() => {
        this.$message({
          message: '已取消删除',
          type: 'info'
        });
      });
    },
    removeItem(item) {
      api.todoItem.deleteTodoItem({
        id: item.id
      }).then((response) => {
          if (response.data.status === 'success') {
            this.$store.commit('todoItem/removeTodoItem', item)
            message.emitSuccessMessage(response.data.messages[0]);
          }
        }
      );
    },
  }
};
</script>

<style scoped>

</style>
