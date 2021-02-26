<template>
<!--  title here-->
  <div>标签管理</div>
<!--  quick nav buttons-->
  <div>
    <el-button
      v-on:click="dialogFormVisible = true"
    >添加标签</el-button>
    <el-dialog title="添加标签" v-model="dialogFormVisible">
      <el-form v-model="newTagForm">
        <el-form-item label="标签名称">
          <el-input v-model="newTagForm.tag_name"></el-input>
        </el-form-item>
        <el-form-item label="标签类型">
          <el-select v-model="newTagForm.tag_field_type" placeholder="请选择标签类型">
            <el-option
              v-for="item in tagTypeOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>

        </el-form-item>
        <el-form-item label="标签预览">
          <el-radio-group v-model="newTagForm.tag_for_preview">
            <el-radio-button label="true">可预览</el-radio-button>
            <el-radio-button label="false">无预览</el-radio-button>
          </el-radio-group>

        </el-form-item>
        <el-form-item label="标签颜色">
          <el-color-picker v-model="newTagForm.tag_color" disabled></el-color-picker>
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            v-on:click=""
          >创建标签</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "userGuide",
  data () {
    return {
      loadingAnimation: false,
      dialogFormVisible: false,
      newTagForm: {
        tag_name: null,
        tag_field_type: null,
        tag_field_default_value: null,
        tag_for_preview: null,
        tag_priority: null,
        tag_color: null,
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
        { value: 'date',
          label: '日期'
        },
      ],
      tagList: null,
    };
  },
  computed: {

  },
  methods: {

  }
}
</script>

<style scoped>

</style>
