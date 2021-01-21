
<template>
    <div
        class="background_img"
    ></div>

  <div class="main_wrapper">
    <div class="signup-dialog-title">欢迎登陆</div>
    <div class="form_wrapper">
      <el-card
          shadow="always"
      >
        <el-form
          :model="signupForm"
          status-icon
          :rules="rules"
          ref="signupForm"
          label-width="80px"
        >
          <el-form-item label="用户名" prop="username">
            <el-input
              prefix-icon="el-icon-user"
              v-model="signupForm.username"
              placeholder="请输入用户名"

            ></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input
              v-model="signupForm.password"
              prefix-icon="el-icon-key"
              placeholder="请输入密码"
              show-password
            ></el-input>
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
            >登陆
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
      signupForm: {
        username: null,
        password: null,
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
        ],
        password: [
          { required:true, message: '请输入密码', trigger: 'blur' },
        ],
      },

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
    resetForm(formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style>
  .background_img{
    width: 100%;
    height: 100%;
    background-image: url("/bg_signup.jpg");
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
  .form_wrapper{
    width: 50%;
  }
  .el-card{
    background-color: rgba(0,0,0,0.2);
    border: 0;
    margin-top: 20px;
    display: inline-flex;
    justify-items: center;
    width: 100%;
  }
  .el-card__body{
    width: inherit;
  }
  .button{
    margin-top: 20px;
    width: 50%;
  }
  .el-input__inner{
    color: white;
    background-color: transparent;
  }
  .el-form-item__label{
    color: white;
  }
  .obey-agreement{
    color: white;
    margin-top: 20px;
    font-size: 14px;
  }

</style>
