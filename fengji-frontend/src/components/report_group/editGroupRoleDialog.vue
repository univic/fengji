<template>

  <!--  quick nav buttons-->
  <div>
    <el-dialog
        :title="dialogTitle"
        v-model="dialogVisible"
        :before-close="handleClose"
    >
      <el-form
          :model="formData"
          status-icon
          :rules="formRules"
          ref="groupRoleForm"
      >
        <el-form-item label="角色名称" prop="role_name">
          <el-input
              v-model="formData.role_name"
              maxlength="8"
              show-word-limit
          ></el-input>
        </el-form-item>
        <el-form-item
            label="角色缩写"
            prop="role_abbr"
        >
          <el-input v-model="formData.role_abbr"></el-input>
        </el-form-item>
        <el-form-item
            label="角色描述"
            prop="role_description"
        >
          <el-input v-model="formData.role_description"></el-input>
        </el-form-item>
        <el-form-item label="角色颜色"  prop="role_color">
          <el-color-picker v-model="formData.role_color"></el-color-picker>
        </el-form-item>
        <el-form-item>
          <el-button
              type="primary"
              v-on:click="handleSubmit"
          >提交</el-button>
          <el-button
              v-on:click="resetForm('tagForm')"
          >重置</el-button>
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
  name: "editGroupRoleDialog",
  props: [
    'dialogVisible',
  ],
  emits: [
    'closeDialog',
    'refreshList'
  ],
  data () {
    let validators = {
      validateRoleNameUnique: (rule, value, callback) => {
        // use a customized find function to see if the tag name has already existed
        // only do the unique check if dialogMode is not 'modify'
        if (this.dialogMode !== 'modify') {
          api.groupMemberRole.getRole({
            type: 'check_existence',
            role_name: value,
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
        } else {
          callback()
        }
      },
    }
    return {
      dialogTitle: '创建报告组角色',
      dialogMode: null,
      loadingAnimation: false,
      formData: {
        id: null,
        role_name: null,
        role_abbr: null,
        role_color: '#FFFFFF',
      },
      formRules: {
        role_name: [
          {required: true, message: '请输入角色缩写', trigger: 'blur'},
          {min: 2, max: 10, message: '标签名的长度应为2~10个字符', trigger: 'blur'},
          {validator: validators.validateRoleNameUnique, trigger: 'blur'}
        ],
        role_abbr: [
          {required: true, message: '请输入角色缩写'},
          {min: 2, max: 5, message: '角色缩写的长度应为2~5个字符', trigger: 'blur'},
        ],
        role_description: [
          {max: 20, message: '角色缩写的长度应不超过20个字符', trigger: 'blur'},
        ]
      },
    };
  },
  computed: {
  },
  methods: {
    handleClose() {
      this.$emit('closeDialog')
    },
    handleSubmit() {
      this.$refs.groupRoleForm.validate((valid) => {
        if (valid) {
          this.submitNewRole()
        }
      })
    },
    submitNewRole() {
      let dataObj = qs.stringify(this.formData);
      let cAPI = api.groupMemberRole.addNewRole;
      if (this.dialogMode === 'modify') {
        cAPI = api.groupMemberRole.editRole
      }
      cAPI(dataObj).then((response) => {
            if (response.data.status === 'success') {
              this.handleClose();
              this.resetForm('groupRoleForm');
              ElMessage({
                message: response.data.messages[0],
                type: 'success'
              });
              this.$emit('refreshList')
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              });
            }
          }
      )
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    handleEdit(row) {
      // update the tagForm, so each fields will have corresponding default value
      for (let k in row) {
        if (row.hasOwnProperty(k)) {
          this.formData[k] = row[k]
        }
      }
      this.dialogTitle = "编辑报告组角色 - " + this.formData.role_name
      this.dialogMode = 'modify'
    },
    handleCreate() {
      // handle the create call, prepare the dialog title
      this.dialogTitle = "创建报告组角色"
      this.dialogMode = 'create'
    }
  }
}
</script>

<style scoped>

</style>
