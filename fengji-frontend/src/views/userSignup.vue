
<template>
    <div
        class="background_img"
    ></div>

  <div class="main_wrapper">
    <div class="signup-dialog-title">注册</div>
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
          <el-form-item label="确认密码" prop="confirm_password">
            <el-input
              v-model="signupForm.confirm_password"
              prefix-icon="el-icon-key"
              placeholder="请重复一次密码"
              show-password
            ></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input
              prefix-icon="el-icon-message"
              v-model="signupForm.email"
              placeholder="请输入联系邮箱"
            ></el-input>
          </el-form-item>
          <el-form-item prop="accept_agreement">
            <el-checkbox
              v-model="signupForm.accept_agreement"
              style="display: block"
              class="obey-agreement"
            >同意使用协议</el-checkbox>
          </el-form-item>
<!--          <div
            class="h-captcha"
            data-sitekey="f1e8fd67-87db-4474-b654-ac89b61d9fe3"
            data-theme="dark"
          ></div>-->
          <el-form-item>
            <el-button
              type="primary"
              class="button"
              v-on:click="handleSubmit"
            >提交
            </el-button>
            <el-button
              v-on:click="resetForm('signupForm')"
            >重置</el-button>
          </el-form-item>

        </el-form>
      </el-card>
    </div>

  </div>



</template>

<script>

import qs from 'qs';
import api from "../api"
import { ElMessage } from 'element-plus';

export default {
  name: "userSignup",
  data() {
    let validators = {
      validateUsernameUnique: (rule, value, callback) => {
        axios.get('http://localhost:5000/api/user/check_username_unique', {
          params: {
            'username': value
          }
        }).then(
            function (response) {
              if (response.data.status === 'success') {
                callback()
              } else if (response.data.status === 'error') {
                callback(new Error(response.data.messages[0]))
              }
              else {
                ElMessage({
                  message: '出现了问题（*゜ー゜*） 无法查询到用户名是否可用',
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
      validateConfirmPassword: (rule, value, callback) => {
        if (value !== this.signupForm.password) {
          callback(new Error('密码不一致'))
        } else {
          callback()
        }
      },
      validateEmail: (rule, value, callback) => {
        let emailReg = new RegExp("([0-9A-Za-z\\-_\\.]+)@([0-9a-z]+\\.[a-z]{2,3}(\\.[a-z]{2})?)$")
        if (emailReg.test(value)) {
          callback()
        } else {
          callback(new Error('不是有效的电子邮件地址'))
        }
      },
      validateAcceptAgreement: (rule, value, callback) => {
        if (value) {
          callback()
        } else {
          callback(new Error('需要同意用户协议'))
        }
      }
    }

    return {
      signupForm: {
        username: null,
        password: null,
        confirm_password: null,
        email: null,
        accept_agreement: false,
      },
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
          {min: 3, max: 30, message: '用户名的长度应为3~25个字符', trigger: 'blur'},
          {validator: validators.validateUsernameUnique, trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
          {min: 6, max: 32, message: '密码长度应为8~32位字符', trigger: 'blur'},
        ],
        confirm_password: [
          {required: true, message: '请再输入一次密码', trigger: 'blur'},
          {validator: validators.validateConfirmPassword, trigger: 'blur'}
        ],
        email: [
          {required: true, message: '请输入邮件地址', trigger: 'blur'},
          {validator: validators.validateEmail, trigger: 'blur'},
        ],
        accept_agreement: [
          {validator: validators.validateAcceptAgreement, trigger: 'blur'}
        ]
      },

    }
  },

  mounted: function () {
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
      let dataObj = qs.stringify(this.signupForm);
      api.user.addUser(dataObj).then(
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
    resetForm(formName) {
      this.$refs[formName].resetFields()
    },
    handleSubmit() {
      this.$refs.signupForm.validate((valid) => {
        if (valid) {
          this.submitForm()
        } else {

        }
      })
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
    background-position: 0 0;
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
    background-color: rgba(0,0,0,0.5);
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
