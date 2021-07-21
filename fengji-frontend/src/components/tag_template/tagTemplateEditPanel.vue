<template>

  <!--  quick nav buttons-->
  <div>
    <el-dialog :title="dialogTitle"
               v-bind:model-value="dialogFormVisible"
               :before-close="handleClose">
      <el-form :model="tagForm"
               status-icon
               :rules="tagFormRules"
               ref="tagForm">
        <el-form-item label="标签名称"
                      prop="tag_template_name">
          <el-input v-model="tagForm.tag_template_name"
                    maxlength="10"
                    show-word-limit></el-input>
        </el-form-item>
        <el-form-item label="标签类型"
                      prop="tag_field_type">
          <el-select v-model="tagForm.tag_field_type"
                     placeholder="请选择标签类型">
            <el-option v-for="item in tagTypeOptions"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="归属标签组"
                      prop="tag_group_assignment">
          <el-select v-model="tagForm.tag_group_assignment"
                     placeholder="请选择归属标签组">
            <el-option v-for="item in tagGroupList"
                       :key="item.id"
                       :label="item.tag_group_name"
                       :value="item.id"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="标签默认值"
                      v-if="tagForm.tag_field_type !== 'simple'"
                      prop="tag_default_value">
          <el-input v-model="tagForm.tag_default_value"></el-input>
        </el-form-item>
        <el-form-item label="标签预览"
                      prop="tag_preview">
          <el-radio-group v-model="tagForm.tag_preview">
            <el-radio-button label="true">可预览</el-radio-button>
            <el-radio-button label="false">无预览</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="必选标签"
                      prop="tag_required">
          <el-radio-group v-model="tagForm.tag_required">
            <el-radio-button label="true">是</el-radio-button>
            <el-radio-button label="false">否</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="标签颜色"
                      prop="tag_color">
          <el-color-picker v-model="tagForm.tag_color"></el-color-picker>
        </el-form-item>
        <el-form-item>
          <el-button type="primary"
                     v-on:click="handleSubmit">提交</el-button>
          <el-button v-on:click="resetForm('tagForm')">重置</el-button>
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
  name: "tagTemplateEditPanel",
  props: [
    'dialogFormVisible',
    'tagGroupList',
    'preSelectedTagGroup',
  ],
  emits: [
    'closeDialog',
    'refreshTagList'
  ],
  data () {
    let validators = {
      validateTagNameUnique: (rule, value, callback) => {
        // use a customized find function to see if the tag name has already existed
        // only do the unique check if dialogMode is not 'modify'
        if (this.dialogMode !== 'modify') {
          api.tag.getTagTemplate({
            type: 'check_existence',
            tag_template_name: value,
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
      // apply different validation rule according to the selected tag_field_type
      validateDefaultValue: (rule, value, callback) => {
        let singleSelectReg = new RegExp("^(.+)(;.+)");
        let numReg = new RegExp("^([0-9]+)(.[0-9]+)?$")
        if (value !== null) {
          switch (this.tagForm.tag_field_type) {
            case 'select':

              if (singleSelectReg.test(value)) {
                callback();
              } else {
                callback(new Error('请使用英文分号(;)分隔各选项'));
              }
              break;
            case 'number':

              if (numReg.test(value)) {
                callback();
              } else {
                callback(new Error('不是有效的数字'));
              }
              break;
            default:
              callback();
              break;
          }
        } else {
          callback()
        }
      },
    }
    return {
      dialogTitle: '创建标签',
      dialogMode: null,
      loadingAnimation: false,
      tagForm: {
        id: null,
        tag_template_name: null,
        tag_field_type: 'simple',
        tag_default_value: null,
        tag_required: false,
        tag_preview: false,
        tag_priority: null,
        tag_group_assignment: null,
        tag_color: '#FFFFFF',
      },
      tagTypeOptions: [
        {
          value: 'simple',
          label: '简单标签'
        },
        {
          value: 'select',
          label: '单选'
        },
        {
          value: 'text',
          label: '文本'
        },
        {
          value: 'number',
          label: '数字'
        },
        // { value: 'date',
        //   label: '日期'
        // },
      ],
      tagFormRules: {
        tag_template_name: [
          { required: true, message: '请输入标签名', trigger: 'blur' },
          { min: 2, max: 10, message: '标签名的长度应为2~10个字符', trigger: 'blur' },
          { validator: validators.validateTagNameUnique, trigger: 'blur' }
        ],
        tag_field_type: [
          { required: true, message: '必须选择一个标签类型', trigger: 'blur' }
        ],
        tag_default_value: [{ validator: validators.validateDefaultValue, trigger: 'blur' }],
        tag_group_assignment: [{ required: true, message: '请选择归属标签组', trigger: 'blur' }]
      },
    };
  },
  computed: {
  },
  methods: {
    handleClose () {
      this.$emit('closeDialog')
    },
    handleSubmit () {
      this.$refs.tagForm.validate((valid) => {
        if (valid) {
          this.submitNewTag()
        }
      })
    },
    submitNewTag () {
      let dataObj = qs.stringify(this.tagForm);
      let cAPI = api.tag.submitNewTag;
      if (this.dialogMode === 'modify') {
        cAPI = api.tag.editTagTemplate
      }
      cAPI(dataObj).then((response) => {
        if (response.data.status === 'success') {
          this.handleClose();
          this.resetForm('tagForm');
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
      }
      )
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    handleEdit (row) {
      // update the tagForm, so each fields will have corresponding default value
      for (let k in row) {
        if (Object.prototype.hasOwnProperty.call(row, k)) {
          this.tagForm[k] = row[k]
        }
      }
      this.dialogTitle = "编辑标签 - " + this.tagForm.tag_template_name
      this.dialogMode = 'modify'
    },
    handleCreate () {
      // handle the create call, prepare the dialog title
      this.dialogTitle = "创建标签"
      this.dialogMode = 'create'
    }
  }
}
</script>

<style scoped>
</style>
