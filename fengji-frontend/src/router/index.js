import { defineAsyncComponent } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import userRouter from "./userRouter"
import store from '../store';
import jwtDecode from 'jwt-decode';

let routerOptions = [
  { path: '/', component: () => import('../views/index.vue') },
  { path: '/home', component: () => import('../views/Home.vue') },
  { path: '/:pathMatch(.*)', component: () => import('../views/404.vue') },
]

routerOptions.splice(routerOptions.length - 1, 0, ...userRouter)

const Router = createRouter({
  history: createWebHistory(),
  routes: routerOptions      // short for routes: routes
})

// before each routing, check if there is a valid access token
Router.beforeEach((to, from) => {
  let accessToken = window.localStorage.getItem('access_token');
  if (accessToken === null) {
    if (to.path === '/login' || to.path === '/signup') {
      return true;
    } else {
      return '/login';
    }
  } else {
    let decodedJWT = jwtDecode(accessToken);
    store.commit('user/SET_USER_IDENTITY', decodedJWT.sub);
    return true;
  }
})

export default Router
