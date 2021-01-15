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
        <el-input
            prefix-icon="el-icon-user"
            v-model="inputUsername"
            placeholder="请输入用户名"

        ></el-input>
        <el-input
            v-model="inputPassword"
            prefix-icon="el-icon-key"
            placeholder="请输入密码"
            show-password
        ></el-input>
        <el-input
            v-model="inputRetypePassword"
            prefix-icon="el-icon-key"
            placeholder="请重复一次密码"
            show-password
        ></el-input>
        <el-input
            prefix-icon="el-icon-message"
            v-model="inputEmail"
            placeholder="请输入联系邮箱"
        ></el-input>
        <el-checkbox
          v-model="obeyAgreement"
          style="display: block"
        >同意使用协议</el-checkbox>
        <el-button
            type="primary"
            class="button"
        >提交
        </el-button>
      </el-card>
    </div>

  </div>



</template>

<script>

export default {
  name: "userSignup",
  data() {
    return {
      inputUsername: null,
      inputPassword: null,
      inputRetypePassword: null,
      inputEmail: null,
      obeyAgreement: null,
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
    background-color: rgba(255,255,255,0.4);
    border: 0px;
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
    border-bottom: 3px white;
    background-color: transparent;
  }
  .el-input{
    margin-top: 20px;
  }

</style>
