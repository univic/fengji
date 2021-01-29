<template>
<!--  title here-->
  <div>用户向导</div>
<!--  quick nav buttons-->
  <div>
    <el-row :gutter="12">
      <el-col
        :span="8">
        <el-card shadow="hover">
          <i class="el-icon-plus"></i>
          <span>新建项目/报告组</span>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover">
          <i class="el-icon-plus"></i>
          <span>加入项目/报告组</span>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover">
          <i class="el-icon-edit"></i>
          <span>编辑事务标签</span>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "userGuide"
}
</script>

<style scoped>

</style>
