

<template>
  <div>
    <el-dialog v-model="dialogVisible">
      <div>
        <el-page-header :content="dialogTitle"></el-page-header>
        <el-divider></el-divider>
        <el-form :model="reportGroupForm"
                 status-icon
                 ref="reportGroupForm"
                 :rules="formRules">
          <el-form-item label="报告组名称"
                        prop="name">
            <el-input v-model="reportGroupForm.name"></el-input>
          </el-form-item>
          <el-form-item label="归属报告组"
                        prop="tag_group_assignment">
            <el-cascader v-model="reportGroupForm.tag_group_assignment"
                         placeholder="请选择归属报告组"
                         v-bind:options="cascaderOptions"
                         v-bind:props="cascaderProps"
            >
            </el-cascader>
          </el-form-item>
          <el-form-item label="加入方式"
                        prop="open_join"
          >
            <el-radio-group disabled v-model="reportGroupForm.open_join">
              <el-radio-button label="true">开放加入</el-radio-button>
              <el-radio-button label="false">邀请加入</el-radio-button>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="报告组颜色"
                        prop="color">
            <el-color-picker v-model="reportGroupForm.color"></el-color-picker>
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
  name: "editReportGroup",
  emits: [
    'refreshList'
  ],
  props: [

  ],
  data () {
    let validators = {
      validateGroupName: (rule, value, callback) => {
        api.reportGroup.getReportGroup({
          type: 'check_existence',
          name: value,
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
      dialogMode: null,
      dialogTitle: '创建标签',
      reportGroupForm: {
        id: null,
        name: null,
        open_join: false,
        color: '#FFFFFF',
      },
      formRules: {
        name: [
          { required: true, message: '请输入报告组名', trigger: 'blur' },
          { min: 3, max: 50, message: '报告组名的长度应为3~50个字符', trigger: 'blur' },
          { validator: validators.validateGroupName, trigger: 'blur' }
        ],
      },
      cascaderProps: {
        checkStrictly: true,      // can select parent nodes
        emitPath: false,            // return selected node only
        value: 'id',
        label: 'name',
        children: 'member_node',
      }
    }
  },
  computed: {
    cascaderOptions() {
      return this.$store.state.reportGroup.myReportGroupList;
    },
  },
  methods: {
    handleCreate () {
      this.dialogTitle = "创建报告组";
      this.dialogVisible = true;
      this.dialogMode = 'create';
    },
    handleEdit (elements) {
      this.dialogVisible = true
      for (let item in elements) {
        if (Object.prototype.hasOwnProperty.call(this.reportGroupForm, item)) {
          this.reportGroupForm[item] = elements[item];
        }
      }
      this.dialogTitle = "编辑报告组 - " + this.reportGroupForm.name;
      this.dialogMode = 'modify';
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
      let cAPI = api.reportGroup.addNewGroup;
      if (this.dialogMode === 'modify') {
        cAPI = api.reportGroup.editReportGroup;
      }
      cAPI(dataObj).then((response) => {
        if (response.data.status === 'success') {
          this.$refs.reportGroupForm.resetFields();
          this.dialogVisible = false;
          this.$emit('refreshList');
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
