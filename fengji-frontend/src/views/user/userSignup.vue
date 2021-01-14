<template>
    <div
        class="background_img"
    ></div>

  <div class="main_wrapper">
    <div >
      <div>signup</div>
      <el-card
          shadow="always"
      >
        <el-input
            prefix-icon="el-icon-user"
        ></el-input>
        <el-input
            prefix-icon="el-icon-key"
        ></el-input>
        <el-button
          type="primary"
          class="button"
        >注册
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
    }
  }
}
</script>

<style>
  .background_img{
    width: 100%;
    height: 100%;
    background-image: url("http://diskstation:5000/webman/login_background.jpg?id=1");
    background-size: 100% 100%;
    background-position: 0px 0px;
    margin: 0;
    background-repeat: no-repeat;
    z-index: -1;
    position: absolute;
  }
  .main_wrapper{
    z-index: 1;
    display: flex;
    justify-content: center;
    justify-items: center;

  }
  .signup-dialog-title{

  }
  .el-card{
    background-color: rgba(255,255,255,0.3);
    border: 0px;

  }
  .button{
    margin-top: 20px;
    width: 75%;
  }
  .el-input__inner{

    border-bottom: 3px white;
    background-color: transparent;
  }

</style>
