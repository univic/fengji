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
                      prop="name">
          <el-input v-model="tagForm.name"
                    maxlength="10"
                    show-word-limit></el-input>
        </el-form-item>
        <el-form-item label="标签类型"
                      prop="field_type">
          <el-select v-model="tagForm.field_type"
                     placeholder="请选择标签类型">
            <el-option v-for="item in tagTypeOptions"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="归属标签组"
                      prop="tag_group_assignment">
          <el-cascader v-model="tagForm.tag_group_assignment"
                       placeholder="请选择归属标签组"
                       v-bind:options="tagTemplateGroup"
                       v-bind:props="tagGroupCascaderProps"
          >
          </el-cascader>
        </el-form-item>
        <el-form-item label="标签默认值"
                      v-if="tagForm.field_type !== 'simple'"
                      prop="default_value">
          <el-input v-model="tagForm.default_value"></el-input>
        </el-form-item>
        <el-form-item label="标签预览"
                      prop="preview">
          <el-radio-group v-model="tagForm.preview">
            <el-radio-button label="true">可预览</el-radio-button>
            <el-radio-button label="false">无预览</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="必选标签"
                      prop="required">
          <el-radio-group v-model="tagForm.required">
            <el-radio-button label="true">是</el-radio-button>
            <el-radio-button label="false">否</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="标签颜色"
                      prop="color">
          <el-color-picker v-model="tagForm.color"></el-color-picker>
        </el-form-item>
        <el-form-item>
          <el-button type="primary"
                     v-on:click="handleSubmit">提交
          </el-button>
          <el-button v-on:click="resetForm('tagForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import qs from 'qs';
import api from '../../api';
import message from "../../utilities/message";

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
  data() {
    let validators = {
      validateTagNameUnique: (rule, value, callback) => {
        // use a customized find function to see if the tag name has already existed
        // only do the unique check if dialogMode is not 'modify'
        if (this.dialogMode !== 'modify') {
          api.tagTemplate.getTagTemplate({
            type: 'check_existence',
            name: value,
          }).then((response) => {
            if (response.data.status === 'success') {
              callback();
            } else {
              callback(new Error(response.data.messages[0]));
            }
          }
          );
        }
      },
      // apply different validation rule according to the selected field_type
      validateDefaultValue: (rule, value, callback) => {
        let singleSelectReg = new RegExp("^(.+)(;.+)");
        let numReg = new RegExp("^([0-9]+)(.[0-9]+)?$");
        if (value !== null) {
          switch (this.tagForm.field_type) {
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
          callback();
        }
      },
    };
    return {
      dialogTitle: '创建标签',
      dialogMode: null,
      loadingAnimation: false,
      tagForm: {
        id: null,
        name: null,
        field_type: 'simple',
        default_value: null,
        required: false,
        preview: false,
        tag_priority: null,
        tag_group_assignment: null,
        color: '#FFFFFF',
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
        name: [
          {required: true, message: '请输入标签名', trigger: 'blur'},
          {min: 2, max: 10, message: '标签名的长度应为2~10个字符', trigger: 'blur'},
          {validator: validators.validateTagNameUnique, trigger: 'blur'}
        ],
        field_type: [
          {required: true, message: '必须选择一个标签类型', trigger: 'blur'}
        ],
        default_value: [{validator: validators.validateDefaultValue, trigger: 'blur'}],
        tag_group_assignment: [{required: true, message: '请选择归属标签组', trigger: 'blur'}]
      },
      tagGroupCascaderProps: {
        checkStrictly: true,      // can select parent nodes
        emitPath: false,            // return selected node only
        value: 'id',
        label: 'name',
        children: 'child_group',
      }
    };
  },
  computed: {
    tagTemplateGroup() {
      return this.$store.getters['tagTemplateGroup/getTagTemplateGroupList'];
    }
  },
  methods: {
    handleClose() {
      this.$emit('closeDialog');
    },
    handleSubmit() {
      this.$refs.tagForm.validate((valid) => {
        if (valid) {
          this.submitNewTag();
        }
      });
    },
    submitNewTag() {
      let dataObj = qs.stringify(this.tagForm);
      let cAPI = api.tagTemplate.submitNewTag;
      if (this.dialogMode === 'modify') {
        cAPI = api.tagTemplate.editTagTemplate;
      }
      cAPI(dataObj).then((response) => {
            if (response.data.status === 'success') {
              this.handleClose();
              this.resetForm('tagForm');
              message.emitSuccessMessage(response.data.messages[0])
              this.$emit('refreshTagList');
            }
          }
      );
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    handleEdit(tagTemplateElement) {
      // update the tagForm, so each fields will have corresponding default value
      for (let k in tagTemplateElement) {
        if (Object.prototype.hasOwnProperty.call(tagTemplateElement, k)) {
          this.tagForm[k] = tagTemplateElement[k];
        }
      }
      this.dialogTitle = "编辑标签 - " + this.tagForm.name;
      this.dialogMode = 'modify';
    },
    handleCreate() {
      // handle the create call, prepare the dialog title
      this.dialogTitle = "创建标签";
      this.dialogMode = 'create';
    }
  }
};
</script>

<style scoped>
</style>
