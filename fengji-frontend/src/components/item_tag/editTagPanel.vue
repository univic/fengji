<template>

<!--  quick nav buttons-->
  <div>
    <el-dialog
        title="添加标签"
        v-model="dialogFormVisible"
        :before-close="handleClose"
    >
      <el-form
        :model="tagForm"
        status-icon
        :rules="tagFormRules"
        ref="tagForm"
      >
        <el-form-item label="标签名称" prop="tagName">
          <el-input
            v-model="tagForm.tagName"
            maxlength="10"
            show-word-limit
          ></el-input>
        </el-form-item>
        <el-form-item label="标签类型" prop="tagFieldType">
          <el-select
            v-model="tagForm.tagFieldType"
            placeholder="请选择标签类型"
          >
            <el-option
              v-for="item in tagTypeOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="标签默认值"
          v-if="tagForm.tagFieldType !== 'simple'"
          prop="tagDefaultValue"
        >
          <el-input v-model="tagForm.tagDefaultValue"></el-input>
        </el-form-item>
        <el-form-item label="标签预览"  prop="tagPreview">
          <el-radio-group v-model="tagForm.tagPreview">
            <el-radio-button label="true">可预览</el-radio-button>
            <el-radio-button label="false">无预览</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="必选标签"  prop="tagRequired">
          <el-radio-group v-model="tagForm.tagRequired">
            <el-radio-button label="true">是</el-radio-button>
            <el-radio-button label="false">否</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="标签颜色"  prop="tagColor">
          <el-color-picker v-model="tagForm.tagColor"></el-color-picker>
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            v-on:click="handleSubmit"
          >创建标签</el-button>
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
  name: "editTagPanel",
  props: [
    'dialogFormVisible',
  ],
  emits: [
      'closeDialog'
  ],
  data () {
    let validators = {
      validateTagNameUnique: (rule, value, callback) => {
        // use a customized find function to see if the tag name has already existed
        api.tag.getTagList({
          type: 'check_existence',
          tag_name: value,
        }).then(
            function (response) {
              if (response.data.status === 'success') {
                callback()

              } else if (response.data.status === 'error') {
                callback(new Error(response.data.messages[0]))
              }
              else {
                ElMessage({
                  message: '出现了问题（*゜ー゜*）',
                  type: 'error',
                })
              }
            }
        ).catch(
            function (error) {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + error.message,
                type: 'error'
              })
            }
          )
      },
      // apply different validation rule according to the selected tagFieldType
      validateDefaultValue: (rule, value, callback) => {
        console.log(value)
        if (value !== null) {
          switch (this.tagForm.tagFieldType) {
            case 'select':
              let singleSelectReg = new RegExp("^(.+)(;.+)");
              if (singleSelectReg.test(value)) {
                callback();
              } else {
                callback(new Error('请使用英文分号(;)分隔各选项'));
              }
              break;
            case 'number':
              let numReg = new RegExp("^([0-9]+)(.[0-9]+)?$")
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
      loadingAnimation: false,
      tagForm: {
        tagName: null,
        tagFieldType: 'simple',
        tagDefaultValue: null,
        tagRequired: false,
        tagPreview: false,
        tagPriority: null,
        tagColor: '#FFFFFF',
      },
      tagTypeOptions:[
        { value: 'simple',
          label: '简单标签'
        },
        { value: 'select',
          label: '单选'
        },
        { value: 'text',
          label: '文本'
        },
        { value: 'number',
          label: '数字'
        },
        // { value: 'date',
        //   label: '日期'
        // },
      ],
      tagFormRules: {
        tagName: [
          {required: true, message: '请输入标签名', trigger: 'blur'},
          {min: 2, max: 10, message: '标签名的长度应为2~10个字符', trigger: 'blur'},
          {validator: validators.validateTagNameUnique, trigger: 'blur'}
        ],
        tagFieldType: [
          {required: true, message: '必须选择一个标签类型', trigger: 'blur'}
        ],
        tagDefaultValue: [{validator: validators.validateDefaultValue, trigger: 'blur'}]
      },
    };
  },
  methods: {
    handleClose() {
      this.$emit('closeDialog')
    },
    handleSubmit() {
      this.$refs.tagForm.validate((valid) => {
        if (valid) {
          this.submitNewTag()
        } else {

          
        }
      })
    },
    submitNewTag() {
      let dataObj = qs.stringify(this.tagForm);
      api.tag.submitNewTag(dataObj).then((response) => {
          if (response.data.status === 'success') {
            this.handleClose()
            this.resetForm('tagForm')
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
      ).catch(
          function (error) {
            ElMessage({
              message: '出现了问题（*゜ー゜*）' + error,
              type: 'error'
            });
          }
      )
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    // handleEdit(tagEditForm) {
    //   for (let k in tagEditForm) {
    //     if (tagEditForm.hasOwnProperty(k)) {
    //       this.tagForm[k] = tagEditForm[k]
    //     }
    //   }
    // }
  }
}
</script>

<style scoped>

</style>
