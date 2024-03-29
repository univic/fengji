<template>
  <div>
    <el-dialog v-bind:title="dialogTitle"
               v-bind:model-value="dialogVisible"
               v-bind:beforeClose="handleClose">
      <el-form v-bind:model="postForm"
               status-icon
               v-bind:rules="formRules"
               ref="tagGroupForm">
        <el-form-item label="标签组名称"
                      prop="name">
          <el-input v-model="postForm.name"
                    maxlength="10"
                    show-word-limit></el-input>
        </el-form-item>
        <el-form-item label="隶属标签组"
                      prop="parent_group">
          <el-cascader v-model="postForm.parent_group"
                       placeholder="请选择归属标签组"
                       v-bind:options="tagTemplateGroup"
                       v-bind:props="tagGroupCascaderProps"
          ></el-cascader>
        </el-form-item>
        <el-form-item label="标签组颜色"
                      prop="color">
          <el-color-picker v-model="postForm.color"></el-color-picker>
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
    'refreshTagGroupList'
  ],
  data () {
    let validators = {
      validateTagGroupNameUnique: (rule, value, callback) => {
        api.tagTemplateGroup.getTagTemplateGroup({
          type: 'check_existence',
          name: value
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
        name: null,
        color: '#FFFFFF',
        parent_group: null,
      },
      formRules: {
        name: [
          { required: true, message: '请输入标签组名', trigger: 'blur' },
          { min: 2, max: 10, message: '标签组名的长度应为2~10个字符', trigger: 'blur' },
          { validator: validators.validateTagGroupNameUnique, trigger: 'blur' },
        ]
      },
      tagGroupCascaderProps: {
        checkStrictly: true,        // can select parent nodes
        emitPath: false,            // return selected node only
        value: 'id',
        label: 'name',
        children: 'child_group',
      }
    }
  },
  computed: {
    tagTemplateGroup() {
      return this.$store.getters['tagTemplateGroup/getTagTemplateGroupList']
    }
  },
  methods: {
    handleCreate () {
      // handle the create call, prepare the dialog title
      this.dialogTitle = "创建标签组";
      this.dialogMode = 'create';
    },
    handleEdit (tagGroupElement) {
      // update the tagForm, so each fields will have corresponding default value
      for (let item in tagGroupElement) {
        if (Object.prototype.hasOwnProperty.call(this.postForm, item)) {
          this.postForm[item] = tagGroupElement[item];
        }
      }
      this.dialogTitle = "编辑标签组 - " + this.postForm.name;
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
      let cAPI = api.tagTemplateGroup.addNewTagTemplateGroup;
      if (this.dialogMode === 'modify') {
        cAPI = api.tagTemplateGroup.editTagTemplateGroup;
      }
      cAPI(dataObj).then((response) => {
        if (response.data.status === 'success') {
          this.handleClose();
          this.resetForm('tagGroupForm');
          this.$emit('refreshTagGroupList')
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
