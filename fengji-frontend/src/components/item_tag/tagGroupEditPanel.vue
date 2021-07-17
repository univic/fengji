<template>
  <div>
    <el-dialog v-bind:title="dialogTitle"
               v-model="dialogVisible"
               v-bind:beforeClose="handleClose">
      <el-form v-bind:model="postForm"
               status-icon
               v-bind:rules="formRules"
               ref="tagGroupForm">
        <el-form-item label="标签组名称"
                      prop="tag_group_name">
          <el-input v-model="postForm.tag_group_name"
                    maxlength="10"
                    show-word-limit></el-input>
        </el-form-item>
        <el-form-item label="标签组颜色"
                      prop="tag_group_color">
          <el-color-picker v-model="postForm.tag_group_color"></el-color-picker>
        </el-form-item>
        <el-form-item>
          <el-button type="primary"
                     v-on:click="handleSubmit">提交</el-button>
          <el-button v-on:click="resetForm('tagGroupForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import qs from 'qs';
import api from '../../api';
import { ElMessage } from 'element-plus';

export default {
  name: "tagGroupEditPanel",
  props: [
    'dialogVisible'
  ],
  emits: [
    'closeDialog',
    'refreshTagList'
  ],
  data () {
    let validators = {
      validateTagGroupNameUnique: (rule, value, callback) => {
        api.tagGroup.getTagGroup({
          type: 'check_existence',
          tag_group_name: value
        }).then(
          function (response) {
            if (response.data.status === 'success') {
              callback()
            } else if (response.data.status === 'error') {
              callback(new Error(response.data.messages[0]))
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）',
                type: 'error',
              })
            }
          }
        )
      }
    }
    return {
      dialogMode: null,
      dialogTitle: '创建标签',
      postForm: {
        id: null,
        tag_group_name: null,
        tag_group_color: '#FFFFFF'
      },
      formRules: {
        tag_group_name: [
          { required: true, message: '请输入标签组名', trigger: 'blur' },
          { min: 2, max: 10, message: '标签组名的长度应为2~10个字符', trigger: 'blur' },
          { validator: validators.validateTagGroupNameUnique, trigger: 'blur' },
        ]
      }
    }
  },
  methods: {
    handleCreate () {
      // handle the create call, prepare the dialog title
      this.dialogTitle = "创建标签组";
      this.dialogMode = 'create';
    },
    handleEdit (row) {
      // update the tagForm, so each fields will have corresponding default value
      for (let k in row) {
        if (row.hasOwnProperty(k)) {
          this.tagForm[k] = row[k];
        }
      }
      this.dialogTitle = "编辑标签组 - " + this.tagForm.tag_name;
      this.dialogMode = 'modify';
    },
    handleSubmit () {
      this.$refs.tagGroupForm.validate((valid) => {
        if (valid) {
          this.submitTagGroup()
        }
      })
    },
    submitTagGroup () {
      let dataObj = qs.stringify(this.postForm);
      let cAPI = api.tagGroup.addNewTagGroup;
      if (this.dialogMode === 'modify') {
        cAPI = api.tagGroup.editTagGroup;
      }
      cAPI(dataObj).then((response) => {
        if (response.data.status === 'success') {
          this.handleClose();
          this.resetForm('tagGroupForm');
          ElMessage({
            message: response.data.messages[0],
            type: 'success'
          });
          this.$emit('refreshTagList')
        } else {
          ElMessage({
            message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
            type: 'error'
          });
        }
      })
    },
    handleClose () {
      this.$emit('closeDialog');
    },
    resetForm (formName) {
      this.$refs[formName].resetFields();
    },
  }

};
</script>

<style scoped></style>
