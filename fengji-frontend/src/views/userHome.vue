<template>
  <el-container>
    <el-header>
      <div style="display: flex">
        <!--      logo here-->
        <div style="width: 20%">LOGO HERE</div>
        <!--      menu bar here-->
        <div style="width: 50%; justify-items: flex-end">
          <el-menu mode="horizontal">
            <el-menu-item index="1">工作台</el-menu-item>
            <el-submenu index="2">
              <template #title>总览</template>
              <el-menu-item index="2-1">选项1</el-menu-item>
              <el-menu-item index="2-2">选项2</el-menu-item>
            </el-submenu>
            <el-menu-item index="3">个人中心</el-menu-item>
          </el-menu>
        </div>

        <!--      avatar, username and user menu, etc-->
        <div style="width: 20%">
          <span>
            <el-avatar :size="50"
                       src="/default_avatar.png"></el-avatar>
          </span>
          <router-link to="/login">
            <span>{{ userIdentity }}</span>
          </router-link>
        </div>
      </div>
    </el-header>
    <el-container>
      <el-aside>
        <el-menu router>
          <el-menu-item index="/user/guide">
            <i class="el-icon-guide"></i>
            <span>用户向导</span>
          </el-menu-item>
          <el-menu-item index="/user/workbench">
            <i class="el-icon-notebook-2"></i>
            <span>工作台</span>
          </el-menu-item>
          <el-menu-item index="/user/edit_tag_template">
            <i class="el-icon-collection-tag"></i>
            <span>标签管理</span>
          </el-menu-item>

          <el-menu-item index="/user/my_report_group">
            <i class="el-icon-files"></i>
            <span>我的报告组</span>
          </el-menu-item>
          <el-submenu>
            <template #title>
              <i class="el-icon-location"></i>
              <span>数据管理</span>
            </template>
            <el-menu-item index="/user/manage_group_role">
              <i class="el-icon-s-custom"></i>
              <span>报告组角色管理</span>
            </el-menu-item>
            <el-menu-item index="/user/manage_report_group">
              <i class="el-icon-edit"></i>
              <span>报告组管理</span>
            </el-menu-item>
          </el-submenu>

          <el-menu-item index="/user/item_list">
            <i class="el-icon-info"></i>
            <span>关于</span>
          </el-menu-item>
        </el-menu>

      </el-aside>
      <el-container>
        <el-main>
          <router-view></router-view>
        </el-main>
        <el-footer>
          <span>&copy; {{ new Date().getFullYear() }}</span>
          <span class="ml-2">鄂ICP备19025675号</span>
        </el-footer>
      </el-container>

    </el-container>
  </el-container>
</template>

<script>

export default {
  name: "userHome",
  data () {
    return {
      tagTemplateList: null,
    }
  },
  components: {
  },
  computed: {
    userIdentity () {
      return this.$store.state.user.userIdentity.username
    },
  }
}
</script>

<style scoped>
</style>
