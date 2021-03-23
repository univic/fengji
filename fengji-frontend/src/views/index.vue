<template>
  <el-container>
    <el-header
      style="box-shadow: 0 2px 4px rgba(0,0,0,0.12), 0 0 6px rgba(0, 0, 0, .04);"
    >
      <span>凤集</span>

    </el-header>
    <el-main>
      <div class="main_wrapper">
        <el-image
          src="/bg2.jfif"
          class="bg_img"
        ></el-image>
        <div
          style="height: 500px"
        >

        </div>
        <router-link to="/login">
          <el-button
            style="position: relative; z-index: 1; display: inline"
          >
            登陆
          </el-button>
        </router-link>


        <router-link to="/signup">
          <el-button
            style="position: relative; z-index: 1; display: inline"
          >
            注册
          </el-button>
        </router-link>


      </div>

    </el-main>
    <el-footer class="footer">
      <span>&copy; {{ new Date().getFullYear() }}</span>
      <span
        class="ml-2"
      >鄂ICP备19025675号</span>
    </el-footer>
  </el-container>
</template>

<script>

// TODO: header bar status change according to the login status
// TODO: message icons, etc
export default {
  name: "Index.vue",
  data() {
    return {

    }
  }
}
</script>

<style>

.main_wrapper{
  position: static;
  display: block;
}
.bg_img{
  position: absolute;
  z-index: -1;
  display: block
}

.footer{
  color: white;
  position: static;
  display: inline;
  background-color: #2c3e50;
}

</style>
