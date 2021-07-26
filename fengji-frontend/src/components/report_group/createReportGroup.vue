

<template>
  <div>
    <el-dialog v-model="dialogVisible">
      <div>
        <el-page-header content="创建报告组"></el-page-header>
        <el-divider></el-divider>
        <el-form :model="reportGroupForm"
                 status-icon
                 ref="reportGroupForm"
                 :rules="formRules">
          <el-form-item label="报告组名称"
                        prop="group_name">
            <el-input v-model="reportGroupForm.group_name"></el-input>
          </el-form-item>
          <el-form-item label="这是一个项目吗？"
                        prop="is_project">
            <el-radio-group v-model="reportGroupForm.is_project">
              <el-radio-button label="true">是项目</el-radio-button>
              <el-radio-button label="false">不是项目</el-radio-button>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="加入方式"
                        prop="is_project">
            <el-radio-group v-model="reportGroupForm.is_open">
              <el-radio-button label="true">开放加入</el-radio-button>
              <el-radio-button label="false">邀请加入</el-radio-button>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="报告组颜色"
                        prop="group_color">
            <el-color-picker v-model="reportGroupForm.group_color"></el-color-picker>
          </el-form-item>
          <el-form-item>
            <el-button type="primary"
                       v-on:click="handleSubmit">提交</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import qs from 'qs';
import api from '../../api';
import { ElMessage } from 'element-plus';

export default {
  name: "editReportGroup.vue",
  emits: [
    'refreshList'
  ],
  data () {
    let validators = {
      validateGroupName: (rule, value, callback) => {
        api.reportGroup.getReportGroup({
          type: 'check_existence',
          group_name: value,
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
      },
    }
    return {
      dialogVisible: false,
      reportGroupForm: {
        id: null,
        group_name: null,
        is_project: false,
        is_open: false,
        group_color: '#FFFFFF',
      },
      formRules: {
        group_name: [
          { required: true, message: '请输入报告组名', trigger: 'blur' },
          { min: 3, max: 50, message: '报告组名的长度应为3~50个字符', trigger: 'blur' },
          { validator: validators.validateGroupName, trigger: 'blur' }
        ],
      }
    }
  },
  methods: {
    handleCreate () {
      this.dialogVisible = true
    },
    handleSubmit () {
      this.$refs.reportGroupForm.validate((valid) => {
        if (valid) {
          this.submitNewTag()
        }
      })
    },
    submitNewTag () {
      let dataObj = qs.stringify(this.reportGroupForm);
      api.reportGroup.addNewGroup(dataObj).then((response) => {
        if (response.data.status === 'success') {
          this.$refs.reportGroupForm.resetFields();
          this.dialogVisible = false;
          this.$emit('refreshList')
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
    }
  }
}
</script>

<style scoped>
</style>
