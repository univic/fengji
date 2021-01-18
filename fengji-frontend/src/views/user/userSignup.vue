
<template>
    <div
        class="background_img"
    ></div>

  <div class="main_wrapper">
    <div class="signup-dialog-title">注册</div>
    <div>
      <el-card
          shadow="always"
      >

        <el-form
          :model="ruleForm"
          status-icon
          :rules="rules"
          ref="ruleForm"
        >
          <el-form-item label="用户名" prop="username">
            <el-input
              prefix-icon="el-icon-user"
              v-model="ruleForm.username"
              placeholder="请输入用户名"

            ></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input
              v-model="ruleForm.password"
              prefix-icon="el-icon-key"
              placeholder="请输入密码"
              show-password
            ></el-input>
          </el-form-item>
          <el-form-item label="确认密码">
            <el-input
              v-model="ruleForm.confirmPassword"
              prefix-icon="el-icon-key"
              placeholder="请重复一次密码"
              show-password
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-input
              prefix-icon="el-icon-message"
              v-model="ruleForm.email"
              placeholder="请输入联系邮箱"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-checkbox
              v-model="ruleForm.obeyAgreement"
              style="display: block"
              class="obey-agreement"
            >同意使用协议</el-checkbox>
          </el-form-item>
          <div
            class="h-captcha"
            data-sitekey="f1e8fd67-87db-4474-b654-ac89b61d9fe3"
            data-theme="dark"
          ></div>
          <el-form-item>
            <el-button
              type="primary"
              class="button"
            >提交
            </el-button>
          </el-form-item>

        </el-form>




      </el-card>
    </div>

  </div>



</template>

<script>

export default {
  name: "userSignup",
  data() {
    return {
      ruleForm: {
        username: null,
        password: null,
        confirmPassword: null,
        email: null,
        obeyAgreement: null,
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min:3, max: 5, message: '请输入用户名', trigger: 'blur' },
        ],
        password: [
          { required:true, message: '请输入密码', trigger: 'blur' },
          { min:6, max: 32, message: '密码长度应为6~32位', trigger: 'blur' },
        ],
        confirmPassword: [
          { required:true, message: '请再输入一次密码', trigger: 'blur' },
        ],
        email: [
          { required:true, message: '邮件地址', trigger: 'blur' },
        ]
      }
    }
  },
  mounted: function (){
    this.createCaptcha()
  },
  methods: {
    createCaptcha() {
      const captchaScript = document.createElement('script')
      captchaScript.type = 'text/javascript'
      captchaScript.src = 'https://hcaptcha.com/1/api.js'
      captchaScript.async
      captchaScript.defer
      document.body.appendChild(captchaScript)
    },
    submitForm() {

    },
    resetForm() {

    }
  }
}
</script>

<style>
  .background_img{
    width: 100%;
    height: 100%;
    background-image: url("/bg1.jpg");
    background-size: cover;
    background-position: 0px 0px;
    margin: 0;
    background-repeat: no-repeat;
    z-index: -1;
    position: absolute;
  }
  .main_wrapper{
    z-index: 1;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    justify-items: center;
    justify-self: center;

  }
  .signup-dialog-title{
    font-size: 24px;
    color: white;
    margin-top: 60px;
    width: 100%;
  }
  .el-card{
    background-color: rgba(0,0,0,0.5);
    border: 0;
    margin-top: 20px;
    width: 50%;
    display: inline-flex;

  }
  .button{
    margin-top: 20px;
    width: 50%;
  }
  .el-input__inner{
    color: white;
    background-color: transparent;
  }
  .el-input{
    margin-top: 20px;
  }
  .obey-agreement{
    color: white;
    margin-top: 20px;
    font-size: 14px;
  }

</style>
