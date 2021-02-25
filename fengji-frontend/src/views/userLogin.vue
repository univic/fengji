
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
          :model="loginForm"
          status-icon
          :rules="rules"
          ref="loginForm"
          label-width="80px"
        >
          <el-form-item label="用户名" prop="username">
            <el-input
              prefix-icon="el-icon-user"
              v-model="loginForm.username"
              placeholder="请输入用户名"

            ></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input
              v-model="loginForm.password"
              prefix-icon="el-icon-key"
              placeholder="请输入密码"
              show-password
            ></el-input>
          </el-form-item>

          <el-form-item>
            <el-button
              type="primary"
              class="button"
              v-on:click="handleSubmit"
            >登陆
            </el-button>
          </el-form-item>

        </el-form>
      </el-card>
    </div>

  </div>



</template>

<script>

import qs from 'qs'
import axios from "axios"
import jwtDecode from 'jwt-decode'
import {ElMessage} from "element-plus"

export default {
  name: "userLogin",
  components: {
  },
  data() {

    return {
      loginForm: {
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
  computed: {

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
      let dataObj = qs.stringify(this.loginForm)
      axios.post(
        'http://localhost:5000/api/user/login',
        dataObj,
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          }
        }).then(
          (response) => {
            if (response.data.status === 'success') {
              window.localStorage.setItem('access_token', response.data.access_token)
              let decodedJWT = jwtDecode(response.data.access_token)
              this.$store.commit('user/SET_USER_IDENTITY', decodedJWT.sub)
              this.$router.push('/user')
            } else if (response.data.status === 'error') {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
              })
            } else {
              ElMessage({
                message: '出现了问题（*゜ー゜*）' + response.data.messages[0],
                type: 'error'
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
    handleSubmit() {
      this.$refs.loginForm.validate(
        (valid) => {
          if (valid) {
            this.submitForm()
          }
        }
      )

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

</style>
