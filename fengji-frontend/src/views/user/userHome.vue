<template>
  <el-container>
    <el-header>
      <el-menu
        mode="horizontal"
      >
        <el-menu-item index="1">工作台</el-menu-item>
        <el-submenu index="2">
          <template #title>总览</template>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
        </el-submenu>
        <el-menu-item index="3">个人中心</el-menu-item>
      </el-menu>
    </el-header>
    <el-container>
      <el-aside>
        <el-menu>
          <el-submenu index="1">
            <template v-slot:title>
              <i class="el-icon-location"></i>
              <span>导航一</span>
            </template>

          </el-submenu>
        </el-menu>

      </el-aside>
      <el-container>
        <el-main>
            <ItemList
            ></ItemList>
        </el-main>
        <el-footer>
          <span>&copy; {{ new Date().getFullYear() }}</span>
          <span
              class="ml-2"
          >鄂ICP备19025675号</span>
        </el-footer>
      </el-container>

    </el-container>
  </el-container>
</template>

<script>

import ItemList from "../../components/ItemList.vue";

export default {
  name: "userHome",
  components: {
    ItemList,
  }
}
</script>

<style scoped>

</style>
