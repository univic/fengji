import { defineAsyncComponent } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import userRouter from "./userRouter"

let routerOptions = [
  { path: '/', component: 'index' },
  { path: '/home', component: 'Home' },
  { path: '/:pathMatch(.*)', component: '404' },
]

routerOptions.splice(routerOptions.length - 1, 0, ...userRouter)

/*
将=>箭头函数map至routerOption数组的各个元素中，
箭头函数接收routerOption数组元素，通过spread运算符（三个点）拿到其中内容
通过import拿到对应模板，替换掉component
*/

const routes = routerOptions.map(
  route => {
    return {
      ...route,
      component: () =>
        import(`../views/${route.component}.vue`)

    }
  }
)


const Router = createRouter({
  history: createWebHistory(),
  routes      // short for routes: routes
})


export default Router
