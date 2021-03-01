<template>

<!--  quick nav buttons-->
  <div>
    <el-dialog
        title="添加标签"
        v-model="dialogFormVisible"
        :before-close="handleClose"
    >
      <el-form
        :model="newTagForm"
        status-icon
        :rules="tagFormRules"
        ref="newTagForm"
      >
        <el-form-item label="标签名称" prop="tagName">
          <el-input
            v-model="newTagForm.tagName"
            maxlength="10"
            show-word-limit
          ></el-input>
        </el-form-item>
        <el-form-item label="标签类型" prop="tagFieldType">
          <el-select
            v-model="newTagForm.tagFieldType"
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
          v-if="newTagForm.tagFieldType !== 'simple'"
          prop="tagDefaultValue"
        >
          <el-input v-model="newTagForm.tagDefaultValue"></el-input>
        </el-form-item>
        <el-form-item label="标签预览"  prop="tagPreview">
          <el-radio-group v-model="newTagForm.tagPreview">
            <el-radio-button label="true">可预览</el-radio-button>
            <el-radio-button label="false">无预览</el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="标签颜色"  prop="tagColor">
          <el-color-picker v-model="newTagForm.tagColor"></el-color-picker>
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            v-on:click="handleSubmit"
          >创建标签</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import qs from 'qs';
import myAxios from '../../utilities/request';
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
        function getTagName(tagItem) {
          return tagItem.tagName === value;
        }

        let searchResult = this.tagList.find(getTagName)
        if (typeof (searchResult) === 'undefined') {
          callback();
        } else {
          callback(new Error('标签名已存在'));
        }
      },
      // apply different validation rule according to the selected tagFieldType
      validateDefaultValue: (rule, value, callback) => {
        console.log(value)
        if (value !== null) {
          switch (this.newTagForm.tagFieldType) {
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
      newTagForm: {
        tagName: null,
        tagFieldType: 'simple',
        tagDefaultValue: null,
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
      tagList: [
        {tagName: '123'}
      ],
    };
  },
  computed: {

  },
  methods: {
    handleClose() {
      this.$emit('closeDialog')
    },
    handleSubmit() {
      this.$refs.newTagForm.validate((valid) => {
        if (valid) {
          this.submitNewTag()
        } else {

        }
      })
    },
    submitNewTag() {
      let dataObj = qs.stringify(this.newTagForm);
      myAxios.post(
          '/api/item_tag/',
          dataObj,
          {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            }
          }).then(
              function (response) {
                if (response.data.status === 'success') {
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
  }
}
</script>

<style scoped>

</style>
